---
title: linux系统管理
date: 2019-02-14 19:34:05
tags: [linux]
categories: [linux]
---

### 进程管理

#### 进程管理简介

- 进程是正在执行的一个程序或命令，每一个进程都是一个运行的实体，都有自己的地址空间，并占用一定的系统资源

##### 进程管理的作用

- 判断服务器健康状态
- 查看系统中所有进程
- 杀死进程

#### 进程管理查看 -ps命令和pstree命令

##### 查看所有进程

```shell
ps aux
# 查看系统中所有进程，使用BSD操作格式
ps -le
# 查看系统中所有进程，使用Linux标准命令格式
选项：
	-a	显示一个终端的所有进程，除了会话引线
	-u	显示进程的归属用户及内存的使用情况
	-x	显示没有控制终端的进程
	-l	长格式显示，显示更加详细的信息
	-e	显示所有进程，和-A作用一直
```

##### ps命令输出

```shell
USER	该进程由那个用户产生的
PID		进程的PID号
%CPU	该进程占用CPU资源的百分比，占用越高，进程越耗费资源
%MEM	该进程占用物理内存的百分比，占用越高，进程越耗费资源
VSZ		该进程占用虚拟内存大小，单位为kb
RSS		该进程占用实际物理内存大小，单位kb
TTY		该进程是在哪个终端中运行的，其中tty-tty7代表本地控制台终端，tty1-tty6是本地的字符页面终端，tty7是图像终端，pts/0-255代表虚拟机

STAT	进程状态，常见状态有
	R	运行
	S	睡眠
	T	停止状态
	s	包含子进程
	+	位于后台
START	该进程启动时间
TIME	该进程占用CPU的运算时间，注意不是系统时间
COMMAND	产生此进程的命令名
```

##### pstree命令

```shell
查看进程树
pstree [选项]
选项：
	-p	显示进程的PID
	-u	显示进程的所属用户
```

#### 进程查看 top命令

```shell
top [选项]
选项：
	-d	秒数，指定top命令每隔几秒更新，默认3秒
	-b	使用批处理模式输出，一般和“-n”选项和用
	-n	次数，指定top命令执行的次数，一般和“-b”选项和用
	
在top命令的交互模式当中可以执行的命令
命令：
	？或h	显示交互模式的帮助
	 P	  以CPU使用率排序，默认就是此项
     M	  以内存使用率排序
     N	  以PID排序
     q	  退出top
     
详细信息
    第一行 (uptime)
    系统时间 主机运行时间 用户连接数(who) 系统1，5，15分钟的平均负载
    第二行:进程信息
    进程总数 正在运行的进程数 睡眠的进程数 停止的进程数 僵尸进程数
    第三行:cpu信息
    1.5 us：用户空间所占CPU百分比
    0.9 sy：内核空间占用CPU百分比
    0.0 ni：用户进程空间内改变过优先级的进程占用CPU百分比
    97.5 id：空闲CPU百分比
    0.2 wa：等待输入输出的CPU时间百分比
    0.0 hi：硬件CPU中断占用百分比
    0.0 si：软中断占用百分比
    0.0 st：虚拟机占用百分比

    第四行：内存信息（与第五行的信息类似与free命令）
    total：物理内存总量
    used：已使用的内存总量
    free：空闲的内存总量（free+used=total）
    buffers：用作内核缓存的内存量

    第五行：swap信息
    total：交换分区总量
    used：已使用的交换分区总量
    free：空闲交换区总量
    cached Mem：缓冲的交换区总量，内存中的内容被换出到交换区，然后又被换入到内存，但是使用过的交换区没有被覆盖，交换区的这些内容已存在于内存中的交换区的大小，相应的内存再次被换出时可不必再对交换区写入。
```

#### 杀死进程

##### kill命令

```shell
kill -l
# 查看可用的进程信号

kill -9 2236
# 强制杀死进程

```

##### killall命令

```shell
killall [选项][信号] 进程名
# 按照进程名杀死进程
选项：
	-i	交互式，询问是否杀死某个进程
	-I	忽略进程名大小写
```

##### pkill命令

```shell
pkill [选项][信号] 进程名
# 按照进程名终止进程
选项：
	-t	终端号，按照终端号踢出用户
```

#### 修改进程优先级

```shell
nice命令
# nice命令可以给新执行的命令直接赋予NI值，但是不能修改已经存在进程的NI值
选项：
	-n	NI值，给命令赋予NI值
例如：
	nice -n （-20到19） service httpd start

renice命令
# renice命令是修改已经存在进程的NI值的命令
例如：
	renice -10 2255（PID）

```

### 工作管理

- 当前的登录终端，只能管理当前终端的工作，而不能管理其他登录终端工作
- 放入后台的命令必须可以持续运行一段时间，这样我们才能捕捉和操作这个任务
- 放入后台执行的命令不能和前台用户有交互或需要前台输入，否则放入后台只能暂停，而不能执行

#### 把进程放入后台

```shell
tar -zcf etc.tar.gz /etc &
# 把命令放入后台，并在后台执行

top
# 按下ctrl + z 快捷键，放在后台暂停
```

#### 查看后台的工作

```shell
jobs [-l]
选项：
	-l	显示工作的PID
注释：“+”号代表最近一个放入后台的工作，也是工作恢复时，默认恢复的工作，“-”号代表倒数第二个放入后台的工作
```

#### 将后台暂停的工作恢复到前台执行

```shell
fg %工作号
参数：
	%工作号：%号可以省略，但是注意工作号和PID的区别
```

#### 把后台暂停的工作恢复到后台执行

```shell
bg %工作号
# 后台恢复执行的命令，是不能和前台有交互的，否则不能恢复到后台执行
```

#### 后台命令脱离登录终端执行的方法

- 把需要后台执行的命令加入/etc/rc.local文件
- 使用系统定时任务，让系统在执行的时间执行某个后台命令
- 使用nohup命令

```shell
nohup 命令 &
# 脱离终端执行
```

### 系统资源查看

#### vmstat命令监控系统资源

```shell
vmstat [刷新延时 刷新次数]
例如：
	vmstat 1 3
	
详细解释：
procs	进程信息字段
	r	等待运行的进程数，数量越大，系统越繁忙
	b	不可被唤醒的进程数量，数量越大，系统越繁忙
memory	内存信息字段
	swpd	虚拟内存的使用情况，单位kb
    free	空闲的内存容量，单位kb
    buff	缓冲的内存容量，单位kb
    cache	缓存的内存容量，单位kb
    
    缓冲与缓存的区别
    缓存（cache）是用来加速数据从硬盘中“读取”的，而缓冲（buffer）是用来加速数据“写入”硬盘的
swap	交换分区的信息字段
	si	从磁盘中交换到内存中数据的数量，单位kb
	so	从内存中交换到磁盘中数据的数量，单位kb，此两个数越大，证明数据需要经常在磁盘和内存之间交换，系统性能越差
io	磁盘读写信息字段
	bi	从块设备读入数据的总量，单位块
	bo	写到块设备的数据的总量，单位是块，此两个数越大，代表系统的I/O越繁忙
system	系统信息字段
	in	每秒被中断的进程次数
	cs	每秒钟进行的事件切换次数，此两个数越大，代表系统与接口设备的通信非常繁忙
CPU	CPU信息字段
	us	非内核进程消耗CPU运算时间的百分比
	sy	内核进程消耗CPU运算时间的百分比
	id	空闲CPU的百分比
	wa	等待I/O所消耗的CPU百分比
	st	被虚笔记所盗用的CPU占比
```

#### dmesg开机时内核检测信息

```shell
dmesg | grep CPUs
```

#### free命令查看内存使用状态

```shell
free [-b|-k|-m|-g]
选项：
	-b	以字节为单位显示
	-k	以kb为单位显示，默认就是KB为单位显示
	-m	以MB为单位显示
	-g	以GB为单位显示
```

#### 查看CPU信息

```shell
cat /proc/cpuinfo
```

#### uptime命令

显示系统的启动时间和平均负载，也就是top命令的第一行，w命令也可以看到这个数据

#### 查看系统与内核相关信息

```shell
uname [选项]
选项：
	-a	查看系统所有相关信息
	-r	查看内核版本
	-s	查看内核名称
```

#### 判断当前系统的位数

file /bin/ls

#### 查看当前Linux系统的发行版本

```shell
lsb_release -a
```

#### 列出进程打开或使用的文件信息

```shell
lsof [选项]
# 列出进程调用或打开文件的信息
选项：
	-c字符串	只列出以字符串开头的进程打开的文件
	-u用户名	只列出某个用户的进程打开的文件
	-p PID	  列出某个PID进程打开的文件
	
lsof | more
# 查询系统中所有进程调用的文件

lsof /sbin/init
# 查看某个文件被那个进程调用

lsof -c httpd
# 查看httpd进程调用了那些文件

lsof -u root
# 按照用户名，查询某用户的进程调用的文件名
```

### 系统定时任务

#### at一次性定时任务

```shell
chkconfig --list | grep atd
# at服务是否安装

service atd restart /systemctl start atd
# at服务启动（centos6）
```

##### at的访问控制

- 如果系统中有/etc/at.allow文件，那么只有写入/etc/at.allow(白名单)中的用户可以使用at命名（/etc/at.deny文件会被忽略)
- 如果系统中没有/etc/at.allow文件，只有/etc/at.deny，那么写入/etc/at.deny（黑名单）中的用户不能使用at命令，对root不起作用
- 如果命令中这两个文件都不存在，那么只有root用户可以使用at命令

##### at命令

```shell
at [选项] 时间
选项：
	-m	当at工作完成后，无论是否命令有输出，都用email通知执行at命令的用户
	-c	工作号，显示at工作的实际内容
时间： 
	HH:MM    04:00
	HH:MM YYYY-MM-DD	04:00 2017-03-17
	HH:MM[am|pm] [Month] [Date]		04pm March 17
	HH:MM[am|pm] + number [minutes|hours|days|weeks]	now + 5 minutes

例子：
	at now +2 minutes
	# 在两分钟之后执行hello.sh
	at> /root/hello.sh >> /root/hello.log
例子2：
	at 02：00 2018-05-28
	# 在指定时间重启
	at> /bin/sync
	at> /sbin/shutdown -r now
	
atq
# 查询当前服务器上的at工作

atrm [工作号]
# 删除指定的at任务
```

#### crontab循环定时任务

##### crontab服务管理与访问

```shell
systemctl restart crond.service
# 启动
systemctl enable crond.service
# 激活
```

##### 访问控制

- 当系统中有/etc/cron.allow文件时，只有写入此文件的用户可以使用crontab命令，没有写入的用户不能使用crontab命令。同样如果此文件，/etc/cron.deny文件会被忽略，/etc/cron.allow文件的优先级更高
- 当系统中只有/etc/cron/deny文件时，则写入此文件的用户不能使用crontab命令，没有写入文件的用户可以使用crontab命令

##### 用户的crontab设置

```shell
crontab [选项]
选项：
	-e	编辑crontab定时任务
	-l	查询crontab任务
	-r	删除当前用户所有的crontab任务
例子：
	crontab -e
	# 进入crontab编辑页面，会打开vim编辑你的工作
	* * * * * * 执行任务
	分时日月星
```

#### 系统的crontab设置

- “crontab -e”是每个用户执行的命令，也就是说不通的用户身份可以执行自己的定时任务，可是有些定时任务需要系统执行，这时我们就需要编辑/etc/crontab这个配置文件

##### 执行系统的定时任务的方法

- 手工执行定时任务
- 系统定时任务
	- 第一种把需要定时的脚本复制到/etc/cron.{daily,weekly,monthly}目录中的任意一个
	- 第二种修改/etc/crintab配置文件

#### anacron配置

- anacron是用来保证在系统开始的时候错过的定时任务，可以在系统开机之后再执行

##### anacron检测周期

- anacron会使用一天，七天，一个月作为检测周期
- 在系统的/var/spool/anacron/目录中存在cron.{daily,weekly,minthly}文件，用于记录上次执行cron的时间
- 和当前时间做比较，如果两个时间的差超过anacron的值定时间差值，证明有cron任务被执行

```shell
vi /etc/anacrontab  
RANDOM_DELAY=45
# 最大随机延迟
START_HOURS_RANGE=3-22
#anacron的执行范围是3-22点
1	5	cron.daily		nice run-parts /etc/cron.daily
7	25	cron.weekly		nice run-parts /etc/cron.weekly
@monthly 45	cron.monthly		nice run-parts /etc/cron.monthly
# 天数 强制延迟（分） 工作名称 实际执行的命令
```

