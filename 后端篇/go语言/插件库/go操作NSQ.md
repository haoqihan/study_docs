## 1. 安装

Mac安装nsq：

按照安装文档中的说明进行操作。

打开终端：

执行：$ brew install nsq

若：-bash: brew: command not found

执行：$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

然后执行：brew install nsq

在一个shell中，开始nsqlookupd：

$ nsqlookupd

在另一个shell中，开始nsqd：

$ nsqd --lookupd-tcp-address=127.0.0.1:4160

在另一个shell中，开始nsqadmin：

$ nsqadmin --lookupd-http-address=127.0.0.1:4161

发布初始消息（也在集群中创建主题）：

$ curl -d 'hello world 1' 'http://127.0.0.1:4151/pub?topic=test'

最后，在另一个shell中，开始nsq_to_file：

$ nsq_to_file --topic=test --output-dir=/tmp --lookupd-http-address=127.0.0.1:4161

发布更多消息nsqd：

$ curl -d 'hello world 2' 'http://127.0.0.1:4151/pub?topic=test'

$ curl -d 'hello world 3' 'http://127.0.0.1:4151/pub?topic=test'

验证事物按预期工作，在Web浏览器中打开http://127.0.0.1:4171/ 以查看nsqadminUI并查看统计信息。另外，检查`test.*.log`写入的日志文件（）的内容/tmp。

这里的重要教训是nsq_to_file（客户端）未明确告知test 主题产生的位置，它从中检索此信息，nsqlookupd并且尽管有连接的时间，但不会丢失任何消息。

## 生产者

运行Nsq服务集群

首先启动nsqlookud，在一个shell中，开始nsqlookupd：

$ nsqlookupd

在另一个shell中，开始nsqd：

$ nsqd --lookupd-tcp-address=127.0.0.1:4160

在另一个shell中，开始nsqadmin：

$ nsqadmin --lookupd-http-address=127.0.0.1:4161

发布初始消息（也在集群中创建主题）：

$ curl -d 'hello world 1' 'http://127.0.0.1:4151/pub?topic=test'

最后，在另一个shell中，开始nsq_to_file：

$ nsq_to_file --topic=test --output-dir=/tmp --lookupd-http-address=127.0.0.1:4161

验证事物按预期工作，在Web浏览器中打开http://127.0.0.1:4171/ 以查看nsqadminUI并查看统计信息。另外，检查`test.*.log`写入的日志文件（）的内容/tmp。

链接nsq 并创建生产者：

```go
package main

import (
    "fmt"

    nsq "github.com/nsqio/go-nsq"
)

func main() {
    // 定义nsq生产者
    var producer *nsq.Producer
    // 初始化生产者
    // producer, err := nsq.NewProducer("地址:端口", nsq.*Config )
    producer, err := nsq.NewProducer("127.0.0.1:4150", nsq.NewConfig())
    if err != nil {
        panic(err)
    }

    err = producer.Ping()
    if nil != err {
        // 关闭生产者
        producer.Stop()
        producer = nil
    }

    fmt.Println("ping nsq success")
}
```

生产者创建topic并写入nsq：

```go
package main

import (
    "fmt"

    nsq "github.com/nsqio/go-nsq"
)

func main() {
    // 定义nsq生产者
    var producer *nsq.Producer
    // 初始化生产者
    // producer, err := nsq.NewProducer("地址:端口", nsq.*Config )
    producer, err := nsq.NewProducer("127.0.0.1:4150", nsq.NewConfig())
    if err != nil {
        panic(err)
    }

    err = producer.Ping()
    if nil != err {
        // 关闭生产者
        producer.Stop()
        producer = nil
    }

    // 生产者写入nsq,10条消息，topic = "test"
    topic := "test"
    for i := 0; i < 10; i++ {
        message := fmt.Sprintf("message:%d", i)
        if producer != nil && message != "" { //不能发布空串，否则会导致error
            err = producer.Publish(topic, []byte(message)) // 发布消息
            if err != nil {
                fmt.Printf("producer.Publish,err : %v", err)
            }
            fmt.Println(message)
        }
    }

    fmt.Println("producer.Publish success")

}
```

## 消费者

```go
//Nsq接收测试
package main

import (
    "fmt"
    "time"

    "github.com/nsqio/go-nsq"
)

// 消费者
type ConsumerT struct{}

// 主函数
func main() {
    InitConsumer("test", "test-channel", "127.0.0.1:4161")
    for {
        time.Sleep(time.Second * 10)
    }
}

//处理消息
func (*ConsumerT) HandleMessage(msg *nsq.Message) error {
    fmt.Println("receive", msg.NSQDAddress, "message:", string(msg.Body))
    return nil
}

//初始化消费者
func InitConsumer(topic string, channel string, address string) {
    cfg := nsq.NewConfig()
    cfg.LookupdPollInterval = time.Second          //设置重连时间
    c, err := nsq.NewConsumer(topic, channel, cfg) // 新建一个消费者
    if err != nil {
        panic(err)
    }
    c.SetLogger(nil, 0)        //屏蔽系统日志
    c.AddHandler(&ConsumerT{}) // 添加消费者接口

    //建立NSQLookupd连接
    if err := c.ConnectToNSQLookupd(address); err != nil {
        panic(err)
    }

    //建立多个nsqd连接
    // if err := c.ConnectToNSQDs([]string{"127.0.0.1:4150", "127.0.0.1:4152"}); err != nil {
    //  panic(err)
    // }

    // 建立一个nsqd连接
    // if err := c.ConnectToNSQD("127.0.0.1:4150"); err != nil {
    //  panic(err)
    // }
}
```





