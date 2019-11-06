#### 自动化运维工具

部署类：jenkins

环境类：ansible

监控类：ngios

#### ansible的使用

- 自动化 管理  IT资源 的工具

##### 功能

- 系统环境配置
- 安装软件
- 持续集成
- 热回滚

##### 优点

- 无客户端
- 推送式
- 丰富的module
- 基于YAML的playbook
- 商业化支持

##### 缺点

- 效率低，易挂起
- 并发性差

#### Ansible配置详解

```shell
defaults 默认配置项
privilege_escalation  执行命令的用户权限设置
paramiko_connection paramika 插件设置
ssh_connection ssh 连接设置
accelerate
selinux & colors
```

```shell
ask_pass & ask_sudo_pass

ask_pass :可以控制Ansible剧本playbook是否会自动默认弹出默认密码
ask_sudo_pass:用户使用的系统平台开启了sudo密码的话，应该开绿这一个参数
```

```shell
gather_subset

设置收集的内容：包括all，network，hardware，virtual，facter，ohai
```

```shell
remote_port & remote_tmp & remote_user

客户机设置，分别对登录的用户和端口，以及临时目录
```

```shell
sudo_exe & sudo_flags & sudo_user

sudo命令相关设置，分别是sudo命令路径，sudo参数，能够使用sudo的user
```

```shell
action_plugins & callback_plugins &connection_plugins & filter_plugins & lookup_plugins & vars_plugins

开发者中心的插件相关功能，开发者可以开发相应的插件，来完成自己的功能，分别对一个的功能为：激活事件，回调，连接。过滤器，加载路径，任何地方加载
```

```shell
forks

最大开辟的进程数，这个数不易过大，过大性能消费高，过小，并发性能低，一般设置方法：cpu核数*2
```

```shell
module_name

这个是/user/bin/ansible的默认模块名 （-m） 默认是‘command’模块，‘command’模块不支持shell变量，管道，配额，所以需要把这个参数设置为shell
```

```shell
vault_password_file

这个文件也可以称为一个脚本的形式，如果你使用脚本而不是单纯文件的话，请确保它可以执行并且密码可以在标准输出中打印出来，如果你的脚本需要提示请求数据，请求将会发到标准错误输出中
```

```shell
pattern

如果没有提供“hosts”节点，这是playbook要通信的默认主机组，默认值对所有主机通信，如果不想被惊吓到，最好还是设置个选项
```

```shell
inventory & library

分别为存放主机目录和Ansible默认搜索模块路径
```

#### Ansible的使用

##### 如何添加一台机器？

- 1.编辑/etc/ansible/hosts
- 2.添加本机的public SSH Key 到目标机器的authorized_keys
- 3.添加本机私钥到Ansible（可以省略）
- 运行ansible all -m ping  测试是否添加成功

##### Ansible命令格式-ansible all -m ping

- Ansible命令主题 ansible/Ansible-playbook
- 被操作的目标机器的正则表达式 --all
- 指定要使用的模块  -m ping
- 传入参数

```shell
-a				 指定传入模块的参数
-C -D 			 两个一起使用，检查hosts规则文件的修改
-l				限制匹配规则的主机数
--list-hosts 	 显示所有匹配规则的主机数
-m -M			指定所使用的模块和模块路径
--syntax-check	 检查语法
-v				显示详细日志
```

```shell
ip域名写起来太长，起一个别名
jumper ansible_ssh_port=5555 ansible_ssh_host=192.168.19.128

不想以ROOT用户登录
jumper ansible_ssh_port=5555 ansible_ssh_host=192.168.19.128 ansible_ssh_user=oooo

机器太多，但是是连续的
【vim】
vim[1:50].xxx.com
vim[a-z].xxx.com

什么是patterns
	是指我们通过类正则表达式的方式，决定于哪台主机进行交互
如何执行一个耗时任务
	ansible all -B 3600 -P 0 -a "ls"
	-B 3600 表示最多运行60分钟 -P 0表示不获取状态 -p 60 表示每隔1分钟获取一次状态
```

```shell
其他模块
	git模块
	service模块	系统服务相关
	setup模块	系统环境相关

```

#### 免密登录

```shell
ssh-keygen  # 一直敲击回车即可
ssh-copy-id ip地址
```

#### Ansible API

#### SaltStack

##### 概念

- 一个配置管理系统，能够维护预定义状态的远程节点
- 一个分布式远程执行系统，用来在远程节点上执行命令和查询数据

##### 特点

- 简单（相对Puppet）
- 并行执行
- 基于成熟技术（ZeroMQ，AES）
- python API
- 灵活，开源

##### 服务架构

- Master    负责管理所有节点
- Minion    节点服务
- zeroMQ    通信方式
- AES    数据加密方法

##### 缺点：

- 需要单独安装客户端
- 安全隐患大

##### ZerMQ简述

以嵌入式网络编程库的形式实现了一个并行开发框架，能够提供进程内，进程间，网络和广播方式的消息通道，并支持 发布-》订阅 ，任务分发，请求响应等通信模式

#### Saltstack安装配置运行

##### 安装

```shell
py2.6 ~ py3
zeroMQ or RAET
mako(可选) 一个可选的salt States解析器
gcc（可选）


```

##### 配置

##### 运行

1. 运行Master节点
2. 修改Minion节点配置，填入Master节点信息
3. 启动Minion
4. Master节点添加Minion

##### 配置项











