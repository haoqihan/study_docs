### go全部命令

```go
go <command> [arguments]

commands

        bug         启动错误报告
        build       编译包和依赖项
        clean       删除对象文件和缓存文件
        doc         显示包或符号的文档
        env         打印Go环境信息
        fix         更新包以使用新的API
        fmt         gofmt（重新格式化）包源
        generate    通过处理源生成go文件
        get         下载并安装包和依赖项
        install     编译和安装包和依赖项
        list        列出程序包或模块
        mod         模块维护
        run         编译并运行Go程序
        test        运行测试文件
        tool        运行指定工具
        version     打印版本信息
        vet         报告包中可能出现的错误

Additional help topics:

        buildmode   构建模式
        c           在go与c之间调用
        cache       build and test caching
        environment environment variables
        filetype    file types
        go.mod      the go.mod file
        gopath      GOPATH environment variable
        gopath-get  legacy GOPATH go get
        goproxy     module proxy protocol
        importpath  import path syntax
        modules     modules, module versions, and more
        module-get  module-aware go get
        packages    package lists and patterns
        testflag    testing flags
        testfunc    testing functions

Use "go help <topic>" for more information about that topic.

```

### 常用的命令

#### **build** 编译go程序

```go
// 编译main文件，生成的可执行程序会出现在当前目录下
go run main.go
```

#### doc 查看包的文档

```go
// 查看指定包的文档
go doc fmt
或
godoc fmt 
```

#### env 查看go的环境

```go
// 查看go的环境，会输出到终端上
go env 
```

#### fmt 格式化go文件

```go
// 会格式化你编写的go代码
go fmt main.go
或
gofmt main.go
```

#### get 下载包

```go
// 下载github上指定的包
go get 路径
```

#### install 编译

```
 编译执行文件，放到$GOPATH/bin
 编译模块，放到$GOPATH/pkg
```

#### version 版本信息

```go
// 打印版本信息
go version 
```

#### vet 静态检测

```go
go vet main.go
```









































