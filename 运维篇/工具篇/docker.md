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





#### 版本查看

```shell
# 版本查看
docker version

# 显示docker系统的信息
docker info
```

#### 镜像拉取

```shell
docker pull 镜像名称
```

#### 镜像查询

```shell
# 查看本地镜像
docker image ls

# 查看公共仓库镜像
docker search image_name

# 查看镜像历史
docker history  image_name
```

#### 镜像删除

```
sudo docker rmi 镜像名称
```

#### 容器运行

​           docker容器可以理解为在沙盒中运行的进程,这个沙盒包含该进程所必须的资源,包括文件系统,系统类库,shell环境等,但这个沙盒默认是不会运行任何程序的,你需要在沙盒中运行一个进程来启动某个容器,这个进程是该容器的唯一进程,所以当该进程结束时,容器也会结束

```shell
# 运行容器
docker run 容器名称

# 在容器中安装新的程序
docker run image_name apt-get install -y app_name

# 交互式进入容器中
docker run -i -t image_name /bin/bash
```

#### 端口映射

```shell
docker run nginx -p 主机端口：容器端口
```

#### 挂存储卷

```shell
docker run mysql -v 主机地址：容器地址     # 做地址映射
```

#### 进入容器

```shell
# 进入容器
sudo docker exec -it CONTAINER ID  /bin/bash
```

#### 查看容器日志

```shell
# 查看日志
sudo docker logs -f CONTAINER ID

# 保存对容器的修改  -a, --author="" Author; -m, --message="" Commit message 
docker commit ID new_image_name
```

#### 查询容器

```shell
 # 查看运行的docker容器
sudo docker ps   

 # 查看运行过的容器
sudo docker ps -a

# 列出最近一次启动的container
docker ps -1
```

#### 设置环境变量

```shell
sudo docker run  -e MYSQL_ALLOW_EMPTY_PASSWORD=123456 mysql  # -e 指定环境变量
```

#### 容器(停止,启动,杀死)

```shell
# 停止,启动,杀死一个容器
docker stop Name/ID
docker start Name/ID
docker kill Name/ID
```

#### 容器删除

```shell
# 删除所有容器
docker rm `docker ps -a -q`

# 删除单个容器
docker rm Name/ID
```

#### 镜像操作

```shell
# 列出一个容器里面被改变的文件或者目录,list列表会显示三种事件,A 增加 D删除 C被改变
docker diff Name/ID

# 显示一个运行的容器里面的进程信息
docker top Name/ID

# 从容器里面拷贝文件/目录到本地一个路径
docker cp Name:/container_path to_path 
docker cp ID:/container_path to_path 

# 重启一个正在运行的容器
docker restart Name/ID

# 附加到一个运行的容器上
docker attach ID
```

#### 保存和加载镜像

​        当需要把一台机器上的镜像迁移到另一台机器上的时候,需要保存于加载镜像

```shell
# 保存镜像到一个tar包  -o, --output="" Write to an file 
docker save image_name -o file_path

# 加载一个tar包格式的镜像 -i, --input="" Read from a tar archive file 
docker load -i file_path

# 机器a
docker save image_name > /home/save.tar

# 使用scp将save.tar拷到机器b上,然后
docker load < /home/save.tar
```

#### 仓库登录

```shell
# 登录register server -e, --email="" Email; -p, --password="" Password; -u, --username="" Username 
# 这里是阿里云的镜像仓库
sudo docker login --username=春秋羽123 registry.cn-beijing.aliyuncs.com
```

#### 镜像构建

```shell
sudo docker build -t 名称：版本   # 在当前文件找dockerfile
sudo docker build -t 名称：版本 -f /root/dockerfile      # -f 指定文件
```

#### 镜像打tag

```shell
sudo docker tag mysql:5.6（或ID） mycangku/mysql:1.0
```

#### 镜像推送

```shell
sudo docker push 镜像名称：id
```

#### Dockerfile的基本语法

```shell
FROM # 基础镜像
RUN  # 执行命令
ADD  #拷贝文件
WORKDIR # 设置工作目录
CMD  # 运行命令
EXPOSE  # 暴露的端口
```









#### 2.对image的操作(search,pull,images,rmi,history) view plaincopy

```shell
# 检索image
docker search image_name

# 下载image
docker pull image_name

# 列出镜像列表:-a, --all=false Show all images; --no-trunc=false Don't truncate output; -q, --quiet=false Only show numeric IDs 
docker images

# 删除一个或多个镜像  -f, --force=false Force; --no-prune=false Do not delete untagged parents 
docker rmi  image_name  

# 显示一个镜像的历史   --no-trunc=false Don't truncate output; -q, --quiet=false Only show numeric IDs 
docker history  image_name
```

#### 3.启动容器(run)

​	docker容器可以理解为在沙盒中运行的进程,这个沙盒包含该进程所必须的资源,包括文件系统,系统类库,shell环境等,但这个沙盒默认是不会运行任何程序的,你需要在沙盒中运行一个进程来启动某个容器,这个进程是该容器的唯一进程,所以当该进程结束时,容器也会结束

```shell
# 在容器中运行"echo" 命令,输出"hello word"
docker run image_name  echo "hello word"

# 交互式进入容器中
docker run -i -t image_name /bin/bash

# 在容器中安装新的程序
docker run image_name apt-get install -y app_name
```

​	 在执行apt-get 命令的时候，要带上-y参数。如果不指定-y参数的话，apt-get命令会进入交互模式，需要用户输入命令来进行确认，但在docker环境中是无法响应这种交互的。apt-get 命令执行完毕之后，容器就会停止，但对容器的改动不会丢失。 

#### 4.查看容器(ps) view plaincopy

```shell
# 列出当前所有运行的container
docker ps

# 列出所有的container
docker ps -a

# 列出最近一次启动的container
docker ps -1
```

#### 5.保存对容器的修改(commit)

​	当你对一个容器进行修改之后(通过容器中运行某一个命令),可以把容器的修改保存下来,这样下一次可以从保存后的最新状态运行该容器  view plaincopy

```shell
# 保存对容器的修改  -a, --author="" Author; -m, --message="" Commit message 
docker commit ID new_image_name
```

​	Note:image相当于一个类,container相当于实例，不过可以动态给实例安装新软件，然后把这个container用commit命令固化成一个image。 

#### 6.对容器的操作(rm、stop、start、kill、logs、diff、top、cp、restart、attach ) view plaincopy 

```shell
# 删除所有容器
docker rm `docker ps -a -q`

# 删除单个容器
docker rm Name/ID

# 停止,启动,杀死一个容器
docker stop Name/ID
docker start Name/ID
docker kill Name/ID

# 从一个容器中取日志
docker logs Name/ID

# 列出一个容器里面被改变的文件或者目录,list列表会显示三种事件,A 增加 D删除 C被改变
docker diff Name/ID

# 显示一个运行的容器里面的进程信息
docker top Name/ID

# 从容器里面拷贝文件/目录到本地一个路径
docker cp Name:/container_path to_path 
docker cp ID:/container_path to_path 

# 重启一个正在运行的容器
docker restart Name/ID

# 附加到一个运行的容器上
docker attach ID
```

​	Note:attach命令允许你查看或影响一个运行的容器,你可以在同一时间attach同一个容器,你也可以从一个容器中脱离出来,是CTRL + C

#### 7.保存和加载镜像(save load)

​	当需要把一台机器上的镜像迁移到另一台机器上的时候,需要保存于加载镜像

```shell
# 保存镜像到一个tar包  -o, --output="" Write to an file 
docker save image_name -o file_path

# 加载一个tar包格式的镜像 -i, --input="" Read from a tar archive file 
docker load -i file_path

# 机器a
docker save image_name > /home/save.tar

# 使用scp将save.tar拷到机器b上,然后
docker load < /home/save.tar
```

#### 8.登录 registry server (login)  view plaincopy

```shell
# 登录register server -e, --email="" Email; -p, --password="" Password; -u, --username="" Username 
docker login
```



