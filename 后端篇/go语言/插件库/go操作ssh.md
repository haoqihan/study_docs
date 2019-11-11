样例

```go
package main

import (
	"fmt"
	gossh "golang.org/x/crypto/ssh"
	"io"
	"log"
	"net"
	"os"
	"strings"
	"sync"
)

// DpiCli 连接服务器信息
type DpiCli struct {
	User   string
	Pwd    string
	Addr   string
	client *gossh.Client
}

// Connect 连接服务器
func (c *DpiCli) Connect() (*DpiCli, error) {
	config := &gossh.ClientConfig{}
	config.SetDefaults()
	config.User = c.User
	config.Auth = []gossh.AuthMethod{gossh.Password(c.Pwd)}
	config.HostKeyCallback = func(hostname string, remote net.Addr, key gossh.PublicKey) error { return nil }
	client, err := gossh.Dial("tcp", c.Addr, config)
	if nil != err {
		return c, err
	}
	c.client = client
	return c, nil
}

// SendShell 执行普通的shell命令
func (c DpiCli) SendShell(shell string) (string, error) {
	if c.client == nil {
		if _, err := c.Connect(); err != nil {
			return "", err
		}
	}
	session, err := c.client.NewSession()
	if err != nil {
		return "", err
	}
	defer func() {
		if err := session.Close();err != nil{
			panic(err)
		}
	}()

	buf, err := session.CombinedOutput(shell)
	return string(buf), err
}

// SendString 执行其他非shell的命令
func (c DpiCli) SendString(analysis []string) (string, error) {
	if c.client == nil {
		if _, err := c.Connect(); err != nil {
			return "", err
		}
	}
	session, err := c.client.NewSession()
	if err != nil {
		return "", err
	}
	defer func() {
		if err := session.Close();err != nil{
			panic(err)
		}
	}()

	checkError(err, "创建shell")

	modes := gossh.TerminalModes{
		gossh.ECHO:          1,     // disable echoing
		gossh.TTY_OP_ISPEED: 14400, // input speed = 14.4kbaud
		gossh.TTY_OP_OSPEED: 14400, // output speed = 14.4kbaud
	}

	if err := session.RequestPty("xterm", 80, 40, modes); err != nil {
		log.Fatal(err)
	}
	w, err := session.StdinPipe()
	if err != nil {
		panic(err)
	}
	r, err := session.StdoutPipe()
	if err != nil {
		panic(err)
	}
	e, err := session.StderrPipe()
	if err != nil {
		panic(err)
	}
	in, out := MuxShell(w, r, e)
	if err := session.Shell(); err != nil {
		log.Fatal(err)
	}
	<-out // ignore the shell output
	for _,v := range analysis{
		in <- v
	}

	fmt.Println(<-out,<-out)
	return "",err
}

// MuxShell 发送内容
func MuxShell(w io.Writer, r, e io.Reader) (chan<- string, <-chan string) {
	in := make(chan string, 100)
	out := make(chan string, 100)
	var wg sync.WaitGroup
	wg.Add(1) //for the shell itself
	go func() {
		for cmd := range in {
			wg.Add(1)
			ints,err := w.Write([]byte(cmd + "\r"))
			fmt.Println(ints,err)
			wg.Wait()
		}
	}()

	go func() {
		var (
			buf [4096 * 1024]byte
			t   int
		)
		for {
			n, err := r.Read(buf[t:])
			if err != nil {
				fmt.Println(err.Error())
				close(in)
				close(out)
				return
			}
			t += n
			result := string(buf[:t])
			if strings.HasSuffix(strings.TrimSpace(result), "#") ||
				strings.HasSuffix(strings.TrimSpace(result), "：") ||
				strings.HasSuffix(strings.TrimSpace(result), "nt:") ||
				strings.HasSuffix(strings.TrimSpace(result), "$") {
				out <- string(buf[:t])
				t = 0
				wg.Done()
			}
		}
	}()
	return in, out
}
// 处理错误信息
func checkError(err error, info string) {
	if err != nil {
		fmt.Printf("%s. error: %s\n", info, err)
		os.Exit(1)
	}
}



func main() {
	commandList := []string{"cd /","ls"}
	cli := DpiCli{
		User:"root",
		Pwd:"",
		Addr:"39.105.162.164:22",
	}
	_,err := cli.SendString(commandList)
	fmt.Println(err)
}

```

