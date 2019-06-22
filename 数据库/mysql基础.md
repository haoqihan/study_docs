### mysql数据库基本命令

#### **数据库的增删改查**

```sql
-- 增
create database  数据库名称;

-- 删
drop database 库名;

-- 改
alter database 库名  更改的内容;

-- 查
show create database 库名;查看当前创建的数据库
show databases; 查看所有的数据库
select database();查看所在的数据库
```

#### 表的增删改查

```sql
-- 增
create table 表名(字段名 类型 约束);

-- 删
drop table 表名;

-- 改
alter table 表名 modify 字段名 类型;
alter table 表名 add 字段名;

-- 查
show create table 表名;查看表的详细信息
show tables;查看这个数据库先所有的表
desc 表名;查看这个表里面所有的字段
```

#### 数据的增删改查

```sql
-- 增
insert into 表名(字段名) values (内容);

-- 删
delete from 表名;  清空数据,但是里面的id自增不会去除
truncate 表名; 删除所有的内容

-- 改
update 表名 set name="xxx" where 条件
update 表名 set 要修改的内容

-- 查
select 字段名 from 表名;
select 字段1,字段2 from 表名;
select * from 表名; 查看所有的内容
```

### mysql的数据类型

**数据类型:**定义列中可以存储什么数据以及该数据实际怎样存储的基本规则，其用于以下几个目的

- 允许限制可存储在列中的数据
- 允许在内部更有效的存储数据
- 允许变换排序顺序（作为数值数据类型，数值才能正确排序）

#### **一.字符串数据类型**

该类型为最常用的数据类型，用来存储串（比如名字、地址等）；有两种串类型，分别是定长串和变长串 

**定长串：**接受长度固定的字符串，其长度实在创建表时指定的；定长列不允许多余指定的字符数目，它们分配的存储空间与指定的一样多（比如char） 

**变长串：**存储可变长度的文本，有些变长数据类型具有最大定长，有些是完全变长的，不论哪种，指定的数据得到保存即可（灵活） 

| 数据类型   | 大小           | 用途                          |
| ---------- | -------------- | ----------------------------- |
| char       | 0-255字节      | 定长字符串                    |
| varchar    | 0-65535字节    | 变长字符串                    |
| tinyblog   | 0-255字节      | 不超过255个字符的二进制字符串 |
| tinytext   | 0-255字节      | 短文本字符串                  |
| blob       | 0-65535字节    | 二进制形式的长文本数据        |
| text       | 0-65535字节    | 长文本数据                    |
| mediumblob | 0-16777215字节 | 二进制形式的中等长度文本数据  |
| mediumtext | 0-16777215字节 | 中等长度文本数据              |

#### **二.数值类型**

| 类型         | 大小                                     | 范围(有符号)                                                 | 无符号                                                       | 用途            |
| ------------ | ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------- |
| tinyint      | 1字节                                    | (-128,127)                                                   | (0,255)                                                      | 小整数值        |
| smallint     | 2字节                                    | (-32768,32767)                                               | (0,35535)                                                    | 大整数值        |
| mediumint    | 3字节                                    | (-8 388 608，8 388 607)                                      | (0，16 777 215)                                              | 大整数值        |
| int或integer | 4字节                                    | (-2 147 483 648，2 147 483 647)                              | (0，4 294 967 295)                                           | 大整数值        |
| bigint       | 8 字节                                   | (-9 233 372 036 854 775 808，9 223 372 036 854 775 807)      | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| float        | 4字节                                    | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| double       | 8字节                                    | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| decimal      | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | 小数值          |

#### **三.日期和时间类型**

表示时间值的日期和时间类型为DATETIME、DATE、TIMESTAMP、TIME和YEAR。 

| 类型      | 大小(字节) | 范围                                                         | 格式                | 用途                     |
| --------- | ---------- | ------------------------------------------------------------ | ------------------- | ------------------------ |
| date      | 3          | 1000-01-01/9999-12-31                                        | YYYY-MM-DD          | 日期值                   |
| time      | 3          | -838:59:59'/'838:59:59'                                      | HH:MM:SS            | 时间值或持续时间         |
| year      | 1          | 1901/2155                                                    | YYYY                | 年份值                   |
| datetime  | 8          | 1000-01-01 00:00:00/9999-12-31 23:59:59                      | YYYY-MM-DD HH:MM:SS | 混合日期和时间值         |
| timestamp | 4          | 1970-01-01 00:00:00/2038结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYYMMDD HHMMSS     | 混合日期和时间值，时间戳 |

#### **四.枚举和集合**

- **enum** 单选只能在给定的范围内选一个值,如sex男和male女
- **set** 多选 在给定的范围内可以选择一个或一个以上的值(爱好1,爱好2)

### 完整性约束

| 类型              | 说明      |
| ----------------- | --------- |
| not  null         | 不能为空  |
| default           | 默认值    |
| unique            | 设置唯一  |
| primary key       | 主键      |
| auto_increment    | 自增      |
| foreign key       | 外键      |
| unsigned          | 无符号    |
| zerofill          | 使用0填充 |
| on delete cascade | 同步删除  |
| on update cascade | 同步更新  |

### 表查询

#### 单表查询

- **from**: 找表
- **where** :指定约束条件
	- 比较运算符:>,<,>=,<=,!=
	- **between** 80 and 100 :值在80到100之间
	-  **in**(80,90,100):值是80,90或100
	-  **like'xiaomage**':模糊查找也可以是%,或_:模糊查找
	- 逻辑运算符:**and or not**
- **group by**:分组 
- **having**:过滤
	- **执行优先级**:**where>group by >having**
	- 1.**where** 发生在分组 group by之前,因而where 中可以有任意字段,但绝对不能使用聚合函数
	- 2.**having** 发生在分组 group by之后,因而having中可以使用分组字段,无法直接取到其他字段,可以使用其他函数
- **select** :挑选
- **distinct**:去重
- **order by:**排序
	- asc:正序 小-->大
	- DESC:倒序 大---->小
- **limit**:限制结果的显示条数
	- 第一个是:起始位置
	- 第二个是:显示的条数

#### 多表查询

1. select   字段  from 表1 inner | left |right  join 表2 on 表1.字段  = 表2.字段
	- inner 是只连接匹配的行
	- right:外键之右连接:优先显示右半部分
	- left:外键之左连接:优先显示左半部分
	- union:连接left和right:可以显示全部信息
2. 符合条件的连接查询
	- on:后面加两个表的比较条件
3. 子查询
	- 子查询是将一个查询语句嵌套在另一个查询语句中 
	- 内层查询语句的查询结果,可以为外层查询语句提供条件 
	- 子查询中可以包含:in ,not,any,all,exists和not exists 
	- EXISTS:判断的是真和假,有内容为真,没有就是假 

#### 聚合函数

| 函数名                  | 说明                   |
| ----------------------- | ---------------------- |
| **max**()               | 求最大值               |
| **min**()               | 求最小值               |
| **avg**()               | 求平均值               |
| **sum**()               | 求和                   |
| **count**()             | 求总个数               |
| **group_concat**(name): | 查找这个组里所有的名字 |

### pymsql的使用(python)

```python
import pymysql

1.连接  host:数据库地址  port:端口 user:用户名 password:密码 db:数据库 charset:指定类型
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='db8', charset='utf8')


 2.创建游标
cursor = conn.cursor()

# 防止注入
sql = "select * from userinfo where username='%s' and pwd='%s'" 
cursor.execute(sql,[user,pwd])

# 增
# 一条
sql = "insert into userinfo(username,pwd,) values(xx,oo)" 
cursor.execute(sql)
# 多条
cursor.executemany(sql,[(),(),()])

# 删
sql = "delete from userinfo where id = 2"
cursor.execute(sql)

# 改
sql = "update userinfo set userinfo=%s where id = 2"
cursor.execute(sql,username)

# 查
fetchone():获取下一行数据，第一次为首行；
fetchall():获取所有行数据源
fetchmany(4):获取4行数据

sql = 'select * from userinfo'
cursor.execute(sql)

# 查询第一行的数据
row = cursor.fetchone() 
# 获取查询的指定条数的信息
ret = cursor.fetchmany(3)
# 获取查询的所有信息
ret = cursor.fetchall()


# ------------------事务--------------
sql = "insert into userinfo(name,password) values(%s,%s)"
try:
    # 执行SQL语句
    res = cursor.execute(sql,["rain222","1234"])
    # 提交事务
    conn.commit()
    # 提交之后，获取刚插入的数据的ID
    last_id = cursor.lastrowid
except Exception as e:
    # 有异常，回滚事务
    conn.rollback()
# ----------------------------------------



# 移动指针
cursor.scroll(1,mode='relative')  # 相对当前位置移动
cursor.scroll(2,mode='absolute') # 相对绝对位置移动
第一个值为移动的行数，整数为向下移动，负数为向上移动，mode指定了是相对当前位置移动，还是相对于首行移动

# 关闭连接，游标和连接都要关闭
cursor.close()
conn.close()
```
### 数据库的备份和还原

#### 备份

```sql
-- 备份一个数据库
基本语法
mysqldump -u username -p dbname table1 table2 ...-> BackupName.sql
	dbname参数表示数据库的名称；
	table1和table2参数表示需要备份的表的名称，为空则整个数据库备份；
	BackupName.sql参数表设计备份文件的名称，文件名前面可以加上一个绝对路径。通常将数据库被分成一个后缀名为sql的文件；
-- 备份多个数据库
mysqldump -u username -p --databases dbname2 dbname2 > Backup.sql
	加上了--databases选项，然后后面跟多个数据库
-- 备份所有数据库
mysqldump -u -root -p -all-databases > D:\all.sql
```

#### 还原

```sql
mysql -u root -p < C:\backup.sql
```


注意：这种方法不适用于InnoDB存储引擎的表，而对于MyISAM存储引擎的表很方便。同时，还原时MySQL的版本最好相同。




