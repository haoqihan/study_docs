---
title: docker的安装
date: 2019-01-13 18:17:20
tags: [docker]
categories: [运维开发之路]
---

### docker安装

#### 1.Ubuntu系统

Ubuntu安装docker大概要区分为Ubuntu14.04之前和Ubuntu14.04之后两种方法 

如果是14.04版本之后的Ubuntu,其内核版本以及一些依赖包都已经准备充分,直接运行下载最新版docker即可: 

```shell
 curl -sSL https://get.docker.com/ | sh 
```

新安装的系统可能会没有curl服务,需要下载: 

```shell
sudo apt-get update 
sudo apt-get install curl
```

顺便提及,docker应用的启动需要root的管理员权限,最好在安装之前获取root权限,啰嗦一下如何方便地将用户转为root角色 

```
sudo su
```

然后根据提示输入当前用户密码即可.

下载好之后可以测试,下载hello-world或者busybox测试一下.

```
sudo docker run hello-world
```

docker run是docker的运行命令.后面是容器名称,如果本地没有该命令,则docker服务会从docker仓库下载该容器,然后运行.　 

测试打印 hello world就说明成功了.可用docker info查看安装信息. 

最好使用新版本的Ubuntu安装docker.如果是12.04或者13.04版本的则需要先安装一些依赖性的包 

先要升级内核(同样先获取root权限) 

```
sudo apt-get update
sudo apt-get install linux-image-generic-lts-raring linux-headers-generic-lts-raring
```

　Docker有deb格式的安装包 

```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
```

后把Docker的库添加到apt的源列表中，更新并安装lxc-docker包。 

```
sudo sh -c "echo deb http://get.docker.io/ubuntu docker main\
> /etc/apt/sources.list.d/docker.list"
sudo apt-get update
sudo apt-get install lxc-docker
```

如果有警告信息,yes即可 

#### 2.centos系统和rhel

这两个系统在新的版本里面都自带了docker,只不过docker版本不一定是最新的,我记得centos7里面的自带的docker是0.9,当前最新docker版本已经到了0.11,不过不会影响试用. 

系统安装需要保证内核版本在3.10以上,低于这个版本的理论上也可以安装,只不过需要大牛去研究一番,我们直接升级内核 

yum安装带aufs模块的3.10内核 

```
cd /etc/yum.repos.d 
wget http://www.hop5.in/yum/el6/hop5.repo
yum install kernel-ml-aufs kernel-ml-aufs-devel
```

修改grub的主配置文件/etc/grub.conf，设置default=0，表示第一个title下的内容为默认启动的kernel（一般新安装的内核在第一个位置）,之后重启. 

执行安装: 

```
curl -sSL https://get.docker.com/ | sh 
```

启动服务:

```
sudo service docker start
```

如果是系统版本7以上,已经自带docker包,直接运行: 

```shell
yum install docker
```

#### 镜像加速

```shell
网址：https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors
```

