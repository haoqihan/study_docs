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

