## fmt

fmt包实现了类似C语言printf和scanf的格式化I/O。主要分为向外输出内容和获取输入内容两大部分。

### 向外输出

标准库fmt提供了以下几种输出相关函数。

#### Print

Print系列函数会将内容输出到系统的标准输出，区别在于Print函数直接输出内容，Printf函数支持格式化输出字符串，Println函数会在输出内容的结尾添加一个换行符。 

```go
// Print 将参数列表 a 中的各个参数转换为字符串并写入到标准输出中。
// 非字符串参数之间会添加空格，返回写入的字节数。
func Print(a ...interface{}) (n int, err error)

// Println 功能类似 Print，只不过最后会添加一个换行符。
// 所有参数之间会添加空格，返回写入的字节数。
func Println(a ...interface{}) (n int, err error)

// Printf 将参数列表 a 填写到格式字符串 format 的占位符中。
// 填写后的结果写入到标准输出中，返回写入的字节数。
func Printf(format string, a ...interface{}) (n int, err error)
```

例子：

```go
func main() {
    fmt.Print("在终端显示该信息，但是没有换行")
    name := "你的名字"
    fmt.Printf("我是：%s\n", name)
    fmt.Println("在终端打印单独一行显示，这个是换行的")
}
```

执行上面的代码输出：

```
    在终端显示该信息，但是没有换行我是：你的名字
    在终端打印单独一行显示，这个是换行的
```

#### Fprint

Fprint系列函数会将内容输出到一个io.Writer接口类型的变量w中，我们通常用这个函数往文件中写入内容。

```go
// 功能同上面三个函数，只不过将转换结果写入到 w 中。
func Fprint(w io.Writer, a ...interface{}) (n int, err error)
func Fprintln(w io.Writer, a ...interface{}) (n int, err error)
func Fprintf(w io.Writer, format string, a ...interface{}) (n int, err error)
```

举个例子：

```go
// 向标准输出写入内容
fmt.Fprintln(os.Stdout, "向标准输出写入内容")
fileObj, err := os.OpenFile("./xx.txt", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644)
if err != nil {
    fmt.Println("打开文件出错，err:", err)
    return
}
name := "枯藤"
// 向打开的文件句柄中写入内容
fmt.Fprintf(fileObj, "往文件中写如信息：%s", name)
```

注意，只要满足io.Writer接口的类型都支持写入。

####  Sprint

Sprint系列函数会把传入的数据生成并返回一个字符串。

```go
// 功能同上面三个函数，只不过将转换结果以字符串形式返回。
func Sprint(a ...interface{}) string
func Sprintln(a ...interface{}) string
func Sprintf(format string, a ...interface{}) string
```

简单的示例代码如下：

```go
s1 := fmt.Sprint("枯藤")
name := "枯藤"
age := 18
s2 := fmt.Sprintf("name:%s,age:%d", name, age)
s3 := fmt.Sprintln("枯藤")
fmt.Println(s1, s2, s3)
```

#### Errorf

Errorf函数根据format参数生成格式化字符串并返回一个包含该字符串的错误。

```go
func Errorf(format string, a ...interface{}) error
```

通常使用这种方式来自定义错误类型，例如：

```go
err := fmt.Errorf("这是一个错误")
```



### 格式化占位符

`*printf`系列函数都支持format格式化参数，在这里我们按照占位符将被替换的变量类型划分，方便查询和记忆。

基础变量

```go
type Website struct {
    Name string
}

// 定义结构体变量
var site = Website{Name:"studygolang"}

```

#### 普通占位符

| 占位符 | 说明                                                         | 举例                                                  | 输出                               |
| ------ | ------------------------------------------------------------ | ----------------------------------------------------- | ---------------------------------- |
| `%v`   | 相应值的默认格式<br>在打印结构体时，“加号”标记（%+v）会添加字段名 | `fmt.Printf("%v", site)`<br>`fmt.Printf("%+v", site)` | `{studygolang}{Name:studygolang}`  |
| `%#v`  | 相应值的Go语法表示                                           | `fmt.Printf("%#v", site)`                             | `main.Website{Name:"studygolang"}` |
| `%T`   | 相应值的类型的Go语法表示                                     | `fmt.Printf("%T", site)`                              | `main.Website`                     |
| `%%`   | `字面上的百分号，并非值的占位符`                             | `Printf("%%")`                                        | `%`                                |

#### 布尔值占位符

| 占位符 | 说明              | 举例                 | 输出 |
| ------ | ----------------- | -------------------- | ---- |
| `%t`   | 单词true 或 false | `Printf("%t", true)` | true |

 **整数占位符** 

| 占位符 | 说明                                         | 举例                       | 结果     |
| ------ | -------------------------------------------- | -------------------------- | -------- |
| `%b`   | `二进制表示`                                 | `fmt.Printf("%b", 5)`      | 101      |
| `%c`   | 相应Unicode码点所表示的字符                  | `fmt.Printf("%c", 0x4E2D)` | 中       |
| `%d`   | 十进制表示                                   | `Printf("%d", 0x12)`       | 18       |
| `%o`   | 八进制表示                                   | `Printf("%d", 10)`         | 12       |
| `%q`   | `单引号围绕的字符字面值，由Go语法安全地转义` | `Printf("%q", 0x4E2D)`     | '中'     |
| `%x`   | 十六进制表示，字母形式为小写 a-f             | `Printf("%x", 13)`         | d        |
| `%X`   | 十六进制表示，字母形式为大写 A-F             | `Printf("%x", 13)`         | D        |
| `%U`   | `Unicode格式：U+1234，等同于 "U+%04X"`       | `Printf("%U", 0x4E2D)`     | `U+4E2D` |

#### 浮点数和复数的组成部分

| 占位符 | 说明                                                         | 举例                     | 输出           |
| ------ | ------------------------------------------------------------ | ------------------------ | -------------- |
| `%b`   | `无小数部分的，指数为二的幂的科学计数法，与 strconv.FormatFloat` |                          |                |
| `%e`   | `科学计数法，例如 -1234.456e+78 `                            | `Printf("%e", 10.2)`     | `1.020000e+01` |
| `%E`   | `科学计数法，例如 -1234.456E+78`                             | `Printf("%E", 10.2)`     | `1.020000E+01` |
| `%f`   | `有小数点而无指数，例如 123.456`                             | `Printf("%f", 10.2)`     | `10.200000`    |
| `%g`   | `根据情况选择 %e 或 %f 以产生更紧凑的（无末尾的0）输出`      | `Printf("%g", 10.20)`    | `10.2`         |
| `%G`   | `根据情况选择 %E 或 %f 以产生更紧凑的（无末尾的0）输出`      | `Printf("%G", 10.20+2i)` | `(10.2+2i)`    |

#### 字符串和字节切片

| 占位符 | 说明                                   | 举例                            | 说明           |
| ------ | -------------------------------------- | ------------------------------- | -------------- |
| `%s`   | 输出字符串表示（string类型或[]byte)    | `Printf("%s", []byte("博客")) ` | 博客           |
| `%q`   | 双引号围绕的字符串，由Go语法安全地转义 | `Printf("%q", "Go语言中文网")`  | "Go语言中文网" |
| `%x`   | 十六进制，小写字母，每字节两个字符     | `Printf("%x", "golang")`        | `676f6c616e67` |
| `%X`   | 十六进制，大写字母，每字节两个字符     | `Printf("%X", "golang")`        | `676F6C616E67` |

#### 指针

| 占位符 | 说明                     | 举例                  | 说明       |
| ------ | ------------------------ | --------------------- | ---------- |
| `%p`   | 十六进制表示，前缀 `0x ` | `Printf("%p", &site)` | `0x4f57f0` |

#### 宽度标识符

宽度通过一个紧跟在百分号后面的十进制数指定，如果未指定宽度，则表示值时除必需之外不作填充。精度通过（可选的）宽度后跟点号后跟的十进制数指定。如果未指定精度，会使用默认精度；如果点号后没有跟数字，表示精度为0。举例如下

| 占位符 | 说明               |
| ------ | ------------------ |
| %f     | 默认宽度，默认精度 |
| %9f    | 宽度9，默认精度    |
| %.2f   | 默认宽度，精度2    |
| %9.2f  | 宽度9，精度2       |
| %9.f   | 宽度9，精度0       |

示例代码如下：

```go
n := 88.88
fmt.Printf("%f\n", n)
fmt.Printf("%9f\n", n)
fmt.Printf("%.2f\n", n)
fmt.Printf("%9.2f\n", n)
fmt.Printf("%9.f\n", n)
```

输出结果如下：

```
    88.880000
    88.880000
    88.88
        88.88
           89
```

#### 其他falg

| 占位符 | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| ’+’    | 总是输出数值的正负号；对%q（%+q）会生成全部是ASCII字符的输出（通过转义）； |
| ’ ‘    | 对数值，正数前加空格而负数前加负号；对字符串采用%x或%X时（% x或% X）会给各打印的字节之间加空格 |
| ’-’    | 在输出右边填充空白而不是默认的左边（即从默认的右对齐切换为左对齐）； |
| ’#’    | 八进制数前加0（%#o），十六进制数前加0x（%#x）或0X（%#X），指针去掉前面的0x（%#p）对%q（%#q），对%U（%#U）会输出空格和单引号括起来的go字面值； |
| ‘0’    | 使用0而不是空格填充，对于数值类型会把填充的0放在正负号后面； |

举个例子：

```go
s := "枯藤"
fmt.Printf("%s\n", s)
fmt.Printf("%5s\n", s)
fmt.Printf("%-5s\n", s)
fmt.Printf("%5.7s\n", s)
fmt.Printf("%-5.7s\n", s)
fmt.Printf("%5.2s\n", s)
fmt.Printf("%05s\n", s)
```

输出结果如下：

```
    枯藤
       枯藤
    枯藤
       枯藤
    枯藤
       枯藤
    000枯藤
```

###  获取输入

 Go语言fmt包下有fmt.Scan、fmt.Scanf、fmt.Scanln三个函数，可以在程序运行过程中从标准输入获取用户的输入。 

#### fmt.Scan

函数定签名如下：

```go
func Scan(a ...interface{}) (n int, err error)
```

- Scan从标准输入扫描文本，读取由空白符分隔的值保存到传递给本函数的参数中，换行符视为空白符。
- 本函数返回成功扫描的数据个数和遇到的任何错误。如果读取的数据个数比提供的参数少，会返回一个错误报告原因。

具体代码示例如下：

```go
func main() {
    var (
        name    string
        age     int
        married bool
    )
    fmt.Scan(&name, &age, &married)
    fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
}
```

将上面的代码编译后在终端执行，在终端依次输入枯藤、18和false使用空格分隔。

```
    $ ./scan_demo 
    枯藤 18 false
    扫描结果 name:枯藤 age:18 married:false
```

fmt.Scan从标准输入中扫描用户输入的数据，将以空白符分隔的数据分别存入指定的参数。

#### fmt.Scanf

函数签名如下：

```go
func Scanf(format string, a ...interface{}) (n int, err error)
```

- Scanf从标准输入扫描文本，根据format参数指定的格式去读取由空白符分隔的值保存到传递给本函数的参数中。
- 本函数返回成功扫描的数据个数和遇到的任何错误。

代码示例如下：

```go
func main() {
    var (
        name    string
        age     int
        married bool
    )
    fmt.Scanf("1:%s 2:%d 3:%t", &name, &age, &married)
    fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
}
```

将上面的代码编译后在终端执行，在终端按照指定的格式依次输入枯藤、18和false。

```
    $ ./scan_demo 
    1:枯藤 2:18 3:false
    扫描结果 name:枯藤 age:18 married:false
```

fmt.Scanf不同于fmt.Scan简单的以空格作为输入数据的分隔符，fmt.Scanf为输入数据指定了具体的输入内容格式，只有按照格式输入数据才会被扫描并存入对应变量。

例如，我们还是按照上个示例中以空格分隔的方式输入，fmt.Scanf就不能正确扫描到输入的数据。

```
    $ ./scan_demo 
    枯藤 18 false
    扫描结果 name: age:0 married:false
```

#### fmt.Scanln

函数签名如下：

```go
func Scanln(a ...interface{}) (n int, err error)
```

- Scanln类似Scan，它在遇到换行时才停止扫描。最后一个数据后面必须有换行或者到达结束位置。
- 本函数返回成功扫描的数据个数和遇到的任何错误。

具体代码示例如下：

```go
    func main() {
        var (
            name    string
            age     int
            married bool
        )
        fmt.Scanln(&name, &age, &married)
        fmt.Printf("扫描结果 name:%s age:%d married:%t \n", name, age, married)
    }
```

将上面的代码编译后在终端执行，在终端依次输入枯藤、18和false使用空格分隔。

```
    $ ./scan_demo 
    枯藤 18 false
    扫描结果 name:枯藤 age:18 married:false
```

fmt.Scanln遇到回车就结束扫描了，这个比较常用。

#### bufio.NewReader

有时候我们想完整获取输入的内容，而输入的内容可能包含空格，这种情况下可以使用bufio包来实现。示例代码如下：

```go
func bufioDemo() {
    reader := bufio.NewReader(os.Stdin) // 从标准输入生成读对象
    fmt.Print("请输入内容：")
    text, _ := reader.ReadString('\n') // 读到换行
    text = strings.TrimSpace(text)
    fmt.Printf("%#v\n", text)
}
```

#### Fscan系列

这几个函数功能分别类似于fmt.Scan、fmt.Scanf、fmt.Scanln三个函数，只不过它们不是从标准输入中读取数据而是从io.Reader中读取数据。

```go
func Fscan(r io.Reader, a ...interface{}) (n int, err error)
func Fscanln(r io.Reader, a ...interface{}) (n int, err error)
func Fscanf(r io.Reader, format string, a ...interface{}) (n int, err error)
```

#### Sscan系列

这几个函数功能分别类似于fmt.Scan、fmt.Scanf、fmt.Scanln三个函数，只不过它们不是从标准输入中读取数据而是从指定字符串中读取数据。

```go
func Sscan(str string, a ...interface{}) (n int, err error)
func Sscanln(str string, a ...interface{}) (n int, err error)
func Sscanf(str string, format string, a ...interface{}) (n int, err error)
```

