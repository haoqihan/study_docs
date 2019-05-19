---
title: Linux之网络服务
date: 2019-02-18 14:48:54
tags: [linux]
categories: [linux]
---

### Bind服务

```shell
BIND
开源，稳定，应用广泛的DNS服务
组成
	域名解析服务
	权威域名服务
	DNS工具
	
DNS中的域名
	www.baidu.com = www.baidu.com.(.代表根域。com代表一级域名，baidu代表二级域名)
	
DNS解析记录分类
	A记录，CNAME，NS记录，MX记录

```

```shell
安装BIND
Redhat家族：yum install bind bind-chroot
Ubuntu家族：sudo apt-get install bind9
```

```shell
配置文件
	options{}整个BIND使用的全局选项
	logging{} 服务日志选项
	zone {} DNS域解析
```

### Bind负载均衡

### 智能DNS