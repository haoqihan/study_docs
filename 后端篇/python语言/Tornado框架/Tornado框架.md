---
title: Tornado框架
date: 2019-01-15 19:06:18
tags: [tornado]
categories: [框架]
---

安装：

```shell
pip3 install tornado
```

快速启动：

```python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

常用模块

```shell
tornado.web RequestHandler和 Application 类处理http请求
tornado.template 模板渲染
tornado.touting 处理路由
```

异步网络模块

```shell
tornado.ioloop 事件循环
tornado.iostream 非阻塞socket封装
tornado.tcpserver 和 tornado.tcpclient
```

协程和并发模块

```shell
tornado.gen 协程模块
tornado.locks、tornado.queues 同步协程队列模块
```

