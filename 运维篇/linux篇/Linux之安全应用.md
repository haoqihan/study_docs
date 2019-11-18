### 主机扫描

#### 网络入侵方式

踩点-》网络扫描-》查点-》提权

#### 实例中运用到的命令

tracert，nmap，nc

#### 主机扫描命令 fping

作用：

​	批量的给目标主机发送ping命令，测试主机的存活情况

特点：

​	并行发送，结果易读

##### fping参数介绍

命令参数man、-h方式

```shell
-a	只显示存活的主机（相反参数 -u）

1.通过标准输入方式
fping + IP1 + IP2
	-g	支持主机段的方式192.168.1.1 192.168.1.255 或 192.168.1.0/24
	
2.通过读取一个文件中的IP内容
    方式：fping -f filename
```

#### 主机扫描命令hping

```shell
报错查看：https://www.cnblogs.com/fwonfo/p/7735756.html
安装：
    下载地址：www.hping.org
依赖：
	yum install -y  libpcap libpcap-devel
	ln -sf /usr/include/pcap-bpf.h /usr/include/net/bpf.h
安装步骤：
	./configure && make && make install
特点：支持使用的TCP/IP数据包组装，分析工具
参数：
	对指定目标发起tcp探测
	-p	端口
	-s	设置TCP模式SYN包
	伪造来源IP，模拟Ddos攻击
	-a	伪造IP地址
	

# 屏蔽ping命令
```

### 路由扫描

作用：查询一个主机到另一个主机的经过路由的跳数，及数据延迟情况

```shell
常用工具：traceroute，mtr
mtr特点：能测试出主机到每一个路由间的联通性
```

#### Traceroute参数介绍

```shell
一。默认使用的是UDP协议（30000上的端口）
二.使用TCP协议 -T -p
三。使用ICMP协议 -I

mtr + 域名
```

### 批量主机服务扫描

目的：

- 批量主机存活扫描
- 针对主机服务扫描

作用

- 能更方便快捷获取网络中主机的存活状态
- 更加细致，智能获取主机服务侦查情况

```shell
命令：nmap和ncat

ncat工具使用
组合参数：
-w设置的超时时间
-z 一个输入输出模式
-v	显示命令执行过程
方式一。基于tcp协议（默认）
	nc -v -z -w2 39.105.162.164 1-50
方式二。基于UDP协议
	nc -v -u -z -w2 39.105.162.164 1-50
```

| 扫描类型                | 描述          | 特点                   |
| ----------------------- | ------------- | ---------------------- |
| ICMP协议类型（-sP）     | ping扫描      | 简单，快速，有效       |
| TCP SYN扫描（-sS）      | TCP半开放扫描 | 高效，不易被检测，通用 |
| TCP connect 扫描（-sT） | TCP全开放扫描 | 真实，结果可靠         |
| UDP扫描（-sU）          | UDP协议扫描   | 有效透过防火墙策略     |

### linux防范恶意扫描安全策略

```shell
常见的攻击方式：
	SYN攻击
	DDOS攻击
	恶意扫描
什么是SYN攻击？
	利用TCP缺陷进行，导致系统服务停止响应，网络带宽跑满或者响应缓慢
什么是DDOS攻击
	分布式访问拒绝服务攻击
SYN类型DDOS攻击防御
方式一：减少发送syn+ack包重试次数
	sysctl -w net.ip4.tcp_synack_retries=3
	sysctl -w net.ip4.tcp_syn_retries=3
方式二。SYN cookie技术
	sysctl -w net.ipv4.tcp_syncookies=1
方式三。增加backlog队列
	sysctl -w net.ipv4.tcp_max_backlog=2048

其他预防策略
策略1.如何关闭ICMP协议请求
	sysctl -w net.ipv4.icmp_echo_ignore_all=1
策略2.通过iptables防止扫描
	
```

### iptables的使用

#### 关于iptables

##### 什么是iptables？

常见于linux系统下的应用层防火墙

##### 常见人员

系统管理人员，网络工程人员，安全人员等等



