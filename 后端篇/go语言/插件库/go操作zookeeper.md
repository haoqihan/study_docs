## 1.基础操作测试

简单的例子来测试下基本的操作：

```go
package main

/**
客户端doc地址：github.com/samuel/go-zookeeper/zk
**/
import (
    "fmt"
    "time"

    zk "github.com/samuel/go-zookeeper/zk"
)

/**
 * 获取一个zk连接
 * @return {[type]}
 */
func getConnect(zkList []string) (conn *zk.Conn) {
    conn, _, err := zk.Connect(zkList, 10*time.Second)
    if err != nil {
        fmt.Println(err)
    }
    return
}

/**
 * 测试连接
 * @return
 */
func test1() {
    zkList := []string{"localhost:2181"}
    conn := getConnect(zkList)

    defer conn.Close()
    var flags int32 = 0
    //flags有4种取值：
    //0:永久，除非手动删除
    //zk.FlagEphemeral = 1:短暂，session断开则改节点也被删除
    //zk.FlagSequence  = 2:会自动在节点后面添加序号
    //3:Ephemeral和Sequence，即，短暂且自动添加序号
    conn.Create("/go_servers", nil, flags, zk.WorldACL(zk.PermAll)) // zk.WorldACL(zk.PermAll)控制访问权限模式

    time.Sleep(20 * time.Second)
}

/*
删改与增不同在于其函数中的version参数,其中version是用于 CAS支持
func (c *Conn) Set(path string, data []byte, version int32) (*Stat, error)
func (c *Conn) Delete(path string, version int32) error

demo：
if err = conn.Delete(migrateLockPath, -1); err != nil {
    log.Error("conn.Delete(\"%s\") error(%v)", migrateLockPath, err)
}
*/

/**
 * 测试临时节点
 * @return {[type]}
 */
func test2() {
    zkList := []string{"localhost:2181"}
    conn := getConnect(zkList)

    defer conn.Close()
    conn.Create("/testadaadsasdsaw", nil, zk.FlagEphemeral, zk.WorldACL(zk.PermAll))

    time.Sleep(20 * time.Second)
}

/**
 * 获取所有节点
 */
func test3() {
    zkList := []string{"localhost:2181"}
    conn := getConnect(zkList)

    defer conn.Close()

    children, _, err := conn.Children("/go_servers")
    if err != nil {
        fmt.Println(err)
    }
    fmt.Printf("%v \n", children)
}

func main() {
    test3()
}
```

## 2.简单的分布式server

### 1.1.1. 简单的分布式server

目前分布式系统已经很流行了，一些开源框架也被广泛应用，如dubbo、Motan等。对于一个分布式服务，最基本的一项功能就是服务的注册和发现，而利用zk的EPHEMERAL节点则可以很方便的实现该功能。EPHEMERAL节点正如其名，是临时性的，其生命周期是和客户端会话绑定的，当会话连接断开时，节点也会被删除。下边我们就来实现一个简单的分布式server：

#### server：

服务启动时，创建zk连接，并在go_servers节点下创建一个新节点，节点名为"ip:port"，完成服务注册 服务结束时，由于连接断开，创建的节点会被删除，这样client就不会连到该节点

#### client：

先从zk获取go_servers节点下所有子节点，这样就拿到了所有注册的server 从server列表中选中一个节点（这里只是随机选取，实际服务一般会提供多种策略），创建连接进行通信 这里为了演示，我们每次client连接server，获取server发送的时间后就断开。主要代码如下：

server.go

```go
package main

import (
    "fmt"
    "net"
    "os"
    "time"

    "github.com/samuel/go-zookeeper/zk"
)

func main() {
    go starServer("127.0.0.1:8897")
    go starServer("127.0.0.1:8898")
    go starServer("127.0.0.1:8899")

    a := make(chan bool, 1)
    <-a
}

func checkError(err error) {
    if err != nil {
        fmt.Println(err)
    }
}

func starServer(port string) {
    tcpAddr, err := net.ResolveTCPAddr("tcp4", port)
    fmt.Println(tcpAddr)
    checkError(err)

    listener, err := net.ListenTCP("tcp", tcpAddr)
    checkError(err)

    //注册zk节点q
    // 链接zk
    conn, err := GetConnect()
    if err != nil {
        fmt.Printf(" connect zk error: %s ", err)
    }
    defer conn.Close()
    // zk节点注册
    err = RegistServer(conn, port)
    if err != nil {
        fmt.Printf(" regist node error: %s ", err)
    }

    for {
        conn, err := listener.Accept()
        if err != nil {
            fmt.Fprintf(os.Stderr, "Error: %s", err)
            continue
        }
        go handleCient(conn, port)
    }

    fmt.Println("aaaaaa")
}

func handleCient(conn net.Conn, port string) {
    defer conn.Close()

    daytime := time.Now().String()
    conn.Write([]byte(port + ": " + daytime))
}
func GetConnect() (conn *zk.Conn, err error) {
    zkList := []string{"localhost:2181"}
    conn, _, err = zk.Connect(zkList, 10*time.Second)
    if err != nil {
        fmt.Println(err)
    }
    return
}

func RegistServer(conn *zk.Conn, host string) (err error) {
    _, err = conn.Create("/go_servers/"+host, nil, zk.FlagEphemeral, zk.WorldACL(zk.PermAll))
    return
}

func GetServerList(conn *zk.Conn) (list []string, err error) {
    list, _, err = conn.Children("/go_servers")
    return
}
```

### 1.1.2. client.go

```go
package main

import (
    "errors"
    "fmt"
    "io/ioutil"
    "math/rand"
    "net"
    "time"

    "github.com/samuel/go-zookeeper/zk"
)

func checkError(err error) {
    if err != nil {
        fmt.Println(err)
    }
}
func main() {
    for i := 0; i < 100; i++ {
        startClient()

        time.Sleep(1 * time.Second)
    }
}

func startClient() {
    // service := "127.0.0.1:8899"
    //获取地址
    serverHost, err := getServerHost()
    if err != nil {
        fmt.Printf("get server host fail: %s \n", err)
        return
    }

    fmt.Println("connect host: " + serverHost)
    tcpAddr, err := net.ResolveTCPAddr("tcp4", serverHost)
    checkError(err)
    conn, err := net.DialTCP("tcp", nil, tcpAddr)
    checkError(err)
    defer conn.Close()

    _, err = conn.Write([]byte("timestamp"))
    checkError(err)

    result, err := ioutil.ReadAll(conn)
    checkError(err)
    fmt.Println(string(result))

    return
}

func getServerHost() (host string, err error) {
    conn, err := GetConnect()
    if err != nil {
        fmt.Printf(" connect zk error: %s \n ", err)
        return
    }
    defer conn.Close()
    serverList, err := GetServerList(conn)
    if err != nil {
        fmt.Printf(" get server list error: %s \n", err)
        return
    }

    count := len(serverList)
    if count == 0 {
        err = errors.New("server list is empty \n")
        return
    }

    //随机选中一个返回
    r := rand.New(rand.NewSource(time.Now().UnixNano()))
    host = serverList[r.Intn(3)]
    return
}
func GetConnect() (conn *zk.Conn, err error) {
    zkList := []string{"localhost:2181"}
    conn, _, err = zk.Connect(zkList, 10*time.Second)
    if err != nil {
        fmt.Println(err)
    }
    return
}
func GetServerList(conn *zk.Conn) (list []string, err error) {
    list, _, err = conn.Children("/go_servers")
    return
}
```

先启动server，可以看到有三个节点注册到zk：

```
    127.0.0.1:8897
    127.0.0.1:8899
    127.0.0.1:8898
    2018/08/27 14:04:58 Connected to 127.0.0.1:2181
    2018/08/27 14:04:58 Connected to 127.0.0.1:2181
    2018/08/27 14:04:58 Connected to 127.0.0.1:2181
    2018/08/27 14:04:58 Authenticated: id=100619932030205976, timeout=10000
    2018/08/27 14:04:58 Re-submitting `0` credentials after reconnect
    2018/08/27 14:04:58 Authenticated: id=100619932030205977, timeout=10000
    2018/08/27 14:04:58 Re-submitting `0` credentials after reconnect
    2018/08/27 14:04:58 Authenticated: id=100619932030205978, timeout=10000
    2018/08/27 14:04:58 Re-submitting `0` credentials after reconnect
```

启动client，可以看到每次client都会随机连接到一个节点进行通信：

```
    2018/08/27 14:05:21 Connected to 127.0.0.1:2181
    2018/08/27 14:05:21 Authenticated: id=100619932030205979, timeout=10000
    2018/08/27 14:05:21 Re-submitting `0` credentials after reconnect
    2018/08/27 14:05:21 Recv loop terminated: err=EOF
    connect host: 127.0.0.1:8899
    2018/08/27 14:05:21 Send loop terminated: err=<nil>
    read tcp 127.0.0.1:54062->127.0.0.1:8899: read: connection reset by peer
    127.0.0.1:8899: 2018-08-27 14:05:21.291641 +0800 CST m=+22.480149656
    2018/08/27 14:05:22 Connected to [::1]:2181
    2018/08/27 14:05:22 Authenticated: id=100619932030205980, timeout=10000
    2018/08/27 14:05:22 Re-submitting `0` credentials after reconnect
    2018/08/27 14:05:22 Recv loop terminated: err=EOF
    2018/08/27 14:05:22 Send loop terminated: err=<nil>
    connect host: 127.0.0.1:8897
    read tcp 127.0.0.1:54064->127.0.0.1:8897: read: connection reset by peer
    127.0.0.1:8897: 2018-08-27 14:05:22.302322 +0800 CST m=+23.490801385
    2018/08/27 14:05:23 Connected to 127.0.0.1:2181
    2018/08/27 14:05:23 Authenticated: id=100619932030205981, timeout=10000
    2018/08/27 14:05:23 Re-submitting `0` credentials after reconnect
    2018/08/27 14:05:23 Recv loop terminated: err=EOF
    2018/08/27 14:05:23 Send loop terminated: err=<nil>
    connect host: 127.0.0.1:8897
    read tcp 127.0.0.1:54070->127.0.0.1:8897: read: connection reset by peer
    127.0.0.1:8897: 2018-08-27 14:05:23.312873 +0800 CST m=+24.501324228
    2018/08/27 14:05:24 Connected to 127.0.0.1:2181
    2018/08/27 14:05:24 Authenticated: id=100619932030205982, timeout=10000
    2018/08/27 14:05:24 Re-submitting `0` credentials after reconnect
    2018/08/27 14:05:24 Recv loop terminated: err=EOF
    connect host: 127.0.0.1:8899
    2018/08/27 14:05:24 Send loop terminated: err=<nil>
    read tcp 127.0.0.1:54072->127.0.0.1:8899: read: connection reset by peer
    127.0.0.1:8899: 2018-08-27 14:05:24.323668 +0800 CST m=+25.512090155
    2018/08/27 14:05:25 Connected to 127.0.0.1:2181
    2018/08/27 14:05:25 Authenticated: id=100619932030205983, timeout=10000
    2018/08/27 14:05:25 Re-submitting `0` credentials after reconnect
    2018/08/27 14:05:25 Recv loop terminated: err=EOF
    2018/08/27 14:05:25 Send loop terminated: err=<nil>
    connect host: 127.0.0.1:8897
    read tcp 127.0.0.1:54074->127.0.0.1:8897: read: connection reset by peer
    127.0.0.1:8897: 2018-08-27 14:05:25.330257 +0800 CST m=+26.518650566
    2018/08/27 14:05:26 Connected to [::1]:2181
    2018/08/27 14:05:26 Authenticated: id=100619932030205984, timeout=10000
    2018/08/27 14:05:26 Re-submitting `0` credentials after reconnect
    2018/08/27 14:05:26 Recv loop terminated: err=EOF
    2018/08/27 14:05:26 Send loop terminated: err=<nil>
    connect host: 127.0.0.1:8897
    read tcp 127.0.0.1:54080->127.0.0.1:8897: read: connection reset by peer
    127.0.0.1:8897: 2018-08-27 14:05:26.357251 +0800 CST m=+27.545614616
    2018/08/27 14:05:27 Connected to 127.0.0.1:2181
    2018/08/27 14:05:27 Authenticated: id=100619932030205985, timeout=10000
    2018/08/27 14:05:27 Re-submitting `0` credentials after reconnect
    connect host: 127.0.0.1:8899
    2018/08/27 14:05:27 Recv loop terminated: err=EOF
    2018/08/27 14:05:27 Send loop terminated: err=<nil>
    read tcp 127.0.0.1:54082->127.0.0.1:8899: read: connection reset by peer
    127.0.0.1:8899: 2018-08-27 14:05:27.369096 +0800 CST m=+28.557430764
    2018/08/27 14:05:28 Connected to [::1]:2181
    2018/08/27 14:05:28 Authenticated: id=100619932030205986, timeout=10000
    2018/08/27 14:05:28 Re-submitting `0` credentials after reconnect
    2018/08/27 14:05:28 Recv loop terminated: err=EOF
    2018/08/27 14:05:28 Send loop terminated: err=<nil>
    connect host: 127.0.0.1:8898
    read tcp 127.0.0.1:54084->127.0.0.1:8898: read: connection reset by peer
    127.0.0.1:8898: 2018-08-27 14:05:28.380455 +0800 CST m=+29.568760988
    ......
```

至此，我们的分布式server就实现了

## 3.Zookeeper命令使用

### 1.1.1. Zookeeper部署

Zookeeper的部署相对来说还是比较简单，读者可以在网上找到相应的教程。Zookeeper有三种运行形式：集群模式、单机模式、伪集群模式。

以下实验都是在单机模式下进行。

服务端使用

zookeeper下bin目录下常用的脚本解释：

1.zkCleanup 清理Zookeeper历史数据，包括事物日志文件和快照数据文件

2.zkCli Zookeeper的一个简易客户端

3.zkEnv 设置Zookeeper的环境变量

4.zkServer Zookeeper服务器的启动、停止、和重启脚本

1.运行服务

进入bin目录，使用zkServer.sh start启动服务

使用jps命令查看，存在QuorumPeerMain进程，表示Zookeeper已经启动

2.停止服务

在bin目录下，使用zkServer.sh stop停止服务

使用jps命令查看，QuorumPeerMain进程已不存在，表示Zookeeper已经关闭

客户端使用

1.打开客户端

在服务端开启的情况下，运行客户端，使用如下命令：./zkCli.sh

连接服务端成功。若连接不同的主机，可使用如下命令：./zkCli.sh -server ip:port（当然可以使用配置文件）。

可以使用帮助命令help来查看客户端的操作

2.创建节点

使用create命令，可以创建一个Zookeeper节点，如下：

create [-s] [-e] path data acl

其中，-s或-e分别指定节点特性，顺序或临时节点，若不指定，则表示持久节点；acl用来进行权限控制。

① 创建顺序节点

使用 create -s /zk-test 123 命令创建zk-test顺序节点

可以看到创建的zk-test节点后面添加了一串数字以示区别。

② 创建临时节点

使用 create -e /zk-temp 123 命令创建zk-temp临时节点

临时节点在客户端会话结束后，就会自动删除，下面使用quit命令退出客户端

再次使用客户端连接服务端，并使用ls / 命令查看根目录下的节点

可以看到根目录下已经不存在zk-temp临时节点了。

③ 创建永久节点

使用 create /zk-permanent 123 命令创建zk-permanent永久节点

可以看到永久节点不同于顺序节点，不会自动在后面添加一串数字。

3.读取节点

与读取相关的命令有ls 命令和get 命令，ls命令可以列出Zookeeper指定节点下的所有子节点，只能查看指定节点下的第一级的所有子节点；get命令可以获取Zookeeper指定节点的数据内容和属性信息。其用法分别如下

ls path [watch]

get path [watch]

ls2 path [watch]

若获取根节点下面的所有子节点，使用ls / 命令即可

若想获取根节点数据内容和属性信息，使用get / 命令即可

也可以使用ls2 / 命令查看

可以看到其子节点数量为8。

若想获取/zk-permanent的数据内容和属性，可使用如下命令：get /zk-permanent

可以看到其数据内容为123，还有其他的属性，之后会详细介绍。

4.更新节点

使用set命令，可以更新指定节点的数据内容，用法如下

set path data [version]

其中，data就是要更新的新内容，version表示数据版本，如将/zk-permanent节点的数据更新为456，可以使用如下命令：set /zk-permanent 456

现在dataVersion已经变为1了，表示进行了更新。

5.删除节点

使用delete命令可以删除Zookeeper上的指定节点，用法如下

delete path [version]

其中version也是表示数据版本，使用delete /zk-permanent 命令即可删除/zk-permanent节点

可以看到，已经成功删除/zk-permanent节点。值得注意的是，若删除节点存在子节点，那么无法删除该节点，必须先删除子节点，再删除父节点。