---
title: ansible的基本使用
date: 2019-01-13 16:25:34
tags: [ansible]
categories: [运维开发之路]
---

#### 一.简介

ansible是什么东西?官方的title是“Ansible is Simple IT Automation”——简单的自动化IT工具。这个工具的目标有这么几项：让我们自动化部署APP；自动化管理配置项；自动化的持续交付；自动化的（AWS）云服务管理。 

所有的这几个目标本质上来说都是在一个台或者几台服务器上，执行一系列的命令而已。就像我之前有介绍过的Fabric，以及我们基于Fabric开发的自动化应用部署的工具： Essay 。都是做了这么个事——批量的在远程服务器上执行命令 。 

那么fabric和ansible有什么差别呢？简单来说fabric像是一个工具箱，提供了很多好用的工具，用来在Remote执行命令，而Ansible则是提供了一套简单的流程，你要按照它的流程来做，就能轻松完成任务。这就像是库和框架的关系一样。 

当然，它们之间也是有共同点的——都是基于 paramiko 开发的。这个paramiko是什么呢？它是一个纯Python实现的ssh协议库。因此fabric和ansible还有一个共同点就是不需要在远程主机上安装client/agents，因为它们是基于ssh来和远程主机通讯的。 

#### 二.安装及初步使用

1. **编译安装,此处使用yum**

```shell
yum install epel   # 下载epel源
yum install -y ansible  # 安装ansible
```

2.**查看ansible生成的文件**

```shell
rpm -ql ansible
```

3.**查看ansible生成的命令**

```shell
ansible   			 # 用来执行ansible的一些命令
ansible-doc   		 # 用来查看ansible的模块的帮助信息
ansible-playbook   	  # 用来执行playbook
ansible-galaxy		  # 用来下载第三方的playbook
```

4.**ansible命令模式**

```shell
ansible <host-pattern> [options]
-a MODULE_ARGS  # 模块的参数
-C --check      # 测试,干跑
-f  FORKS       # 指定并发数
--list-hosts    # 列出host-pattern主机
--syntax-check  # 语法检查
-m  MODULE_NAME # 指定模块
```

5.**ansible第一条命令**

```shell
ansible  all -m  ping  # 跟系统自带的ping不一样
```

6.**host-pattern格式**

```shell
[web]
192.168.19.33
192.168.19.44
[db]
192.168.19.55
[cache]
192.168.19.66

www[001:006].example.com
指定所有  all
指定单台机器(指定多个机器)
指定分组(多个分组)
指定分组并集  # ansible "web:db" -m ping
指定分组的交集  # ansible "web:&db" -m ping
指定分组的差集  # ansible "web:!db" -m ping
```

7.**ansible-doc**

```shell
Usage: ansible-doc [-l|-F|-s] [options] [-t <plugin type> ] 
[plugin]
-a  # 列出所有的模块
-l  # 列出ansible的模块
-s  # 片段式显示模块的信息
```

8.**补充**

```shell
[name]   #分组
name=CentOS-$releasever - Base - mirrors.aliyun.com  #这个分组的名字
failovermethod=priority
baseurl=http://mirrors.aliyun.com/centos/$releasever/os/$basearch/ #分组的url,叫baseurl
        http://mirrors.aliyuncs.com/centos/$releasever/os/$basearch/
        http://mirrors.cloud.aliyuncs.com/centos/$releasever/os/$basearch/
gpgcheck=0 # gpgcheck=1需要验证key文件,gpgcheck=0不验证key
enabled=1 #enabled=1 表示分组可用,enabled=0表示分组是不可用的
gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-7 #key文件
```

#### 三.命令相关

##### 命令相关

1.**command**

```shell
ansible  web -m aommand "pwd"
ansible  web -a "chdir=/tmp/ mkdir /data2"  # 切换到/tmp并执行pwd
ansible  web -a  "creates=/etc/  mkdir /data2" # 判断creates是否存在,真就忽略后面的操作
ansible  web -a  "removes=/tmp/data  mkdir  /tmp/data2"  # 判断removes是否存在,假就忽略后面的操作
```

2.**shell**

```shell
ansible  web -m shell  -a "echo 'test1'|password --stdin test1" # 修改密码
ansible  192.168.19.9  -m  shell "/root/a.sh"  # 指定远程主机上的shell脚本
ansible  192.168.19.2  -m  shell  -a  "/root/a.py"  # 指定远程主机上的python文件
```

3.**sctipt**

```shell
ansible  all  -m  script  -a  "/root/a.sh"  # 执行管控机的shell脚本
```

##### 文件相关

1.**copy复制管控机文件到被管控机**

```shell
ansible  web  -m  copy  -a  "src=/etc/xxx  dest=/data/xxx"  # src指定源文件 dest指定目标文件
ansible  web  -m  copy  -a  "src=/etc/xxx  dest=/data/xxx backup=yes"  # backup备份
ansible  web  -m  copy  -a  "src=/etc/init.d dest=/data/"  # 复制目录和目录下的文件到远程主机,远程主机也是一个文件夹
ansible  web  -m  copy  -a  "src=/etc/init.d/ dest=/data/"  # 复制目录下的文件
ansible  web  -m  copy  -a  "src=/etc/xxx  dest=/data/xxx backup=yes mode=600"  # mode 指定权限,owner指定文件的属主,group用来指定属组
ansible  web  -m  copy  -a  "content='内容xxxxx' dest=/data10/xx.txt"  # content 直接写内容
```

2.**file**

```shell
ansible  db  -m  file  -a  "path=/data10  state=directory"  # path指定地址,state=directory表示创建文件夹
ansible  db  -m  file  -a  "path=/data10/xxx  state=touch"  # state=touch  表示创建新文件
ansible  db  -m  file  -a  "path=/data10/test1  state=absent"  # state=absent  代表删除
ansible db -m  file -a 'path=/data10/test10 src=/data10/test1 state=link' #src表示源文件,path是不是目标,state=link是不是创建一个软连接
```

3.**fetch**

```shell
ansible  db  -m  fetch  -a  "src=/etc/xxx dest/tmp"  # src源地址(在被控机器上),dest目标地址(管控机上的地址)每个管控机的文件都生成了一个目录,会保持文件的原来目录结构
```

##### 软件相关

1.**yum**

```shell
ansible  web  -m  yum  -a  "name=nginx state=installed"  # 安装nginx
ansible  web  -m  shell  -a  "rpm  -qa | grep nginx"  # 查看nginx是不是安装成功
ansible  web  -m  yum  -a  "name=nginx  state=absent"  # 卸载nginx
ansible  web  -m  yum  -a  "name=redis,memcached"
```

2.**pip**

```shell
ansible  web  -m  pip  -a  "name=Django==1.11.15"
```

##### 定时任务

1. **cron**

```shell
ansible  web  -m  cron  -a  "name=testjob  minute=4  job='echo 哈哈 > /tmp/xx.txt'"  # 创建 name:指定的cron名字  minute:指定分钟  hour:指定小时  day:指定天  month:指定月  weekday:指定周  job:指定要执行的命令
ansible  web  -m  cron  -a  "name=testjob  state=absent"  # 删除任务
ansible  web  -m  cron  -a  "name=testjob  minute=4  disabled=yes  job='echo 哈哈 > /tmp/xx.txt'"  # disabled=yes表示禁用
```

##### 用户相关

1. **user** 

```shell
ansible  web  -m  user  -a  "name=客户1  home=/data/客户1"  # 创建用户并指定家目录
ansible  web  -m  user  -a  "name=客户2  groups='xxx1,xxx2' home=/data/客户2"  # groups='xxx1,xxx2' 指定用户的附加组
```

##### 收集系统信息

1. **setup 收集系统信息**

```shell
 "ansible_all_ipv4_addresses" #ipv4简单信息
 "ansible_all_ipv6_addresses" #ipv6的简单信息
 "ansible_architecture": "x86_64", #系统架构
 "ansible_date_time": #系统时间
 "ansible_default_ipv4": #详细信息
 "ansible_devices": #磁盘信息
 "ansible_distribution_major_version": "7",#系统版本
 "ansible_distribution": "CentOS", #系统的发行商
 "ansible_distribution_file_variety": "RedHat", #系统系列
 "ansible_fqdn": "localhost.localdomain", #系统的主机名
 "ansible_hostname": "localhost",#简写主机名
 "ansible_kernel": "3.10.0-693.el7.x86_64", #系统的内核版本
 "ansible_os_family": "RedHat",# 系统的家族
 "ansible_processor_vcpus": 2, #cpu的个数
 "ansible_python_version": "2.7.5", # ansible所用python的版本
 
  ansible web -m setup -a 'filter="*cpu*"'  #filter搜索
```

##### 启动应用

1. **service**

```shell
enabled:#开机启动
name:#服务的名称
state: #操作
```

**四.playbook的基本使用**

**playbook命令**,建议:一个文件做一件事

1.**基本格式**

```shell
ansible-playbook [options] playbook.yml
-C # 干跑,检查
-f FORKS # 用来做并发,来指定并发数
--list-hosts #列出执行命令的主机
--syntax-check # 检查语法
--list-tasks #列出playbook要执行的任务列表
-t TAGS, #指定要运行到tags
-e EXTRA_VARS #给playbook传递变量
```

2.**单个playbook**

```shell
#单个playbook
- hosts: web  #指定要运行命令的主机
  remote_user: root # 指定运行命令的用户
  tasks: #任务列表
  - name: mkdir # 任务1,name是必须的
    file: path=/data state=directory # 指定的模块: 模块的参数
  - name: copyfile
    copy: src=/etc/fstab dest=/data/f
```

3.**多个playbook**

```shell
##多个playbook
- hosts: web
  remote_user: root
  tasks:
  - name: mkdir
    file: path=/data state=directory
  - name: copyfile
    copy: src=/etc/fstab dest=/data/f

- hosts: db
  remote_user: root
  tasks:
  - name: wget
    shell: "wget -O /data/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo"
```

4.**指定tags**

```shell
##指定tags
- hosts: web
  remote_user: root
  tasks:
  - name: mkdir
    file: path=/data state=directory
  - name: copyfile
    copy: src=/etc/fstab dest=/data/f
    tags: copyfile
```

##### 变量

1.**第一种**

```shell
## 传递变量 -e"key=value"
- hosts: web
  remote_user: root
  tasks:
  - name: yum {{pkg_name}} pkg
    yum: name={{pkg_name}}
```

2.**第二种**

```shell
- hosts: web
  remote_user: root
  vars:
    - pkg_name: memcached
  tasks:
  - name: yum {{pkg_name}} pkg
    yum: name={{pkg_name}}
```

3.**第三种**

```shell
#在hosts文件里面写,值可以不同
[web]
192.168.19.9 pkg_name=nginx
192.168.19.26 pkg_name=redis
```

4.**第四种**

```shell
[web:vars]
pkg_name=nginx
```

5.**变量的应用顺序**

```shell
-e > yml文件 > hosts文件 #命令行里面是最高的,hosts文件是最低的
```

##### 条件

1. **when 条件判断**

```shell
- hosts: cache
  remote_user: root
  tasks:
  - name: copyfile1
    copy: content='wusir zhenchou' dest=/tmp/a.txt
    when: ansible_os_family=="RedHat" #只有为真的时候才会执行上面的操作
  - name: copyfile2
    copy: content='alex gengchou' dest=/tmp/b.txt
    when: ansible_os_family=="OpenBSD"
```

##### 循环with_items

1.**循环单个**

```shell
- hosts: cache
  remote_user: root
  tasks:
  - name: create user
    user: name={{item}} ## 循环下面的with_items
    with_items:
    - yuchao
    - yantao
  - name: create group
    group: name={{item}}## 循环下面的with_items
    with_items:
    - yuchao2
    - yantao2
```

2.**循环嵌套**

```shell
- hosts: cache
  remote_user: root
  tasks:
  - name: create group
    group: name={{item}}
    with_items:
    - yuchao4
    - yantao4
  - name: create user
    user: name={{item.name}}  group={{item.group}} #可以通过字典取值
    with_items:
    - {"name":yuchao3,"group":yuchao4}
    - {"name":yantao3,"group":yuchao4} 
```

##### 模板文件

1.**模板的基本使用**

```shell
 - hosts: cache
     remote_user: root
     tasks:
     - name: install redis
       yum: name=redis
     - name: copyfile
       template: src=redis.conf.j2 dest=/etc/redis.conf ## 模板基于jinja2
     - name: start
       service: name=redis state=started
     #模板文件放在templates,可以直接用相对路径去调用配置文件  
```

#### roles(高级使用)

1. **作用**	
	1. 结构清晰
	2. 可以重用
2. **结构**

```shell
tasks #目录是必须的,存放任务
templates #是存放模板
vars #用来存放变量    ### 切记,不能加-,加-报错
files #用来存放文件
mkdir -p {nginx,uwsgi,mysql}/{tasks,templates,vars,files} #创建目录结构的命令
```

#### 补充

**生成公私钥**

```shell
ssh-keygen
```

**复制公钥到远程主机**

```shell
ssh-copy-id  192.168.19.99
```

**ping命令发送的是ICMP协议**

**查看用户相关**

```shell
tail -l /etc/shadow  查看最后一个用户
echo "testl" | password  --stdin testl 设置用户密码,不需要二次确
useradd  # 创建用户默认的家目录在/home  -d 可以指定用户的家目录
groupadd  # 用来创建用户组,用户组没有家目录
```

**创建链接**

```shell
ln  创建硬链接  链接文件变更 源文件不变
ln  -s  创建软连接  链接文件变更 源文件变
```

**pip的基本使用**

```shell
pip  freeze  >  file  # 给当前的python模块做快照
pip  install  -r  xxx.txt   # 安装
pip  list  # 查看所有的python模块
```

1. **crontab定时任务**

```shell
* */5 * * * job  #/n 表示每隔n 
0 */5 * * 3,6 job  #3,6 表示周三和周六
## 切记 最前面不能用*,表示每时每刻都在执行,一定要有一个时间
## 应用场景: 打包日志,定期的同步时间,备份
-e  # 编辑
-l  # 列出
-r  # 删除
```

**启动应用**

```shell
systemctl  restart  nginx  # centos7中的操作应用
service  nginx  restart  # centos6里面的操作
```

**查看系统内存使用量**

```shell
free -m 查看系统的内存使用量
```

**Ad-hoc**:命令行的意思

**mv 的使用**

```shell
mv redis.conf{,.j2} == mv redis.conf redis.conf.j2
```

**yum和rpm的基本使用**

```shell
yum remove 卸载
rpm redhat pk manage
yum 自动解决依赖关系
rpm 不会自动解决依赖关系
```

**CI和CD的基本使用**

```shell
CI 持续交付  jenkins  maven war包
CD 持续集成  脚本去做 docker (最大的一个作用,到处运行  )   k8s
```

**暂时关闭防火墙**

```shell
setenforce 0 #暂时关闭selinux
```

**uwsgi的配置**

```shell
[uwsgi]
http = :8000   #端口
#the local unix socket file than commnuincate to Nginx
socket = /data/mysite/mysite.socket  #socket 只能本机使用
# the base directory (full path)
chdir = /data/mysite #当前工作目录
# Django's wsgi file
wsgi-file = mysite/wsgi.py  #要执行的文件
# maximum number of worker processes
processes = 4 #进程数
#thread numbers startched in each worker process
threads = 2 #线程数
# clear environment on exit
vacuum          = true
daemonize = /data/mysite/uwsgi.log  #后台启动,并提供日志
py-autoreload=1 #py文件变更后uwsgi自动重启           
kill -9 可以杀死父进程
```

**启动uwsgi**

```shell
uwsgi --http :8000 --module mysite.wsgi ## --http 启动的端口 --module 项目.wsgi文件
```

