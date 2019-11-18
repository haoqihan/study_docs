[学习地址](https://github.com/A-BenMao/pure-bash-bible-zh_CN)

### 主控脚本实现

#### vim编辑器设置

```shell
语法高亮
	syntax on
显示行号
	set number
自动缩进
	set autoindent
	set cindent
自动加入文件头

```

#### shell编程高级知识

##### shell高亮显示

```shell
基本格式：
	echo -e 终端颜色 + 内容 + 结束后的颜色
例子：
	echo -e "\e[1;30m 内容 \e[1;0m"
	echo -e "\e[1;30" "内容" $(tupt sgr0)
```

##### shell中的关联数组

```shell
关联数组：
	普通数组：只能使用整数作为数组索引
	关联数组：可以使用字符串作为数组索引
	
	申明关联数组变量
	# declare -A ass_array1
	
	数组名[索引]=变量值
	# ass_array1[index1]=per
```

##### monitor.sh脚本

```shell
#/bin/bash
resettem=$(tput sgr0)
declare -A ssharray
i=0
numbers=""

for script_file in `ls -I "monitor_man.sh" ./`
do
        echo -e "\e[1;30]" "The script:" ${i} '===>' ${resettem} ${script_file}
        ssharray[$i]=${script_file}
        numbers="${numbers} | ${i}"
        i=$((i+1))
done
echo "结束l"
while true
do
        read -p "请输入数字 [${numbers}]:" execshell
        echo ${execshell}
        if [[ ! ${execshell} =~ ^[0-9]+ ]]; then
                exit 0
        fi
        /bin/sh ./${ssharray[${execshell}]}
done
```

### 系统信息及运行状态获取

脚本system_monitor.sh

功能一、提取操作系统信息（内核，系统版本，网络地址）

功能二、分析系统的运行状态（cpu负载，内存及磁盘使用率等）

```shell
#/bin/bash
clear
if [[ $# -eq 0 ]]
then
reset_terminal=$(tput sgr0)
# 提取操作系统类型
	os=$(uname -o)
	echo -e  "\e[1;33m" "操作系统类型" $reset_terminal $os
# 获取操作系统发行版本
	os_name=$(lsb_release -d)
	echo -e '\e[1;32m' "操作系统发行版本" $reset_terminal $os_name

# 获取系统架构信息
	architecture=$(uname -m)
	echo -e "\E[32m" "操作系统位数" $reset_terminal $architecture

# 获取内核信息
	kernerrelease=$(uname -r)
	echo -e "\E[32m" "内核信息：" $reset_terminal $kernerrelease

# 主机名
	hostname=$HOSTNAME
	echo -e "\E[32m" "主机名" $reset_terminal $hostname

# 获取内网ip
	internalIP=$(hostname -I)
	echo -e  "\E[32m" "内网IP地址：" $reset_terminal $internalIP
	
# 获取公网ip
	externalip=$(curl -s http://ipecho.net/plain)
	echo -e  "\E[32m" "公网IP：" $reset_terminal $externalip

# 获取DNS
	nameservers=$(cat /etc/resolv.conf | grep nameserver | awk '{print $NF}')
	echo -e  "\E[32m" "DNS：" $reset_terminal $nameservers

# 查看网络是否通畅
	ping -c 2 www.baidu.com &>/dev/null && echo "网络通畅" || echo “网络不通畅”
# 查看当前用户登录数
	who>/tmp/who
	echo -e "\E[32m" "当前在线用户" $reset_terminal  && cat /tmp/who
	rm -f /tmp/who
fi
```

#### 分析系统的运行状态

- 系统使用的内存和应用使用的内存区别
	- 系统使用内存=Total-Free
	- 应用使用内存Total-（Free+Cached+Buffers）
- 内存中的cache和buffer的区别

|        | 功能                                | 读取策略     |
| ------ | ----------------------------------- | ------------ |
| cache  | 缓存主要用于打开的文件              | 最少使用原则 |
| Buffer | 分缓存主要用于目录项，inode等文件系 | 先进先出策略 |

- CPU负载概念

### nginx和mysql应用状态分析

#### 应用运行状态监控脚本

##### 利用操作系统命令

网络命令：ping、nslookup、nm-tool、tracer、traceroute、dig、telnet、nc、curl

监控进程：ps、netstat、pgrep

应用客户端：mysql、ab、mongo、php、jstack

第三方工具包：nginxstatus、nagios-libexec

服务端接口支持

- nginx -http_stub_status_module
- nutcracker监控集群（redis、memcache）状态
- Mongodb

监控mysql主从复制状态

- 搭建主从复制环境
- 基于mysql客户端连接，获取主从复制状态
- myslq > show slave status\G
- Slave_IO_Running-IO线程是否有连接到主服务器上
- Seconds_Behind_Master 主从同步的延时时间
- 

### 应用日志分析

#### 系统日志文件

- /var/log/messages  // 系统主日志文件
- /var/log/secure  // 认证，安全
- /var/log/dmesg  //和系统启动相关

#### 应用服务

- access.log  //nginx访问日志
- mysqld.log  //mysql运行日志
- xferlog  //和访问FTP服务器相关

#### 程序脚本

- 开发语言：c、C++、java、php
- 框架：Django、MVC、servlet
- 脚本语言：shell、python

#### Http状态码

- 1**	信息服务收到请求，需要请求者进一步操作
- 2**    成功，操作被成功接收并处理
- 3**    重定向，需要进一步的操作以完成请求
- 4**    客户端错误
- 5**    服务器错误

#### 脚本功能介绍

- 功能一、分析HTTP状态码在100，200,300,400,500之间及以上的请求条数
- 分析日志中http状态码为404,500的请求条数











