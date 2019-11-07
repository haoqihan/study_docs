### HTTP协议

http1.0

```shell
1.明文
2.传输
3.header太长
4.server 主动push
```

http2.0

```shell
1.二进制
2.单链接+帧
3.头部压缩
4.push

```

http3.0

```shell
tcp -> udp

```







#### HTTP协议的定义

> 一种无状态的、应用层的、以请求/应答方式运行的协议，它使用可扩展的语义和自描述消息格式，与基于网络的超文本信息系统灵活的互动

#### HTTP协议的格式

![UTOOLS1562919355174.png](https://i.loli.net/2019/07/12/5d2841af9785e18217.png)

#### ABNF扩展巴克斯范式

![UTOOLS1562919439922.png](https://i.loli.net/2019/07/12/5d284202f312937289.png)

![UTOOLS1562919543557.png](https://i.loli.net/2019/07/12/5d28426a9a6b847854.png)

![UTOOLS1562919573465.png](https://i.loli.net/2019/07/12/5d284288841d970615.png)

![UTOOLS1562919616635.png](https://i.loli.net/2019/07/12/5d2842b3bb6ab73306.png)

### OSI模型

#### 七层模型

![UTOOLS1562919707551.png](https://i.loli.net/2019/07/12/5d28430eaf61a88596.png)

#### osi和tcp/ip对比关系

![UTOOLS1562919767107.png](https://i.loli.net/2019/07/12/5d28434a31d8063319.png)

### http解决的问题

- HTTP协议
  - Roy Thomas Fielding ：HTTP主要作者，REST架构作者
- URL 统一资源标识符

![UTOOLS1573095408838.png](https://i.loli.net/2019/11/07/xhnk1sTzQU9pdVS.png)

### 解决www信息交互必须面对的需求

- 低门槛
- 可扩展性：巨大的用户群体，超长的寿命
- 分布式系统下的Hypermedia，大粒度数据的网络传输
- internet规模
  - 无法控制的scalabilty
    - 不可预测的负载，非法格式的数据，恶意信息
    - 客户端不能保持所有服务器信息，服务器不能保持多个请求见的状态信息
  - 独立的组件部署，新老组件并存
- 向前兼容

### 如何使用network面板来抓包

```shell
快捷键： ctrl + shift + i
```

- **控制器**：控制面板的外观与功能
- **过滤器**:过滤请求列表中显示的资源
  - 按住ctrl ，然后点击过滤器可以同时选择多个多滤器
- 概览：显示HTTP请求，相应时间轴
- 请求列表：默认时间排序，可选择显示列
- 概要：请求总数，总数据量，总花费时间



#### 数据请求的流程

![UTOOLS1562985509653.png](https://i.loli.net/2019/07/13/5d2944181bde460973.png)

![UTOOLS1562985563419.png](https://i.loli.net/2019/07/13/5d29444cb8fc713756.png)



### http的请求行

- request-line = mothod SP request-target SP HTTP-version CRLF

![UTOOLS1573095408838.png](https://i.loli.net/2019/11/07/xhnk1sTzQU9pdVS.png)

- method 方法：指明操作目的，动词
-  request-target = origin-form/absolute-form/authority-form / asterisk-form
  - origin-form = absolute-path["?",query]
    - 向origin server 发起请求，path为空时必须传递 `/`
  - absolute-form = absolute-URL
    - 仅用于正向代理proxy发起请求时，详见正向代理与隧道
  - authority-form = authority
    - 仅用于CONNECT方法，例如：CONNECT www.xxxx.com:80 HTTP/1.1
  -  asterisk-form = "*"
    - 仅用于OPTIONS方法
- 版本号
  - HTTP/0.9 只支持GET方法，过时
  - HTTP/1.0 常见使用于代理服务器（例如Nginx默认配置）
  - HTTP/1.1 : 1999
  - HTTP/2.0 : 2015.5 正式发布
- 常用方法
  - GET：主要获取信息方法，大量的性能优化都针对该方法，幂等方法
  - HEAD： 类似GET方法，但服务器不发送BODY，用以获取header元素
  - POST：常用于提交HTML FORM表单，新增资源等
  - PUT：更新资源，带条件时是幂等方法
  - DELETE：删除资源，幂等方法
  - CONNECT：建立tunnel隧道
  - OPTIONS：显示服务器对访问资源支持的方法，幂等方法
  - TRACE：回显服务器收到的请求，用于定位问题，有安全风险
- 用于文档管理的webdav方法
  - PROPFIND：从web资源中检索以xml格式存储的属性，它也被重载，以允许一个检索远程系统的集合结构（也叫目录层次结构）
  - proppctch:在单个原子性动作中更改和删除资源的多个属性
  - MKCOL：创建结合或者目录
  - COPY：将资源从一个URI复制到另一个URI
  - MOVE：将一个资源的从一个URI移动到另一个URI
  - LOCK：锁定一个资源，webDEV支持共享锁和互斥锁
  - UNLOCK：解除资源的锁定











