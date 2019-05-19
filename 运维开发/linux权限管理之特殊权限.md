---
title: linux权限管理之特殊权限
date: 2019-02-13 17:40:37
tags: [linux]
categories: [linux]
---

### ACL权限

#### ACL权限简介与开启

```shell
1.查看分区ACL权限是否开启
dumpe2fs -h /dev/vda1
# dumpe2fs命令式查询指定分区详细文件系统信息的命令
选项:
	-h	仅显示超级块中信息,而不显示磁盘块组的详细信息

2.临时开启分区ACL权限
mount -o remount,acl /

3.永久开启分区ACL权限
vim /etc/fstab 
UUID=eb448abb-3012-4d8d-bcde-94434d586a31 /                       ext4    defaults,acl    1 1
# 加入acl
mount -o remount /
# 重新挂载文件或重启系统,使修改生效
```

#### 查看与设定ACL权限

##### 查看ACL命令

```shell
getfacl 文件名
# 获取文件的ACL权限
```

##### 设定ACL权限的命令

```shell
setfacl 选项 文件名
选项:
	-m	设定ACL权限
	-x	删除指定ACL权限
	-b	删除所有的ACL权限
	-d	设定默认的ACL权限
	-k	删除默认ACL权限
	-R	递归设定ACL权限
例如:
	setfacl -m u:用户名:权限 文件夹
```

##### 给用户组设定ACL权限

```shell
setfacl -m g:组名:权限 文件夹
```
##### 给mask设定权限

```shell
setfacl -m m:权限 文件夹
# 设定mask权限
例子：
	setfacl -m m:rx 文件夹名
	# 设定mask权限为r-x，使用m：权限的格式
```

#### 最大有效权限与删除ACL权限

##### 最大有效权限mask

- mask是用来指最大有效权限的，如果我给用户赋予了ACL权限，是需要和mask相 “与” 才能得到用户的真正权限

##### 删除ACL权限

```shell
setfacl -x u:用户名 文件名
# 删除指定用户的ACL权限

setfacl -x g：组名 文件名
# 删除指定用户组ACL权限

setfacl -b 文件名
# 删除文件的所有的ACL权限
```

#### 默认ACL权限与递归ACL权限

##### 递归权限

- 递归是父目录在设定ACL权限时，所有的子文件和子目录也会拥有相同的ACL权限
- setfacl -m u：用户名：权限 -R 文件夹名

##### 默认权限

- 默认ACL权限的作用是如果给父目录设定了默认ACL权限，那么父目录中所有新建的子文件都会继承父目录的ACL权限

```shell
serfacl -m d:u:用户名：权限 文件夹名
```

### sudo权限

- root把本来只能超级用户执行超级用户执行的命令赋予普通用户执行
- sudo的操作对象是系统命令

#### sudo的使用

```shell
visudo
# 实际修改的是/etc/sudoers
root 	ALL=（ALL）  	ALL
# 用户名 被管理主机的地址 = （可使用的身份） 授权命令 （绝对路径）
# %where	ALL（ALL）	ALL
# %组名	被管理主机地址=（可使用的身份） 授权命令（绝对路径）
sudo -l
# 查看可用的sudo的命令
sudo /sbin/shoutdown -r now

例子1：
	# 普通用户执行sudo赋予的命令
	sudo + 命令
例子2：
	# 授权普通用户可以添加其他用户
	visudo
	user1 ALL=/user/sbin/useradd
	user1 ALL=/user/sbin/passwd
	# 授予用户设定密码权限
	注意：这个很危险，可以修改root密码
```

### 文件特殊权限

#### SetUID

##### 功能

- 只有可以执行的二进制程序才能设定SUID权限
- 命令执行者要对程序拥有x（执行）权限
- 命令执行者在执行该程序时获得该程序文件属主的身份（在执行程序的过程中灵魂附体为文件的属主）
- SetUID权限只在该程序执行的过程中有效，也就是说身份改变只在程序运行中有效

```shell
passwd命令拥有SetUID权限，所以普通用户可以修改自己的密码
-rwsr-xr-x. 1 root root 27832 Jun 10  2014 /usr/bin/passwd

cat命令没有SetUID权限，所以普通用户必能查看/etc/shadown文件内容
-rwxr-xr-x. 1 root root 54080 Nov  6  2016 /bin/cat
```

##### 设定SetUID的方法

```shell
4代表SUID
  chmod 4755 文件名
  chmod u+s 文件名
```

##### 危险的SetUID

- 关键目录应严格控制写权限，比如：/ ,"/usr"等
- 用户密码设置要严格遵守三原则
- 对系统中默认应该具有SetUID权限的文件作一列表，定时检查有没有这之外的文件被设置了SetUID权限

#### SetGID

##### 作用

- 只有可以执行的二进制程序才能设定SGID权限
- 命令执行者要对程序拥有x（执行）权限
- 命令执行者在执行该程序时，组身份升级为该程序文件的属组
- SetGID权限只在该程序执行的过程中有效，也就是说组身份改变只在程序执行过程中有效

```shell
ll /usr/bin/locate 
-rwx--s--x 1 root slocate 40520 Apr 11  2018 /usr/bin/locate
# 查看设置的SGID
```

- /usr/bin/locate 是可执行的二进制程序，可以赋予SGID
- 执行用户lamp对/usr/bin/locate 命令拥有执行权限
- 执行/usr/bin/locate 命令时候，组身份升级为slocate组，而slocate组对/var/lib/mlocate/mlocate.db数据库拥有r权限，所以普通用户可以使用locate命令查询mlocate.db数据库
- 命令结束，lamp用户的组身份回归为lamp组

##### SetGID针对目录的作用

- 普通用户必须对此目录拥有r和x权限，才能进入此目录
- 普通用户在此目录中的有效组会变成此目录的数组
- 若普通用户对此目录拥有w权限时，新建的文件的默认数组则是这个目录的属组

##### 设定SetUID的方法

```shell
2代表SUID
  chmod 2755 文件夹名
  chmod g+s 文件夹名
```

#### Sticky BIT

##### SBIT粘着位作用

- 粘着位目前只对目录有效
- 普通用户对于该目录拥有w和x权限，即普通用户可以在此目录有写入权限
- 如果没有粘着位，用为普通用户拥有w权限，所以可以删除此目录下的所有文件，包括其他用户建立的文件，一旦赋予了粘着位，除了root可以删除所有文件，普通用户就算有w权限，也只能删除自己建立的文件，但是不能删除其他用户建立的文件

##### 设置与取消粘着位

```shell
设置粘着位
	chmod 1755 目录名
	chmod o+t 目录名
取消粘着为
	chmod 0777 目录名
	chmod o-t 目录名
```

### 不可改变位权限（chattr权限）

#### chattr命令

```shell
chattr [+-=] [选项] 文件或目录名
	+	增加权限
	-	删除权限
	= 	等于某权限
选项：
	i	如果对文件设置i属性，那么不允许对文件进行删除，改名，也不能添加和修改数据；
		如果对目录设置值i属性，那么只能修改目录下文件的数据，但不允许建立和删除文件
	a	如果对文件设置a属性，那么只能在文件中增加数据，但不能删除也不能修改数据
		如果对目录设置值a属性，那么只允许在目录中建立和修改文件，但不允许删除
```

#### 查看文件系统属性

```shell
lsattr 选项 文件名
选项：
	a	显示所有文件和目录
	d	若目标是目录，仅列出目录本身属性，而不是子文件的
```



