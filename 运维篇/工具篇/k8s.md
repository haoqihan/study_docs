实验地址

```http
https://www.katacoda.com/courses/kubernetes/playground
```

### master

- apiserver
  - kubectl
  - restapi
  - web ui
- ETCD
- 

### node

- kubelet
- kube-proxy:创建虚拟网卡
- docker

### pod

- 调度的最小单位
- pod可以使多个docker容器，但大多时候是一个应用容器+一个pause

### deployment

- 维持pod数量

### service

- 多个pod抽象为一个服务

### ingress

- 做http的映射的

```shell
# 查看详细信息
kubectl cluster-info

# 启动pod
kubectl run d3 --image httpd:alpine  --port 80

# 修改个数
kubectl edit deployment d3 # 修改spec下的replicas的个数

# 查看运行的pod
kubectl get deployments.

# 创建service
kubectl expose deployment d3 --target-port=80 --type=NodePort
# 查看service
kubectl get service

# 进入节点
kubectl exec -it d3-... sh



```

下载：

```shell
docker pull mysql:5.6

sudo docker run -p 3307:3306 --name mysql -v /home/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.6



镜像（image） 容器（container） 仓库（registry）

```

#### k8s的介绍

- 基于容器技术的分布式架构领先方案，他是google严格保密十几年的秘密武器，-Borg的一个开源方案
- Kubernetes是Google开源的一个容器编排引擎，它支持自动化部署，大规模可伸缩，应用容器化管理

#### k8s能做什么

- 容器的自动化复制和部署，随时扩展或收缩容器规模，并提供负载均衡
- 方便的容器升级
- 提供容器弹性，如果失效就替换它

#### k8s对于测试能做什么

- 测试服务器的集中化，自动化管理。将各种平台的服务器加入集群，按需部署或销毁
- 持续集成时方便地自动部署

#### k8s基本概念

- Master是主服务器，node是用于部署应用容器的服务器
- Pod基本操作单元，也是应用运行的载体，整个Kubernetes系统都是围绕着Pod展开的，比如如何部署运行Pod，如何保证Pod的数量，如何访问Pod等
- Deployment定义了Pod部署的信息
- 若干个Pod副本组成一个service，对外提供服务
- 副本是指一个Pod的多个实例
- Namespace用于多租户的资源隔离，在测试环境中可以根据namespace划分成多套测试环境。默认有2个Namespace：kube-system/default

#### K8s调度过程

- kubernetes Client将请求发送给API server
- API server根据请求的类型，将处理的结果存入高可用键值存储系统Etcd中
- Schedule将未分发的Pod绑定（bind）到可用的Node节点上，存到etcd中
- Controller Manager根据etcd中的信息，调用node的kubelet创建Pod
- Controller Manager监控Pod的运行状况并确保运行正常

#### k8s安装前的准备

- 准备科学上网，在主机上安装shadowsocks，并配好服务器（服务器地址、密码需要自己想办法）

#### k8s安装说明

- 2台主机都要安装docker
- 2台主机都要安装kubeadm、kubelet和kubectl
- 2台主机都要禁用虚拟内存（swapoff -a）

#### k8s安装以及配置

**安装kubeadm，kubelet和kubectl**

```shell
sudo apt-get update && sudo apt-get install -y apt-transport-https curl
```

**设置代理**

```shell
# linux设置代理
export http_proxy=0.0.0.1:1233 && export https_proxy=0.0.0.0:1233
```


