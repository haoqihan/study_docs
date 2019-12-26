一、下载python3源码包

```shell
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
```

二、下载python3编译的依赖包

```shell
yum install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel -y
```

三、解压

```shell
tar -xvf Python-3.6.5.tgz 
```

四、进入源码包

```shell
cd  Python-3.6.5
```

五、编译安装

```shell
# 创建编译目录
mkdir /usr/local/python3
# 指定编译目录
./configure --prefix=/usr/local/python3
# 编译安装
make
make install
```

六、建立软连接

```shell
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

