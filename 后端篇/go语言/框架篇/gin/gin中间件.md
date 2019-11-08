# 全局中间件

- 所有请求都经过此中间件

```go
package main

import (
    "fmt"
    "time"

    "github.com/gin-gonic/gin"
)

// 定义中间
func MiddleWare() gin.HandlerFunc {
    return func(c *gin.Context) {
        t := time.Now()
        fmt.Println("中间件开始执行了")
        // 设置变量到Context的key中，可以通过Get()取
        c.Set("request", "中间件")
        status := c.Writer.Status()
        fmt.Println("中间件执行完毕", status)
        t2 := time.Since(t)
        fmt.Println("time:", t2)
    }
}

func main() {
    // 1.创建路由
    // 默认使用了2个中间件Logger(), Recovery()
    r := gin.Default()
    // 注册中间件
    r.Use(MiddleWare())
    // {}为了代码规范
    {
        r.GET("/ce", func(c *gin.Context) {
            // 取值
            req, _ := c.Get("request")
            fmt.Println("request:", req)
            // 页面接收
            c.JSON(200, gin.H{"request": req})
        })

    }
    r.Run()
}
```

输出结果：

![img](http://www.5lmh.com/static/gin/4.1/1.png) ![img](http://www.5lmh.com/static/gin/4.1/2.png)

注意: 请注意黑色的数据里面有一步算时间差没有执行(需要学习Next就懂了)

# Next()方法

```go
package main

import (
    "fmt"
    "time"

    "github.com/gin-gonic/gin"
)

// 定义中间
func MiddleWare() gin.HandlerFunc {
    return func(c *gin.Context) {
        t := time.Now()
        fmt.Println("中间件开始执行了")
        // 设置变量到Context的key中，可以通过Get()取
        c.Set("request", "中间件")
        // 执行函数
        c.Next()
        // 中间件执行完后续的一些事情
        status := c.Writer.Status()
        fmt.Println("中间件执行完毕", status)
        t2 := time.Since(t)
        fmt.Println("time:", t2)
    }
}

func main() {
    // 1.创建路由
    // 默认使用了2个中间件Logger(), Recovery()
    r := gin.Default()
    // 注册中间件
    r.Use(MiddleWare())
    // {}为了代码规范
    {
        r.GET("/ce", func(c *gin.Context) {
            // 取值
            req, _ := c.Get("request")
            fmt.Println("request:", req)
            // 页面接收
            c.JSON(200, gin.H{"request": req})
        })

    }
    r.Run()
}
```

输出结果：

![img](http://www.5lmh.com/static/gin/4.1/3.png)

![img](http://www.5lmh.com/static/gin/4.1/2.png)

# 局部中间件

```go
package main

import (
    "fmt"
    "time"

    "github.com/gin-gonic/gin"
)

// 定义中间
func MiddleWare() gin.HandlerFunc {
    return func(c *gin.Context) {
        t := time.Now()
        fmt.Println("中间件开始执行了")
        // 设置变量到Context的key中，可以通过Get()取
        c.Set("request", "中间件")
        // 执行函数
        c.Next()
        // 中间件执行完后续的一些事情
        status := c.Writer.Status()
        fmt.Println("中间件执行完毕", status)
        t2 := time.Since(t)
        fmt.Println("time:", t2)
    }
}

func main() {
    // 1.创建路由
    // 默认使用了2个中间件Logger(), Recovery()
    r := gin.Default()
    //局部中间键使用
    r.GET("/ce", MiddleWare(), func(c *gin.Context) {
        // 取值
        req, _ := c.Get("request")
        fmt.Println("request:", req)
        // 页面接收
        c.JSON(200, gin.H{"request": req})
    })
    r.Run()
}
```

效果演示：

![img](http://www.5lmh.com/static/gin/4.1/3.png)

![img](http://www.5lmh.com/static/gin/4.1/2.png)

# 中间件练习

- 定义程序计时中间件，然后定义2个路由，执行函数后应该打印统计的执行时间，如下：

```go
package main

import (
    "fmt"
    "time"

    "github.com/gin-gonic/gin"
)

// 定义中间
func myTime(c *gin.Context) {
    start := time.Now()
    c.Next()
    // 统计时间
    since := time.Since(start)
    fmt.Println("程序用时：", since)
}

func main() {
    // 1.创建路由
    // 默认使用了2个中间件Logger(), Recovery()
    r := gin.Default()
    // 注册中间件
    r.Use(myTime)
    // {}为了代码规范
    shoppingGroup := r.Group("/shopping")
    {
        shoppingGroup.GET("/index", shopIndexHandler)
        shoppingGroup.GET("/home", shopHomeHandler)
    }
    r.Run(":8000")
}

func shopIndexHandler(c *gin.Context) {
    time.Sleep(5 * time.Second)
}

func shopHomeHandler(c *gin.Context) {
    time.Sleep(3 * time.Second)
}
```

效果演示：

![img](http://www.5lmh.com/static/gin/4.1/4.png)

