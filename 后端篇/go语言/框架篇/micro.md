#### GO-micro的使用

- 什么是micro

```go
// 框架和工具集： Go-Micro（库）、Micro（运行时工具集）
// 社区：slack.micro.mu
// 生态系统、平台Paas
```

Micro工具集组件

```go
// API
	- API：将http请求映射到api接口
	- RPC：将HTTP请求映射到RPC服务
	- event：将HTTP请求广播到订阅者
	- proxy：反向代理
	- web：支持对websocket的反向代理
// Web
	功能：web反向代理和管理控制台
// Proxy
	功能：代理micro风格的请求，支持异构系统只需要`瘦客户端`便可调用Micro服务
	注：与Micro API不同的是，Proxy只处理micro 风格的RPC请求，而非HTTP请求
// CLI
	功能：以命令行操作Micro服务
	执行：micro help了解更多
// Bot
	功能：与常用通信软件对接，负责传送信息，远程指令操作
	注：目前没有对接中国常用的微信、钉钉等
```

- GO-Micro框架的设计

![UTOOLS1577072081645.png](https://i.loli.net/2019/12/23/qgPUGMILhkAFrVl.png)

- GO-Micro主要的组件
- GO-Micro的插件化



