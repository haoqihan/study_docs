#### 变量定义

```go
变量需要先声明,再赋值

// 声明:
var a int		// 声明int类型的变量
var b [10]int	// 声明int类型的数组
var c []int		// 声明int类型的切片
var d *int		// 声明int类型的指针

// 赋值
a = 10
b[0] = 10

// 同时声明与赋值
var a = 10
a := 10
a,b,c,d := 1,2,true,"xxx"
```

#### 常量定义

```go
// const是用来定义常量的
const filename = "abc.txt"
const a,b = 3,4		

const (
	python = 1
    go = 2
    java = 3
)

const(
	python = iota  //自增,初始值为0
    go
    java
)
```

#### 条件语句和循环

##### if条件语句

```go
if a == 100{
    return "满分"
}else if a >=60{
    return "及格"
}else{
    return "不及格"
}

if a,b := 1,2; a + b == 3{
    fmt.Println(a,b)
}
fmt.Println(a,b)  // 此处会报错,a和b是在if里定义的,作用域仅限于if 中使用
```

##### switch条件语句

```go
// go中的switch会自动break,除非使用fallthrough
k:= 1
switch k {
	case 1:
		fmt.Println(1)
	case 2:
		fmt.Println(2)
	case 3:
		fmt.Println(3)
	case 4:
		fmt.Println(4)
	case 5:
		fmt.Println(5)
	default:
		fmt.Println(6)
}
```

##### for循环

```go
// 赋值语句；判断语句；递增语句
for i:=100; i>0; i--{
    fmt.Println(i)
}
// 无赋值
func test(n int){
    for ; n>0 ; n/=2 {
        fmt.Println(n);
    }
}
// 仅赋值
scanner := bufio.NewScanner(file)
for scanner.Scan(){
    fmt.Println(scanner.Text);
}
// 死循环
for{
    fmt.Println(1);
}
```

#### 函数

```go
// 格式
func eval(a,b int, s string) int{ ... }

// 当有返回多个值时
func test1(a,b int) (int, int){
    return a+b, a*b
}

// 为多个返回值起名字（仅用于简单函数）
func test2(a,b int) (q, r int){     
    q = a+b
    r = a*b
    return                  // 自动对号入座返回相应变量
}
q, r := test2(1,2)

// 输出错误
func test(a,b int)(int, error)  {
    if a+b>100{
        return a+b, fmt.Errorf("%s","error!")
    }else{
        return a+b, nil
    }
}
```

#### 指针

```go
// go语言的参数传递是值传递
func main(){
    a,b := 1,2
    swap_text(&a,&b)
}

func swap_text(a,b *int){
    fmt.Println(a,*b)		// 0xc420014050  2
}

// 理解： a,b *int 存的是 int 类型值的地址，当对指针类型的变量 *a 时，就是取出地址对应的值
```

### 内建容器

#### 数组

##### 定义数组

```go
var arr [3]int                // 会初始化为 [0,0,0]
arr := [3]int{1,2,3}		 // [1,2,3]  只能存放三个
arr := [...]{1,2,3,4,5}		 // [1,2,3,4,5] 不用在意多少
arr := [2][4]int            // 2行4列
```

##### 遍历数组

```go
arr := [3]int{1, 2, 3}
for k, v := range arr {
	fmt.Println(k, v)
}
```

##### 函数传递(按值传递)

```go
// 注意,[5]int 与 [10]int是不同类型的
// go语言一般不直接使用数组,而是使用切片
func printArr(arr [5]int)  {
    for k,v:=range (arr){
        fmt.Println(k,v)
    }
}
func main() {
    arr :=[5] int {6,7,8,9,10}
    printArr(arr)
}
```

#### 切片

##### 概念

```go
// 顾首不顾尾
arr := [...]{0,1,2,3,4,5,6,7}
arr1 := arr[1:2]	// 1
arr2 := arr[:5]		// 0,1,2,3,4
arr3 := arr[2:]		// 2,3,4,5,6,7
arr4 := arr[:]		// 0,1,2,3,4,5,6,7
```

##### 视图

```go
// 切片是数组的 "视图" , 即引用
func updateArr(arr []int)  {    // []中不写具体大小，表示是切片，引用传递
    arr[0] = 100
}
func main() {
    arr :=[5] int {0,1,2,3,4}
    arr1 := arr[1:3]
    fmt.Println(arr,arr1)       // [0 1 2 3 4] [1 2]
    updateArr(arr1)
    fmt.Println(arr,arr1)       // [0 100 2 3 4] [100 2]
}
```

##### 切片的扩展(cap)

![img](https://wx4.sinaimg.cn/mw690/0067sOJnly1ftabutoetgj31km0muaic.jpg) 

```go
// 切片的切片依然是对一个数组的引用
func updateArr(arr []int)  {
    arr[0] = 100
}
func main() {
    arr :=[5] int {0,1,2,3,4}
    arr1 := arr[1:3]
    arr2 := arr1[0:3]
    fmt.Println(arr,arr1,arr2)  // [0 1 2 3 4] [1 2] [1 2 3]
    updateArr(arr1)
    fmt.Println(arr,arr1,arr2)  // [0 100 2 3 4] [100 2] [100 2 3]
}
// 查看扩展
arr :=[5] int {0,1,2,3,4}
arr1 := arr[1:3]
arr2 := arr1[0:3]
fmt.Println(arr1,len(arr1),cap(arr1))   // [1 2] 2 4
fmt.Println(arr2,len(arr2),cap(arr2))   // [1 2 3] 3 4
```

##### 直接创建切片

```go
a := []int{1,2,3}
var a []int				//会初始化为nil
a := make([]int,16,32)	 // make(切片类型,切片长度,切片cap长度)
```

##### 添加元素

```go
// 若添加元素个数不超过cap值,则在原数组修改
arr :=[5] int {0,1,2,3,4}
arr1 := arr[1:3]
arr2 := append(arr1, 10, 11)
fmt.Println(arr1,arr2,arr)      // [1 2] [1 2 10 11] [0 1 2 10 11]

//若添加元素个数超过cap值,则开辟新的数组,拷贝并添加
arr :=[5] int {0,1,2,3,4}
arr1 := arr[1:3]
arr2 := append(arr1, 10, 11, 12)
fmt.Println(arr1,arr2,arr)      // [1 2] [1 2 10 11 12] [0 1 2 3 4]

func main() {
    var s []int
    for i:=0; i<10; i++ {
        s = append(s,i)
        fmt.Println(s, cap(s))
    }
}
// 结果：（当cap超出，就会重新分配cap值更大的新数组）
[0] 1
[0 1] 2
[0 1 2] 4
[0 1 2 3] 4
[0 1 2 3 4] 8
[0 1 2 3 4 5] 8
[0 1 2 3 4 5 6] 8
[0 1 2 3 4 5 6 7] 8
[0 1 2 3 4 5 6 7 8] 16
[0 1 2 3 4 5 6 7 8 9] 16
```

##### copy(拷贝)

```go
s1 := []int{0,1,2,3}
s2 := make([]int,6)
copy(s2,s1)			  // 把s1中的内容拷贝到s2中
fmt.Println(s1,s2)      // [0 1 2 3] [0 1 2 3 0 0]
```

#### map

##### 定义

```go
m := map[string]int{}		// nil
var m map[string]string		// nil
m := make(map[string]string) // empty map

m2 := map[string]string{
    "name":"xxx",
    "age":"111"
}
fmt.Println(m2)                     // map[name:xxx age:111]
```

##### 遍历

```go
// map是无序的hash map,所以遍历时每一次输出的顺序都不一样
m := map[string]string{
        "name":"xxx",
    	"age":"111"
}
for k,v := range m{
     fmt.Println(k,v)
}
```

##### 取值

```go
m := map[string]string{
        "name":"xxx",
    	"age":"111"
}
name := m["name"]		
mt.Println(name)           //  "xxx"

// 获取一个不存在的值
sex := m["sex"]
mt.Println(sex)				// 返回一个空值

// 判断key是否存在
value,ok := m["aaa"]
mt.Println(value,ok)		// 返回一个空和false

// 标准用法
if v,ok := m["age"]; ok{
    fmt.Println(v)
}else{
    fmt.Println("key not exist")
}
```

##### 删除(delete)

```go
delete(m,"age") 	// 删除m中的age
```

### 面对对象

```go
// go语言的面对对象仅支持封装,不支持继承和多态
```

#### 结构体

##### 定义

```go
// 定义一个结构体

type treeNode struct{
    value int
    left,right *treeNode
}

func main(){
    root := treeNode{1,nil,nil}
    node1 := treeNode{value:3}
    root.left = &node1
    root.left.right = new(treeNode)         // 内建函数初始化node  new(treeNode) = &{0 <nil> <nil>}
    nodes := []treeNode{
        {1,nil,nil},
        {2,&root,&node1},
    }
    fmt.Println(nodes[1].left.left.value)       // 3
}
```

##### 自定义工厂函数

```go
// 由于没有构造函数,所以可以用工厂函数替代
func createNode(value int) *treeNode{
    return &treeNode{value:value}
}

func main(){
    node := createNode(10)
    fmt.Println(node)			// &{10,<nil>,<nil>}
}
```

##### 结构体方法

```go
// 结构体方法并不是写在结构体中,而是像函数一样写在外面,他实际上就是定义了[接收对象]的函数
// 由于本质依然是函数,所以按值传递,若要改变对象,需要用指针传递
type treeNode struct{
    value int
    left,right *treeNode
}

// func(接收对象) 方法名(参数) 返回值{}
func (node treeNode) get() int{
    return node.value
}

func (node *treeNode) set(value int){
    node.value = value
}

func main(){
    root := treeNode{2,nil,nil}
    res := root.get()
    root.set(10)
}
```

#### 封装

```go
// 名字一般用CamelCase(驼峰体)
// 首字母大写是public(公有方法,可以调用)方法
// 首字母小写是private(私有方法)方法
```

##### 包

```go
// 每个目录只有一个包(package)
// main包 包含程序入口
// 为某结构体定义方法必须放在同一包内,但可以放不同文件
```

##### 继承

```
go语言没有继承,如何扩展系统类型或者自定义类型呢?
	1.定义别名
	2.使用组合
```

##### 获取第三方库

```go
// go get xxx 从第官方下载第三方库,需要翻墙
// gopm 可以获取国内镜像  (需要在github下载gopm)
```

#### 接口

##### 定义

```go
type xxx interface{
    FuncName() string		// 定义接口方法与返回类型
}
```

##### 实现

```go
// 结构体不需要显示"实现" 接口,只要定义好方法即可
// interface/interface.go
package file
type File interface {
    Read() string 
    Write(str string)
}
// interface/implament.go
// File1 结构体实现了接口规定的方法
package file
type File1 struct {
    Content string
}
func (file File1)  Read() string{
    return file.Content
}
func (file *File1) Write(str string) {
    file.Content = str
}
// interface/entry/main.go
package main
import (
    "../../interface"
    "fmt"
)
func get(f file.File) string {    // 只有实现了 File 接口的结构体实例才能调用此方法
    res := f.Read()
    return res
}
func main() {
    f := file.File1{}
    f.Write("www")
    fmt.Println(get(f))
}
```

##### 类型

```go
// 查看类型 i.(type)
var i AnimalInterface       // 定义变量 i 是动物接口类型
i = Cat{"cat"}              // 假设 Cat 结构体实现了 AnimalInterface 接口
i.(type)                    // Cat
i = Dog{"dog"}              // 假设 Dog 结构体实现了 AnimalInterface 接口
i.(type)                    // Dog
```

##### 约束接口类型: i.(xxx)

```go
var i AnimalInterface       // 定义变量 i 是动物接口类型
i = Cat{"cat"}              // 假设 Cat 结构体实现了 AnimalInterface 接口
cat := i.(Cat)              // 如果 i 是Cat类型的，则拷贝赋值给 cat变量，否则报错）
if dog, ok := i.(Dog); ok{
    // ok
}else{
    // i isn't dog
}
```

##### 泛型:interface{}

```go
type Queue []int            // 定义了一个 int 类型的切片
func (q *Queue) Push(v int){
    *q = append(*q, v)
}
func (q *Queue) Pop() int{
    head := (*q)[0]
    *q = (*q)[1:]
    return head
}
// 将上面的切片改成可以接受任意类型：
type Queue []interface{}            // 定义了一个 int 类型的切片
func (q *Queue) Push(v interface{}){
    *q = append(*q, v)
}
func (q *Queue) Pop() interface{}{
    head := (*q)[0]
    *q = (*q)[1:]
    return head
}
// 强制类型转换：
head.(int)
```

##### 组合

```go
type Cat interface{
    cat()
}
type Dog interface{
    dog()
}
type Animal interface{          // 要实例既实现 Cat 又实现 Dog
    Cat
    Dog
}
func get(i Animal){
    i.cat()
    i.dog()
}
```

##### 常用系统接口

```go
// 1. 类似 toString() 的信息打印接口
type Stringer interface{
    String() string
}
// 2. Reader
type Reader interface{
    Read(p []byte) (n int, err error)
}
// 3. Writer
type Writer interface{
    Write(p []byte) (n int, err error)
}
```

### 函数式编程

#### 闭包

```go
func add() func(int) int {
    sum := 0                        // 此处的 sum 为自由变量
    return func(v int) int {
        sum += v                    // 指向外层sum
        return sum  
    }
}
func main(){
    add := add()
    for i:=0; i<10; i++ {
        fmt.Printf(add(i))          // 从 0 到 10 的累加
    }
}
```

#### 生成器

```go
// 一个斐波那契数列的生成器
func fib() func() int{
    a, b := 0, 1
    return func() int{
        a, b = b, a+b
        return a
    }
}
func main(){
    f = fib()
    f()             // 1
    f()             // 1
    f()             // 2
    f()             // 3
}
```

#### 函数接口

```go
package main
import (
    "io"
    "bufio"
    "fmt"
    "strings"
)
type funcType func() int
func fib() funcType{
    a, b := 0, 1
    return func() int{
        a, b = b, a+b
        return a
    }
}
func (f funcType) Read(p []byte) (n int, err error)  {
    next := f()
    if next > 1000 {
        return 0, io.EOF
    }
    s := fmt.Sprintf("%d ", next)
    return strings.NewReader(s).Read(p)
}
func scan(read io.Reader)  {
    scanner := bufio.NewScanner(read)
    for scanner.Scan() {
        text := scanner.Text()
        fmt.Printf(text)
    }
}
func main() {
    f := fib()
    scan(f)
}
```

### 错误处理与资源管理

#### defer

```go
func writeFile(filename string)  {
    file, err := os.Create(filename)
    if err!=nil {
        panic("创建文件失败！") // 打印错误信息
    }
    defer file.Close()          // 函数执行完毕前。关闭文件句柄
    writer := bufio.NewWriter(file)
    defer writer.Flush()        // 函数执行完毕前，将缓冲区中的内容刷新到文件中去
    for i:=0; i<100; i++ {
        fmt.Fprintln(writer,i)  // 写入缓冲区
    }
}
func main() {
    writeFile("1.txt")
}
```

#### panic与recover

```go
panic:
  1.停止当前函数执行
  2.停止之前,执行每层defer
  3.如果没有recover 程序直接退出

recover:
  1.近在defer中调用
  2.可以获取 panic 的值
  3.如果无法处理,可重新 panic
```

```go
// 例一：捕获 panic
func dopanic(){
    defer func() {
        err := recover()
        fmt.Println(err)    // error!!
    }()
    panic("error!!")
}
func main() {
    dopanic()
}
// 例二：捕获其他异常
func dopanic(){
    defer func() {
        err := recover()
        fmt.Println(err)    // runtime error: integer divide by zero
    }()
    a := 0
    b := 1/a
    fmt.Println(b)
}
func main() {
    dopanic()
}
// 例三：无异常处理
func dopanic(){
    defer func() {
        err := recover()
        if err, ok := err.(error); ok{
            fmt.Println(err)
        }else{
            fmt.Println("no error!")
        }
    }()
    a := 0
    fmt.Println(a)
}
func main() {
    dopanic()
}
```

###  goroutine并发

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

#### 标准库的使用

##### bufio库

##### encodeing/json库

##### time 库

##### log库

##### regexp库

##### strings/math/rand库

