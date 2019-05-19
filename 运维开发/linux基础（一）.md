---
title: linux基础（一）
date: 2019-02-07 18:00:44
tags: [linux]
categories: [linux]
---

### Linux安装

#### 虚拟机的安装

[Vmware官网](http://vmware.com)

#### 虚拟机的使用



#### 系统分区

#### linux系统安装

centos6的文件系统类型是ext4

linux安装时至少划分根分区 / 和SWAP分区

setup工具配置IP地址

### linux的常用命令

#### 命令基础格式

```shel
[root@root ~]# 
其中：
	root（1）： 当前登录用户
	root（2）：主机名
	~ 		：当前所在目录（~ 表示家目录）
	#		：超级用户提示符
	$		:普通用户的提示符	
```

```shell
命令 [选项] [参数]
注意：个别命令使用不遵循此格式
	当有多个选项的时候，可以写在一起
	简化选项和完整选项
		-a 等于 --al
```

查询目录中的内容： ls

```shell
ls 【选项】 【文件或目录】
选项：
	-a 显示所有文件，包括隐藏文件
	-l 显示详细信息
	-d 查看目录属性
	-h 人性化显示文件大小
	-i 显示inode
-rw-r--r-- 1 root root     332 Feb  6 19:26 main.go
	- 文件类型（-文件 d 目录 |软链接文件）
		rw-			r--		r--
		u所有者	  g所属组	o其他人
	r读  w写 x执行
	root 		属主
	root 		属组
	332  		文件大小
	Feb  6 19:26 最后一次更改的时间
	main.go  	文件名称
```

#### 文件处理命令

##### 目录处理命令

建立目录： mkdir

```shell
mkdir -p [目录名]
	-p 递归创建
	命令英文原意： make directories
```

切换所在目录： cd

```shell
切换所在目录： cd
	命令英文原意： change directory
简化操作
	cd ~	进入当前用户的家目录
	cd		和cd ~一样
	cd -	进入上一次目录
	cd ..	进入上一级目录
	cd .	进入当前目录
	
相对路径和绝对路径
	相对路径：参照当前所在目录，进行查找
	绝对路径：从根目录开始指定，一级一级递归查找，在任何目录下都能进入指定位置
```

查询所在目录位置： pwd

```shell
pwd
命令英文原意：print working directory
```

删除空目录：rmdir

```shell
rmdir [目录名]
命令英文原意：remove empty directories
```

##### 文件处理命令

删除文件或目录：rm

```shell
rm -rf [文件或目录]
	命令英文原意：remove
选项：
	-r 删除目录
	-f 强制
```

复制命令：cp

```shell
cp [选项] [原文件或目录] [目标目录]
命令英文原意：copy
选项：
	-r	复制目录
	-p	连带文件属性复制
	-d	若源文件是链接文件，则复制链接属性
	-a	相当于 -pdr
```

剪切或改名命令：mv

```shell
mv [原文件或目录] [目标目录]
命令英文原意：move
```

常用的目录

- / 根目录
- /bin 命令保存目录(普通用户可以读取命令)
- /boot 启动目录，启动相关文件
- /dev 设备文件保存目录
- /etc 配置文件保存目录
- /home 普通用户的家目录
- /lib 系统库保存目录
- /mnt 系统挂载目录
- /media 挂载目录
- / root 超级用户的家目录
- /tmp 临时目录
- /sbin 命令保存目录（超级用户才能使用的目录）
- /proc 直接写入内存的
- /sys
- /user 系统软件资源目录
	- /user/bin/系统命令 （普通用户）
	- /user/sbin/系统命令 （超级用户）
- /var 系统相关文档内容

##### 链接命令

链接命令：ln

```shell
ln -s [原文件] [目标文件]
命令英文原意：link
功能描述：生成链接文件
	选项： -s 创建软连接
硬链接的特征：
	1.拥有相同的i节点和存储block块，可以看做同一个文件
	2.可通过i节点识别
	3.不能跨分区
	4.不能针对目录使用
软连接特征
	1.类似windows快捷方式
	2.软链接拥有自己的i节点和block块，但数据块只保存原文件的文件名和i节点，并没有实际的文件数据
	3.lrwxrwxrwx l软连接，软连接的文件权限都是lrwxrwxrwx
	4.修改任意文件，另一个都改变
	5.删除原文件，软连接不能使用
```

#### 文件搜索命令

##### locate命令格式

```shell
locate 文件名
在后台数据库中按文件名搜索，搜索速度更快

./var/lib/mlocate
# locate命令所搜索的后台数据库

updatedb
更新数据库

updatedb的配置文件/etc/updatedb.conf
cat /etc/updatedb.conf 
	PRUNE_BIND_MOUNTS = "yes"
	PRUNEFS = "9p afs anon_inodefs auto autofs bdev binfmt_misc cgroup cifs coda configfs cpuset debugfs devpts ecryptfs exofs fuse fuse.sshfs fusectl gfs gfs2 gpfs hugetlbfs inotifyfs iso9660 jffs2 lustre mqueue ncpfs nfs nfs4 nfsd pipefs proc ramfs rootfs rpc_pipefs securityfs selinuxfs sfs sockfs sysfs tmpfs ubifs udf usbfs fuse.glusterfs ceph fuse.ceph"
	PRUNENAMES = ".git .hg .svn"
	PRUNEPATHS = "/afs /media /mnt /net /sfs /tmp /udev /var/cache/ccache /var/lib/yum/yumdb /var/spool/cups /var/spool/squid /var/tmp /var/lib/ceph"
	
第一行PRUNE_BIND_MOUNTS="yes"的意思是：是否进行限制搜索。

第二行是排除检索的文件系统类型，即列出的文件系统类型不进行检索。

第三行表示对哪些后缀的文件排除检索，也就是列在这里面的后缀的文件跳过不进行检索。不同后缀之间用空格隔开。

第四行是排除检索的路径，即列出的路径下的文件和子文件夹均跳过不进行检索。updatedb之后使用locate仍然找不到想要文件可以检查挂载的目录是否被忽略了


```

##### 命令搜索命令whereis与which

```shell
whereis 命令名
	# 搜索命令所在路径及帮助文档所在位置
选项：
	-a：	查看所有的选项
	-b：	只查找可执行文件
	-m：	只查找帮助文件
which 命令名

$PATH :系统环境

```

##### 文件搜索命令find

```shell
find [搜索范围] [搜索条件]
# 搜索文件

find / -name main.go
# 避免大范围搜索，会非常耗费系统资源
# find是在系统当中搜索符合条件的文件名，如果需要匹配，使用通配符匹配，通配符是完全匹配

linux的通配符
*	匹配任意内容
？	匹配任意一个字符
[]	匹配任意一个括号内的字符

find /root -iname main.go
# 不区分大小写

find /root -user root
# 按照所有者搜索

find /root -nouser
# 查找没有所有者的文件

find /var/log/ -mtime +10
# 查找10天前修改的文件

-10	10天内修改的文件
10	10天当天修改的文件
+10	10天前修改的文件

atime	文件访问时间
ctime	改变文件属性
mtime	修改文件内容

find . -size 25k
# 查找当前目录大小是25kb的文件

-25k	小于25kb的文件
25k		等于25kb的文件
+25k	大于25kb的文件

find . inum 262422
# 查找i节点是262422的文件

find /etc -size +20k -a -size -50k
# 查找/etc目录下，大于20kb并且小于50kb的文件
-a and 逻辑与，两个条件都满足
-o or  逻辑或，两个条件满足一个即可

find /etc -size +20k -a -size -50k -exec ls -lh {}\;
# 查找/etc目录下，大于20kb并且小于50kb的文件，并显示详细信息
# -exec/-ok 命令 {}\; 对搜索结果执行操作
```

##### 字符串搜索命令grep

```shell
grep [选项] 字符串 文件名
# 在文件当中匹配符合条件的字符串
选项：
	-i 忽略大小写
	-v 取反

find命令和grep命令的区别
find命令：在系统当中搜索符合条件的文件名，如果匹配，使用通配符，通配符是完全匹配
grep命令：在文件中搜索符合条件的字符串，如果需要匹配，使用正则进行匹配，正则表达式包含匹配
```

#### 帮助命令

##### 帮助命令man

```shell
man 命令
# 获取指定命令帮助

man ls
# 查看ls的帮助

man的级别
1：	查看命令的帮助
2：	查看可被内核调用的函数的帮助
3：	查看函数和函数库的帮助
4：	查看特殊文件的帮助（主要是/dev目录下的文件）
5：	查看配置文件的帮助
6：	查看游戏的帮助
7：	查看其它杂项的帮助
8：	查看系统管理员可用命令的帮助
9：	查看内核相关的帮助

man f 命令 == whatis 命令
# 查看命令有几个级别

man -1 passwd
# 查看passwd命令帮助

apropos 命令
# 查看所有包含该命令帮助
```

##### 其他帮助命令

```shell
命令 --help
# 获取命令选项的帮助

例如：
	ls --help

help shell内部命令
# 获取shell 内部命令的帮助

例如
	whereis cd
	# 确定是否是shell内部命令
	help cd
	# 获取内部命令的帮助

info 命令
 -回车：	进入子帮助页面（带有*号标记）
 -u：	  进入上一层页面
 -n：	  进入下一层帮助小节
 -p：	  进入上一个帮助小节
 -q：	  退出
```

#### 压缩与解压缩命令

常用压缩格式：.zip .gz .bz2 .tar.gz .tar.bz2

##### .zip压缩格式

```shell
zip 压缩文件名 原文件
# 压缩文件

zip -r 压缩文件名 源目录
# 压缩目录

unzip 压缩文件
# 解压缩 .zip文件

```

##### .gz格式压缩

```shell
gzip 原文件
# 压缩为.gz格式的压缩文件，源文件会消失

gzip -c 源文件 > 压缩文件
# 压缩为.gz格式，源文件保留
# 例如 gzip -c cangls > cangls.gz

gzip -r 目录
# 压缩目录下所有的子文件，但是不能压缩目录

gzip -d 压缩文件
# 解压缩文件

gunzip 压缩文件
# 解压缩文件
```

##### .bz2格式压缩

```shell
bzip2 源文件
# 压缩为.bz2格式，不保留源文件

bzip2 -k 源文件
# 压缩之后保留源文件

### bzip2命令不能压缩目录

bzip2 -d 压缩文件
# 解压缩 -k保留压缩文件

bunzip2 压缩文件
# 解压缩 -k保留压缩文件
```

##### 打包命令tar

```shell
# 压缩
tar -cvf 打包文件名 源文件
选项：
	-c	打包
	-v	显示过程
	-f	指定打包后的文件名
例如： 
	tar -cvf login.tar login

# 解压
tar -xvf 打包文件名
选项：
	-x	解打包
例如：
	tar -xvf login.tar
```

##### .tar.gz压缩格式

```shell
压缩
tar -zcvf 压缩包名.tar.gz 源文件
选项：
	-z	压缩为.tar.gz格式
tar -zxvf 压缩包名.tar.gz
选项：
	-x	解压缩.tar.gz格式
```

##### .tar.bz2压缩格式

```shell
压缩
tar -jcvf 压缩包名.tar.bz2 源文件
选项：
	-j	压缩为.tar.bz2格式
	
tar -jcvf  /tmp/压缩包名.tar.bz2 源文件
# 压缩到指定目录下

解压缩
tar -jxvf 压缩包名.tar.bz2
选项：
	-x	解压缩.tar.bz2格式
	-t	测试一下，压缩包中有什么

tar -jxvf 压缩包名.tar.bz2 -C /tmp/...
# 指定解压缩位置
```

#### 关机和重启命令

##### shutdown命令

```shell
# 关机命令
shutdown [选项] 时间
选项：
	-c	取消前一个关机命令
	-h	关机
	-r	重启
halt
poweroff
init 0

# 重启命令
reboot
init 6

# 查看当前系统运行级别
runlevel
# N：代表在进入3之前的级别	3：代表多用户

# 修改系统默认运行级别
cat /etc/inittab

# 退出登录
logout
```

##### 系统运行级别

| 0    | 关机                      |
| ---- | ------------------------- |
| 1    | 单用户                    |
| 2    | 不完全多用户，不含NFS服务 |
| 3    | 完全多用户                |
| 4    | 未分配                    |
| 5    | 图形界面                  |
| 6    | 重启                      |

#### 其他常用命令

##### 挂载命令

```shell
1.查询与自动挂载
mount
# 查询系统中已经挂载的设备

mount -a
# 依据配置文件/etc/fstab内容自动挂载

2.挂载命令格式
mount [-t 文件系统] [-o 特殊选项] 设备文件名 挂载点
选项：
	-t 文件系统：加入文件系统类型来指定挂载类型，可以ext3，ext4，iso9660等文件系统
	-o 特殊选项：可以指定挂载的额外选项
	
3.挂载光盘
mkdir /mnt/cdrom/
# 建立挂载点

mount -t iso9660 /dev/cdrom  /mnt/cdrom/
# 挂载光盘

mount /dev/sr0  /mnt/cdrom/
# 挂载光盘

4.卸载命令
umount 设备文件名或挂载点

umount /mnt/cdrom

5.挂载u盘
fdisk -l

# 查看U盘设备名称
mount -t vfat /dev/sdb1  /mnt/usb/

# 注意：Linux默认是不支持NTFS文件系统的
```

##### 用户登录查看

```shell
w 用户名
命令输出：
	USER	登录的用户名
	TTY		登录终端
	FROM	从哪个ip地址登录的
	LOGIN@	登录时间
	IDLE	用户闲置时间
	JCPU	指的是该终端连接的所有进程占用的时间，这个时间并不包括过去的后台作业时间，但却包括当前正在运行的后台作业所占用的时间
	PCPU	是指当前进程所占用的时间
	WGAT	当前正在运行的命令

who
命令输出
	用户名
	登录终端
	登录时间（登录来源ip地址）

last和lastlog
last命令默认读取/var/log/wtmp文件数据
命令输出
	用户名称
	登录终端
	登录ip
	登录时间
	退出时间（在线时间）
```


