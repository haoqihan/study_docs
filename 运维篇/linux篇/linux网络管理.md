### 网络基础

#### OSI七层模型

```shell
ISO:国际标准化组织
OSI：开放系统互联模型
IOS：苹果操作系统
```

| 名称       | 详细                                         |
| ---------- | -------------------------------------------- |
| 应用层     | 用户接口                                     |
| 表示层     | 数据的表示形态，功能特定的实现：加密         |
| 会话层     | 对应用会话管理，同步                         |
| 传输层     | 可靠与不可靠传输，传输前的错误检测，流控     |
| 网络层     | 提供逻辑地址，选路                           |
| 数据链路层 | 成帧，用MAC访问媒介，错误检测与修正          |
| 物理层     | 设备之间的比特流的传输，物理接口，电气特性等 |

#### TCP/IP四层模型

OSI七层与TCP/IP的对应关系

```shell
应用层
表示层				应用层
会话层
传输层				传输层
网络层				网际互联层
数据链路层
物理层				网络接口层

网络接口层
  网络接入层与OSI参考模型中的物理层和数据链路层相对应，他负责监视数据在主机和网络之间的交换
  事实上，TCP/IP本身并未定义该层协议，而又参与互联的各网络接入层进行连接，地址解析协议（ARP）
  工作在此层，即OSI参考模型的数据链路层
网际互联层
   网际互联层对应于OSI参考模型的网络层，主要解决主机到主机的通信问题，他所包含的协议涉及数据包
   在整个网络上的逻辑传输，该层有三个主要协议：网际协议（IP），互联网组管理协议（IGMP）和互联网
   控制报文协议（ICMP）
传输层
   传输层对应OSI参考模型的传输层，为应用层实体提供端到端的通信功能，保证了数据包的顺序传送及
   数据的完整性，该层定义了两个主要协议：传输控制协议（TCP）和 用户数据报协议（UDP）
应用层
  应用层对应OSI参考模型的高层，为用户提供所需要提供的各种服务，如：FTP，Telnet，DNS，SMTP等

TCP/IP模型与OSI模型的比较
共同点
	OSI参考模型和TCP/IP参考模型都采用了分层结构的概念
	都能够提供面向连接和无连接两种通信服务机制
不同点
	前者是七层，后者是四层
	对可靠性要求不同
	OSI模型在协议开发前设计的，具有通用性，TCP/IP是现有协议然后集然后建立模型，不适用与非TCP/IP网络
	实际市场应用不同（OSI模型只是理论上的模型，并没有成熟的产品，而TCP/IP已经成为“实际上的国际标准”）
```

#### IP地址

##### ip地址分类

![img](https://images2015.cnblogs.com/blog/603942/201610/603942-20161024110358546-1282772232.png) 

##### 子网掩码的使用

```shell
三种：
	255.255.255.0
	255.255.0.0
	255.0.0.0
```

#### 端口作用

```shell
端口号是什么？
	计算机有2的16次方的端口号，可以通过端口找到对应服务
端口号的分类？
常见的端口号？
	FTP（文件传输协议）：端口号 20 21
	SSH（安全shell协议）：端口号 22
	telnet（远程登录协议）：端口号 23
	DNS（域名系统）： 端口号 53
	http（超文本传输协议）：端口号 80
	https（超文本传输安全协议）：端口号 443
	SMTP（简单邮件传输协议）：端口号 25
	POP3(邮局协议3代)： 端口 110
```

##### 查看本机启用的端口

```shell
netstat -an
选项：
	-a	查看所有连接和监听端口
	-n	显示IP地址和端口号，而不显示域名和服务名
```

#### DNS作用

```shell
将域名解析为IP地址
	客户机向DNS服务器发送域名查询请求
	DNS服务器告知客户机Web服务器的ip地址
	客户机与web服务器进行通信
从查询方式划分
	递归查询
		要么作出成功响应，要么一直作出查询失败的响应，一般客户机和服务区之间属递归查询，即客户机向DNS服务器
		发送请求后，若DNS服务器本身不能解析，则会向另外的DNS服务器发起查询请求，得到的请求转交给客户机
	迭代查询
		服务器收到一次迭代查询回复一次查询结果，但是这个结果不一定是目标IP与域名的映射关系，也可以是其他DNS服务器的地址
		
从查询内容上划分
	正向查询由域名查询IP地址
	反向查询由IP地址查找域名
```

#### 网关作用

1. 网关又称为网间连接器，协议转换器
2. 网关在网络层实现网络互连，是最复杂的网络互连设备，近用于两个高层协议不同的网络互连
3. 网关即可用于广域互连，也可以用于局域网互连
4. 网关是一种充当转换重任的服务器和路由器

```shell
网关的作用
	1.网关在所有内网计算机访问的不是本网段的数据报时使用
	2.网关负责将内网ip转换为公网ip，公网ip转换为内网ip
```

### linux网络配置

#### linux配置IP地址

```shell
service network  restart
# 重启网络

1.ifconfig命令临时配置IP地址
2.setup工具永久配置IP地址
3.修改网络配置文件
4.图形界面
```

#### linux网络配置文件

##### 网卡配置文件

```shell
vim /etc/sysconfig/network-scripts/ifcfg-eth0
# 查看网卡配置
DEVICE=eth0					网卡设备名
BOOTPROTO=static			 是否自动获取IP（none，static，dhcp）
HWADDR=00：0c:29:17:c4:09	MAC地址
NM_CONTROLLED=yes			是否可以由Network Manager图形管理工具托管
ONBOOT=yes					是否随网络服务启动，eth0生效
TYPE=Ethernet				类型为以太网
UUID="asdasdasda"			唯一标识码
IPADDR=172.17.189.129		 IP地址
NETMASK=255.255.240.0		 子网掩码
GATEWAY=192.168.19.0		网关
DNS1=8.8.8.8				DNS
IPV6INIT=no					IPV6没有启用
USERCTL=no					不允许非root用户控制此网卡
```

##### 主机名文件

```shell
vim /etc/sysconfig/network
# 查看主机名
NETWORKING_IPV6=no
PEERNTP=no
GATEWAY=172.17.191.253
HOSTNAME=root					主机名

hostname [主机名]
# 查看或临时设置主机名命令
```

##### DNS配置文件

```shell
vim /etc/resolv.conf 
# 查看DNS配置文件

nameserver 100.100.2.136			设置dns
nameserver 100.100.2.138
options timeout:2 attempts:3 rotate single-request-reopen
```

#### 虚拟机网络参数配置

```shell
1.配置linux的IP地址
	setup
	# 修改ip地址
	
2.启动网卡
vim /etc/sysconfig/network-scripts/ifcfg-eth0
把 ONBOOT=no
改为 ONBOOT=yes
service network restart
# 重启网络服务

3.修改UUID
	vim /etc/sysconfig/network-scripts/ifcfg-eth0
	# 删除MAC地址行
	
	rm -rf /etc/udev/rules.d/75-persistent-net-generator.rules
	# 删除网卡和MAC地址绑定文件
	
	重启系统
	
4.设置网络连接方式

5.修改桥接网卡
```

### Linux网络命令

#### 网络环境查看命令

##### 查看网络状态

```shell
ifconfig	查看与配置网络状态命令
```

##### 关闭和启动网卡

```shell
ifdown 网卡设备名
# 禁用该网卡设备

ifup 网卡设备名
# 启用该网卡设备
```

##### 查询网络状态

```shell
netstat 选项
选项：
	-t	列出TCP协议端口
	-u	列出UDP协议端口
	-n	不使用域名和服务名，而使用IP地址和端口号
	-l	仅列出在监听状态网络服务
	-a	列出所有的网络连接
	
netstat -rn
# 查看网关
route -n
# 查看路由列表

route add default gw 192.168.19.1
# 临时设定网关
```

##### 域名解析命令

```shell
yum install bind-utils -y
# 下载nslookup

nslookup [主机名或IP]
# 进行域名与IP地址解析
```

#### 网络测试命令

##### ping命令

```shell
ping [选项] ip或域名
# 探测指定IP或域名的网络情况
选项：
	-c	次数指定ping包的次数
```

##### telnet命令

```shell
telnet [域名或IP] [端口]
# 远程管理与端口探测命令
telnet 192.168.19.1 80
```

##### traceroute命令

```shell
traceroute [选项] IP或域名
# 路由跟踪命令
选项：
	-n	使用IP，不使用域名，速度更快
```

##### wget命令

```shell
wget http：//.........
# 下载命令
```

##### tcpdump命令

```shell
tcpdump -i eth0 -nnX port 21
选项：
	-i		指定网卡接口
	-nn		将数据包中的域名与服务转为IP和端口
	-X		将十六进制和ASCII码显示数据包内容
	port	指定监听的端口
```

### 远程登录

#### SSH协议原理

```shell
对称加密算法
  采用但要是密码系统的加密方法，同一个秘钥可以同时用作信息的加密和解密，这种加密方法称为对称加密，也称为单秘钥加密

非对称加密算法
  非对称加密算法又称为“公开秘钥加密算法”，非对称加密需要两个秘钥：公开秘钥和私有秘钥
```

##### ssh命令

```shell
ssh 用户名@ip
# 远程管理指定Linux服务器

scp [-r] 用户名@ip：文件路径 本地路径
# 下载文件

scp [-r] 本地文件 用户名@ip：上传路径
# 上传文件
# -r 代表上传下载的是目录
```

#### SecureCRT远程管理工具

#### Xshell工具和WinSCP文件传输工具