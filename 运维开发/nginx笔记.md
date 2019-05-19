---
title: nginx笔记
date: 2019-04-26 11:06:06
tags: [运维开发之路]
categories: [运维开发之路]
---

#### NGINX的三个主要应用场景

- 静态资源服务
  - 通过本地文件系统提供服务
- 反向代理服务
  - nginx的强大性能
  - 缓存
  - 负载均衡
- API服务

#### Nginx为什么会出现

- 互联网的数量快速增长
  - 互联网的快速普及
  - 全球网
  - 物联网
- 摩尔定律：性能提升
- 低效Apache
  - 一个链接对一个进程

#### nginx的优点

- 高并发，高性能
- 可扩展性好
- 高可靠性
- 热部署
- BDS许可证

#### nginx的组成

- Nginx二进制可执行文件
  - 由各模块源码编译的一个文件
- nginx.conf配置文件
  - 控制nginx的行为
- access.log访问日志
  - 记录每一条http请求信息
- error.log错误日志
  - 定位问题

#### nginx的安装

```shell
nginx地址：http://nginx.org/en/download.html
wget Stable version 下的nginx
# 下载nginx
wget http://nginx.org/download/nginx-1.16.0.tar.gz  
# 解压nginx
tar -xzf nginx-1.16.0.tar.gz  
# 进入nginx
cd nginx-1.16.0
# 指定编译目录
./configure  --prefix=/home/haoqihan/nginx
 --prefix=PATH        设置编译目录
 # 编译
 make
 # 安装
 make install
```

#### nginx的目录结构

```shell
# 让vim编辑的时候高亮显示
cp -r contrib/vim/* ~/.vim/

```

#### nginx常用配置语法

- 配置文件由指令和指令块构成
- 每条指令以；分号结尾，指令与参数间以空格符号分隔
- 指令块以{}大括号将多条指令组织在一起
- include语句允许组合多个配置文件以提升代码的可维护性
- 使用#符号添加注释，提高可读性
- 使用$符号使用变量
- 部分指令的参数支持正则表达式

#### 配置参数

| 时间单位   | time            |
| ---------- | --------------- |
| ms（毫秒） | milliseconds    |
| s（秒）    | seconds         |
| m（分钟）  | minutes         |
| h（小时）  | hours           |
| d（天）    | days            |
| w（周）    | weeks           |
| M（月）    | months，30 days |
| y（年）    | years 365days   |

| 空间单位 |           |
| -------- | --------- |
|          | bytes     |
| k、K     | kilobytes |
| m、M     | megabytes |
| g、G     | gigabytes |

#### http配置的指令块

- http
- server
- upstream
- location

#### Nginx命令行

1. 格式：nginx -s reload
2. 帮助 -？ -h
3. 使用指定的配置文件 -c
4. 指定配置指令 -g
5. 指定运行目录 -p
6. 发送信号 -s
   1. 立刻停止 stop
   2. 优雅的停止： quit
   3. 重载配置文件 reload
   4. 重新开始记录日志文件 reopen
7. 测试配置文件是否语法错误 -t -T
8. 打印nginx的版本信息，编译信息等 -v -V

#### 热部署

```shell
# 把二进制文件改名
cp nginx nginx.old
# 把编译好的二进制文件，进行替换
# 把旧进程kill掉
kill -USR2 pid
# 把老进程进行关闭
kill -WINCH pid
```

#### 日志切割

```shell
# 移动老日志
mv 老日志  old.log
# 重新生成日志
nginx -s reopen 
```

#### nginx搭建简单的web静态资源网站

```shell
# 开启gzip压缩
gzip  on;
# 字节数小于1的话就不进行压缩了
gzip_min_length 1;
# 压缩级别
gzip_comp_level 2;

server {
        listen       8080;
        server_name  localhost;

        #charset koi8-r;

        access_log  logs/host.access.log  main;

        location / {
	    # 设置index地址
	    alias  dlib/;
	    # 可直接访问文件
	    autoindex on;
	    # 现在访问速度为1k
	    set $limet_rate 1k;
        }

```

#### nginx反向代理

```shell
listen  127.0.0.1:8000 代表只能本机的800端口访问

# 配置上游服务
upstream local{
    server 127.0.0.1:8080
}

# 设置内存存储地址
proxy_cache_path /home/haoqihan/nginxcache levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m use_temp_path=off;


proxy_set_header Host $host;  
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

proxy_cache my_cache;

# 会把这些存储在内存中
proxy_cache_key $host$uri$is_args$args;

```

#### 用GoAccess实现可视化并实时监控access日志

```shell
下载： apt-get install goaccess
# 把日志生成一个html页面
goaccess access.log -o ../html/report.html --real-time-html --time-format='%H:%M:%S' --date-format='%d/%b/%Y' --log-format=COMBINED
```

#### ssl安全协议

#### 为nginx增加一个https证书

```shell
安装：sudo yum install certbot python2-certbot-nginx

```









