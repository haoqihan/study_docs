### shell操作hdfs

#### ls 查看当前目录信息

```shell
# 例子:查看根目录下所有文件（文件夹）信息
hadoop fs -ls /
```

#### mkdir 创建文件夹

```shell
# 例子
hadoop fs -mkdir /tmp/test 		# 在tmp目录下创建test目录
hadoop fs -mkdir -p /hello/world # 创建多级文件夹
```

#### put 上传文件

```shell
# 格式
hadoop fs -put /本地路径 /hdfs路径
# 例子
hadoop fs -put ~/install.log /tmp/test # 上传家目录的install.log 文件到/tmp/test
```

#### moveFromLocal  剪切文件

```shell
# 格式
hadoop fs  -moveFromLocal /本地文件 /hdfs路径
# 例子
hadoop fs -moveFromLocal  test.py  /tmp/test1 # 将本地test.py 文件剪切到/tmp/test1 目录下
```

#### get 下载文件到本地

```shell
# 格式
hadoop fs -get /hdfs路径 /本地路径
# 例子
hadoop fs -get /tmp/test.txt /root/
```

#### getmerge  合并下载

```shell
 # 格式
 hdfs dfs -getmerge /hdfs路径文件夹 /合并后的文件
 # 例子
 hdfs dfs -getmerge  /tmp/test1 test.txt # 把hadoop的text1下的所有文件合并到本地test.txt 文件
```

#### mv 移动文件

```shell
# 格式
hdfs dfs -mv /hdfs路径 /hdfs路径
# 例子
 hdfs dfs -mv /tmp/test /tmp/demo # 把test文件夹改为demo文件夹
```

#### rm 删除文件（文件夹）

```shell
# 格式 删除文件
hdfs dfs -rm /hdfs路径
# 格式 删除文件夹
hdfs dfs -rm -r  /hdfs路径

# 例子 删除文件
 hadoop fs -rm /tmp/test.txt # 删除test.txt 文件
 
 # 例子 删除文件夹
 hadoop fs -rm -r /tmp/demo  # 删除demo文件夹
```



#### touchz 创建文件

```shell
# 例子
hadoop fs -touchz  /tmp/test.txt # 在tmp目录下创建test.txt文件

```

####  查看HDFS中文件内容

```shell
# 格式
hadoop fs -cat /hdfs文件
# 例子
hadoop fs -cat  /tmp/test.txt # 查看test.txt文件信息

```

#### 文件夹的文件个数

```shell
# 格式
hdfs dfs -count /文件夹
# 例子
hdfs dfs -ls /tmp/test1 # 查看test1文件夹中文件的个数
```

#### 查看hdfs的总空间

```shell
# 格式
hdfs dfs -df -h / # 查看空间
```

#### chown 更改目录或文件权限

```shell
# 例子
hadoop fs -chmod 666 /tmp/test # 为test目录添加可读可写权限
```

#### cp 复制文件

```shell
# 格式
hdfs dfs -cp /hdfs路径 /hdfs路径
# 例子
hadoop fs -cp  /tmp/test/demo1.txt  /tmp/test1/ # 把/tmp/test 目录下的demo文件 拷贝到/tmp/test1目录下
```

#### du  显示文件大小

```shell
# 例子
hadoop fs -du /tmp/test/demo1.txt # 查看demo1.txt 文件的大小
```



