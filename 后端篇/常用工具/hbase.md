#### 进入 hbase

```shell
# 进入命令行
hbase shell
# 查看当前用户
whoami
```

#### 表管理

##### 查看所有表

```shell
# 查看有哪些表
list
```

##### 创建表

```shell
# 格式
create '表名','列名1', '列名2', '列名3'
# 例子
create 't1',"name1","name2","name3"
```

##### 删除表

```shell
# 格式，分两步：首先disable，然后drop
disable 表名
drop 表名
# 例子
disable 't1'
drop 't1'
```

##### 查看表结构

```shell
# 格式
describe <table>
# 例子
describe 't1'
```

#### 权限管理

##### 分配权限

```shell
# 语法
grant <user> <permissions> <table> <column family> <column qualifier> 参数后面用逗号分隔
# 权限用五个字母表示： "RWXCA".
# READ('R'), WRITE('W'), EXEC('X'), CREATE('C'), ADMIN('A')

# 例子，给用户‘test'分配对表t1有读写的权限，
grant 'test','RW','t1'
```

##### 查看权限

```shell
# 语法
user_permission <table>
# 例如 查看表t1的权限列表
 user_permission 't1';
```

##### 回收权限

```shell
# 语法
revoke <user> <table> <column family> <column qualifier>
# 例子： 收回test用户在表t1上的权限
 revoke 'test','t1'
```

##### 表数据的增删改查

##### 添加数据

```shell
# 语法

```









