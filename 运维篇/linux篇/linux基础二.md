#### 磁盘管理

##### df    查看磁盘分区使用状况

```shell
选项：
	-l	仅显示本地磁盘（默认）
	-a	显示所有文件系统的磁盘使用情况，包含/proc/
	-h	以1024进制计算最适合的单位显示磁盘容量
	-H	以1000进制计算最适合的单位显示磁盘容量
	-T	显示磁盘分区类型
	-t	显示指定类型文件系统的磁盘分区
	-x	不显示指定类型文件系统的磁盘分区
```

##### du 	统计磁盘的文件大小

```shell
选项：
	-b	以byte为单位统计文件
	-k	以kb为单位统计文件
	-m	以MB为单位统计文件
	-h	按照1024进制以最适合的单位统计文件
	-H	按照1000进制以最适合的单位统计文件
	-s	指定统计目标
```

#### 分区的概念

- 第一 主分区和扩展分区总数不能超过4个
- 第二 扩展分区最多只能有一个
- 第三 扩展分区不能直接存取数据

```shell
分区：  fdisk来分区
```

##### 分区模式值MBR

- 主分区不超过4个
- 单个分区容量最大2TB

##### 分区模式之GPT

- 主分区的个数“几乎”没有限制
- 单个分区容量“几乎”没有限制

##### parted的使用

```shell
parted  #分区工具
选项：
	help				查看帮助信息
	mklabel	gpt			指定使用gpt来分区
	select /dev/sdc		 切换分区
	mkpart				添加分区
	cancel				取消操作
	print				查看目前分区情况
	rm 分区编号			 删除分区
	
mkpart	分区名称	起始位置	结束位置
# 使用命令分区
```

##### mkfs的使用

```shell
mkfs.ext3 /dev/sdb
# 把/dev/sdb 分区格式化为ext3文件系统格式

mkfs -t ext4 /dev/sdb2
# 把/dev/sdb2 分区格式化为ext4文件系统格式

# 只有主分区和逻辑分区可以格式化，其他分区不可以
```

#### 挂载分区

```shell
mount /dev/sdb /mnt/xxx
# 把/dev/sdb挂载到/mnt/xxx下

umount  /mnt/xxx
# 把挂载的分区卸载掉

vim + /etc/fstab
# 修改系统的挂载，可以自动挂载
```

#### swap交换分区

```shell
如何为硬盘添加swap交换分区
	- 第一，建立一个普通的linux分区
	- 第二，修改分区类型的16进制编码
	- 第三，格式化交换分区
	- 第四，启用交换分区
	
mkswap /dev/sdb  
# 格式化为swap交换分区
swapon /dev/sdb  
#  启动分区

swapoff /dev/sdb  
# 关闭分区
```

#### 用户和用户组

##### 用户和用户组信息存储位置

```shell
用户：使用操作系统的人
用户组：具有相同系统权限的一组用户
/etc/group 存储当前系统中所有用户组信息
	- Group：	x		：123	：abc，def，xxx
	- 组名：	组密码占位符：组编号：组中用户列表
/etc/gshadow 存储当前系统中用户组密码信息
	- group：	*：			   ：    abc，def，xxx
	- 组名：	组密码：	组管理者：	 组中用户名列表
/etc/passwd 存储当前系统中所有用户信息
	- user  ：	x	 ：123	 ：456		 ：xxxxx		：/home/user	 :/bin/bash
	- 用户名：密码占位符：用户编号：用户组编号  ：用户注释信息：用户主目录	：shell类型
/etc/shadow	存储当前系统中所有用户的密码信息
	- user：$6$h26yil8F$X3OPNjL....：：：：：
	- 用户名：密码（加密的）：：：：：
```
##### 用户组相关命令

```shell
groupadd 组名	添加用户组
# 创建用户组
选项：
	-f	如果组存在，则强制退出成功
	-g	指定组id
	-h	帮助信息
	-p	组密码
	-r	创建一个系统账户
	
groupmod 	修改用户组
选项：
	-n	修改名称
	-g	修改组id
	
groupmod -n market sexy 
# 修改组名 把sexy改为market

groupmod -g 668 market
# 修改组编号

groupdel	删除用户组
```

##### 用户相关命令

```shell
useradd	创建用户
选项：
	-g	后面加组名和用户名，就是把这个用户添加到这个组中
	-d	可以指定家目录
	-G	指定附属组

例子：
	 useradd -g 组名 用户名
	 useradd -d /home/xxxx 用户名
	 useradd -g 主组 -G 附属组1，附属组2  用户名

usermod	修改用户
选项：
	-c	修改用户备注信息
	-l	修改用户名称
	-d	修改家目录
	-g	修改用户的主用户组
例子：
	usermod -c 注释内容 用户名
	usermod -l 新用户名 旧用户名
	usermod -d 家目录 用户名
	
userdel	删除用户
选项:
	-r	删除用户时，连同用户家目录一块删除

touch /etc/nolog
# 除了root用户，其他用户都不能登录
```

##### 进阶命令

```shell
passwd -l	用户名
# 锁定用户

passwd -u	用户名
# 解锁用户

passwd -d	用户名
# 清空用户密码

gpasswd -a 用户名 用户组
# 给这个用户添加一个附属组

gpasswd -d 用户名 用户组
# 给这个用户删除一个附属组

gpasswd 组名
# 修改用户组密码


newgrp 组名
# 切换用户组

su 切换用户

whoami 
# 显示当前登录用户

id 用户名
# 显示指定用户信息，包括用户编号，用户名
# 主要组编号及名称，附属组列表

groups 用户名
# 显示用户所在的所有用户组

chfn 用户名
# 设置用户资料，依次输入用户资料

finger 用户名
# 显示用户详细信息
```

