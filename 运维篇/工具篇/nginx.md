## 安装

依赖库

```shell
yum -y install autoconf automake make
yum -y install gcc gcc-c++

```

```shell
# 第一步：下载并解压
wget  http://nginx.org/download/nginx-1.9.15.tar.gz
tar -zxvf nginx-1.9.15.tar.gz
```



```shell
sudo ./configure --prefix=/usr/local/software/nginx --with-http_stub_status_module --with-http_ssl_module --add-module=/opt/echo-nginx-module-0.61
sudo make && sudo make install

```

### nginx的location的匹配方式

```shell
1. = ^~ ~ 普通文本四个优先级较高的先匹配，
2.同优先级的，匹配程度较高的先匹配
3.匹配程度也一样的，则写在前面的先匹配
```

反向代理

```shell
proxy_pass 1.1.1.1:33
```

负载均衡

```shell
upstream greoup{
    server 1.1.1.1 weight=1;
    server 2.3.3.3;
}
 weight = 1设置权重



```











