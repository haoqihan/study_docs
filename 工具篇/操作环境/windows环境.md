## windows常用软件

### scoop

```shell
# 想要指定安装目录，在PowerShell中输入如下内容（代码中的D:\Applications\Scoop为指定的目录）：
[environment]::setEnvironmentVariable('SCOOP','D:\Applications\Scoop','User')
$env:SCOOP='D:\Applications\Scoop'
iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
```

### utools  工具集

```shell
地址：https://u.tools/download.html
```

###  快速搜索工具 - Everything

```shell
百度就有
```

### wox 快速启动工具

```shell
http://www.wox.one/
```

### 命令行工具 cmder

```shell
https://cmder.net/
```

### 卸载工具

```shell
http://www.downza.cn/soft/203267.html
```

###  Unix 工具集 - busybox

```shell
scoop install busybox
```

### carnac 按键回显工具

```shell
https://pan.baidu.com/s/1dryStT6uTNoUjKmYIR5FnQ  # 中文版  左键设置位置 右键退出
```

###   markdown编辑器

```shell
https://www.typora.io/
```

### 刻录工具 - Rufus

```
https://github.com/pbatard/rufus/releases
```

### 下载mysql和redis

```shell
scoop install mysql
# 设置后台服务
mysqld.exe --install MySql --defaults-file="d:/lovejava/mysql-5.6/my.ini"  
# d:/lovejava/mysql-5.6/my-default.ini 为你mysql安装的路径


scoop install redis

# 注释：scoop如果默认安装的话 scoop安装的目录就在 C:\Users\用户\scoop\apps
# 1，在redis的目录下执行（执行后就作为windows服务了）
redis-server --service-install redis.windows.conf

# 2，安装好后需要手动启动redis
redis-server --service-start

# 3，停止服务
redis-server --service-stop

# 4，卸载redis服务
redis-server --service-uninstall
```











