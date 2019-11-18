### 软件包管理

#### 软件包的分类

- 源码包
- 二进制包

##### 源码包的优点

- 开源，如果有足够能力，可以修改源代码
- 可以自由选择所需的功能
- 软件是编译安装，所有更加适合自己的系统，更加稳定也效率更高
- 卸载方便

##### 源码包的缺点

- 安装麻烦，尤其是一些比较大的集合软件
- 编译过程时间比较长，安装比二进制安装时间长
- 因为是编译安装，一旦出错会很麻烦

##### 二进制包的优点

- 包管理系统简单，只通过几个命令就可以实现包的安装，升级，查询和卸载
- 安装速度比源码包要快

##### 二进制的缺点

- 经过编译，不能看到源代码了
- 功能选择不如源码包灵活
- 依赖性

### rpm命令管理

#### RPM包命名规则

```shell
httpd-2.2.15-15.el6.centos.1.i686.rpm
	- httpd		软件包名
	- 2.2.15	软件版本
	- 15		软件发布的次数
	- el6.centos 适合的linux的平台
    - i686		适合的硬件平台
    - rpm		rpm包的扩展名
```

##### RPM包的依赖性

- 树形依赖：a -> b -> c
- 环形依赖：a - > b -> c -> a
- 模块依赖：查询网站：www.rpmfind.net

#### 安装命令

#####  包全名与包名

- 包全名：操作的包是没有按照的软件包时，使用包全名，而且要注意路径
- 包名：操作已经安装的软件包时，使用包名是搜索/var/lib/rpm 中的数据库

##### RPM安装

```shell
rpm -ivh 包全名
选项：
	-i			安装
	-v			显示详细信息
	-h			显示进度
	--nodeps	不检测依赖性
```

#### 升级和卸载

##### RPM包升级

```shell
rpm -Uvh 包全名
选项：
	-U	升级
```

##### RPM包卸载

```shell
rpm -e 包名
选项：
	-e			卸载
	--nodeps	不检查依赖性
```

#### RPM包查询

##### 查询是否安装

```shell
rpm -q 包名
# 查询是否安装
-q	查询

rpm -qa
# 查询所有安装的rpm包
```

##### 查询软件包的详细信息

```shell
rpm -qi 包名
选项：
	-i	查询软件信息
	-p	查询未安装包信息
```

##### 查询包中文件安装位置

```shell
rpm -ql 包名
选项：
	-l	列表
	-p	查询未安装包信息
```

##### RPM包默认安装位置

| 地址            | 详细                       |
| --------------- | -------------------------- |
| /etc/           | 配置文件安装目录           |
| /usr/bin/       | 可执行的命令安装目录       |
| /usr/lib/       | 程序所使用的函数库保存位置 |
| /usr/share/doc/ | 基本的软件使用手册保存位置 |
| /usr/share/man/ | 帮助文件保存位置           |

#### 查询系统文件属于哪个rpm包

```shell
rpm -qf 系统文件名
选项：
	-f	查询系统文件属于哪个软件包
```

#### 查询软件包的依赖性

```shell
rpm -qR 包名
选项：
	-R	查询软件包的依赖性
	-p	查询未安装包的信息
```

#### RPM包校验

```shell
rpm -V 已安装的包名
选项：
	-V	校验指定RPM包的文件
	
验证内容中的8个信息的具体内容
	s	文件大小是否改变
	M	文件的类型或文件权限（rwx）是否被改变
	5	文件MD5校验是否改变（可以看成文件内容是否被改变）
	D	设备的主从代码是否改变
	L	文件路径是否改变
	U	文件的属主（所有者）是否改变
	G	文件的属组是否改变
	T	文件的修改实际是否改变

文件类型
	c	配置文件
	d	普通文件
	g	“鬼”文件，就是该文件不应该被这个RPM所包含的
	L	授权文件
	r	描述文件
```

##### RPM包中的文件提取

```shell
rpm2cpio 包全名 | cpio -idv .文件绝对路径

rpm2cpio
# 将rpm包转换为cpio格式的命令

cpio 
# 是一个标准工具，他用于创建软件档案文件和从档案文件中提取文件

cpio 选项 < [文件|设备]
选项：
	-i	copy-in模式，还原
	-d	还原时自动新建目录
	-v	显示还原过程
```

### yum在线安装

#### yum源文件

```shell
vim /etc/yum.repos.d/CentOS-Base.repo 

[base]		容器说明，一定要放在[]中
name 		容器说明，可以自己随便写
mirrorlist	镜像站点，这个可以注释
baseurl		yum源服务器的地址，可以自己更改自己喜欢的yum源
enabled		此容器是否生效，1代表生效，0代表不生效
gpgcheck	如果是1是指RPM数字保证书生效，如果是0则是不生效
gpgkey		数字保证书的公钥文件保存位置，不用修改
failovermethod=priority
```

#### 光盘搭建yum源

```shell
1.挂载光盘
mkdir /mnt/cdrom
# 建立挂载点

mount /dev/cdrom /mnt/cdrom/
# 挂载光盘

2.使网络yum源失效
cd /etc/yum.repos.d/
# 进入yum源目录
mv CentOS-Base.repo CentOS-Base.repo.bak
# 修改yum源文件后缀名，使其失效

3.使光盘yum源生效
vim CentOS-Media.repo
# 修改位置为光盘挂载位置
```

#### yum命令

##### 常用yum命令

```shell
查询
yum list
# 查询所有可用软件包列表

yum search 关键字
# 搜索服务器上所有和关键字相关的包

安装
yum -y install 包名
选项：
	install	安装
	-y		自动回答yes
	
升级
yum -y update 包名
选项：
	update	升级
	
卸载
yum -y remove 包名
选项：
	remove	卸载
```

##### yum软件组管理命令

```shell
yum grouplist
# 列出所有可用的软件组列表

yum grouplist 软件组名
# 安装指定软件组，组名可用由grouplist查询出来

yum groupremove 软件组名
# 卸载指定软件组
```

### 源码包安装

#### 源码包和RPM包的区别

##### 区别：

- 安装之前的区别：概念上的区别
- 安装之后的区别：安装位置的不同

##### 安装位置不同带来的影响

RPM包安装的服务可以使用系统服务管理命令（service）来管理，例如RPM包安装的apache的启动方法

- /etc/rc.d/init.d/httpd start
- service httpd start

##### 源码包安装位置

安装在指定位置，一般是

- /usr/local/软件名/

#### 源码包安装过程

```shell
1.安装准备
	安装gcc
	下载源码包
2.安装注意事项
	源码包保存位置：/usr/local/src
	软件安装位置：/usr/local
	如何确定安装过程报错
		安装过程停止
		并出现error，warning或no提示
3.源码包安装过程
	下载源码包
	解压下载好的源码包
	进入解压目录
	./configure	软件配置与检查
		定义需要功能的选项
		检测系统环境是否符合安装需求
		把定义好的功能选项和检测系统环境的信息都写入Makefile文件，用于后续编辑
		--prefix=指定安装的位置
4.make编译
	make clean	清除编译好的文件
	make install 编译安装

卸载：直接删除安装目录即可
```

### 脚本安装

```shell
网址： lnmp.org
所谓的一键安装包，实际上还是安装的源码包与RPM包，知识把安装过程写成了脚本，便于初学者安装
优点：
	简单，快捷，方便
缺点：
	不能定义安装软件的版本
	不能定义所需要的软件功能
	源码包的优势丧失
	
关闭SElinux和防火墙
vim /etc/selinux/config  把enforcing改为disabled

```



















