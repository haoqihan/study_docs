### goroutine并发

#### goroutine

```go
// go func(){}()
// 用go关键字开启协程,协程是非抢占式多任务处理,有协程主动交出控制权

// 第一种
func main(){
    for i := 0; i < 1000; i++{
        go func(i int){
            for {
                fmt.Println("xxxxx")
            }
        }(i)
    }
    time.Sleep(time.Millsecond)
}

// 第二种
func main(){
    var a [10]int
	for i := 0; i < 10; i++ {
		go func(i int) {
			for {
				a[i]++
				runtime.Gosched()
			}
		}(i)
	}
	time.Sleep(time.Microsecond)
	fmt.Println(a)
}
```

#### go语言调度器

```go
// go func(){}() 
// 用 go 关键字开启协程，协程是非抢占式多任务处理，由协程主动交出控制权
goroutine可能交出控制权的点： 
- I/O操作，select 
- channel 
- 等待锁 
- 函数调用时（有时，不一定） 
- runtime.Gosched()
```

#### channel

> channel其实就是传统语言的阻塞消息队列，可以用来做不同goroutine之间的消息传递

##### 定义

```go

```

#### 更进一步：channel工厂

```go

```

#### channel 方向（只读与只写）

```go

```

##### 缓冲区

> 向管道中写入就必须定义相应的输出，否则会报错  有缓冲区与无缓冲区的区别是 一个是同步的 一个是非同步的，即阻塞型队列和非阻塞队列 详解：<https://blog.csdn.net/samete/article/details/52751227> 

```go

```

##### 关闭管道

```go

```

#### 用channel等待任务结束

上面的例子使用 `time.Sleep(time.Microsecond)`来等待任务结束，不精确且耗时

```go

```

#### 用 sync.WaitGroup 等待任务结束

```go
package main
import (
    "fmt"
    "sync"
)
type worker struct {
    in chan int
    wg *sync.WaitGroup              // *
}
func createWorker(wg *sync.WaitGroup) worker{
    worker := worker{
        in:make(chan int),
        wg:wg,              
    }
    doWorker(worker);
    return worker
}
func doWorker(w worker)  {
    go func(w worker) {
        for {
            fmt.Printf("%c \n", <-w.in)
            w.wg.Done()             // 发送任务结束的信号
        }
    }(w)
}
func main() {
    var wg sync.WaitGroup           // 定义WaitGroup
    var arr [10] worker
    for i:=0; i<10; i++ {
        arr[i] = createWorker(&wg)  //按址传递，用一个引用来开始和结束
    }
    for i:=0; i<10; i++ {
        wg.Add(1)                   // 开始一个任务前，计时器加一（一定要在开始前加）
        arr[i].in <- 'a'+i
    }
    for i:=0; i<10; i++ {
        wg.Add(1)
        arr[i].in <- 'A'+i
    }
    wg.Wait()                       // 阻塞等待所有任务 done
}
```

#### select

> - 有多个 case 语句，只要有一个 case 处于非阻塞可执行状态，就执行，否则一直阻塞
> - 如果有多个case都可以运行，select会随机公平地选出一个执行，其他不会执行

##### 用法

```go

```

```go

```

##### 定时器

> - time.After() 设置一个定时器，返回一个 channel，到一段时间后，向channel发送一条当前时间
> - time.Tick() 返回一个 channel，每过一段时间向channel发送一条当前时间

```go
func main() {
    c1,c2 := create(1),create(2)
    tm := time.After(2*time.Second)     // 定时器，2秒后触发
    tm2 := time.Tick(1*time.Second)     // 每1秒触发一次
    for {
        select {
        case n1 := <-c1:
            fmt.Printf("%c \n",n1)
        case n2 := <-c2:
            fmt.Printf("%c \n",n2)
        case t := <- tm2:
            fmt.Println("------- ",t," -----------")
        case <- tm:
            fmt.Println("bye")
            return 
        }
    }
}
```

