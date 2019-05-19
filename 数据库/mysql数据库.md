### mysql数据库基本命令

**数据库的增删改查**

- **增**
	- create database  数据库名称;
- **删**
	- drop database 库名;
- **改**
	- alter database 库名  更改的内容;
- 查
	- show create database 库名;查看当前创建的数据库
	- show databases; 查看所有的数据库
	- select database();查看所在的数据库

**表的增删改查**

**use 库名;进入这个库**

- **增**
	- create table 表名(字段名 类型 约束);
- **删**
	- drop table 表名;
- 改
	- alter table 表名 modify 字段名 类型;
	- 增加字段 alter table 表名 add 字段名;
- 查
	- show create table 表名;查看表的详细信息
	- show tables;查看这个数据库先所有的表
	- desc 表名;查看这个表里面所有的字段

**记录的增删改查**

- 增

	- insert into 表名(字段名) values (内容);

- **删**

	- delete from 表名;这个是清空,里面的自增不会去除
	- truncate 表名;删除所有的内容

- 改

	- update 表名 set name="xxx" where 条件;
	- update 表名 set 要修改的内容;

- 查

	- select 字段名 from 表名;
	- select 字段1,字段2,字段3 from 表名;
	- select * from 表名;查看所有内容;

	

### mysql的数据类型

**数据类型:**定义列中可以存储什么数据以及该数据实际怎样存储的基本规则，其用于以下几个目的

- 允许限制可存储在列中的数据
- 允许在内部更有效的存储数据
- 允许变换排序顺序（作为数值数据类型，数值才能正确排序）

**一.字符串数据类型**

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

**二.数值类型**

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

**三.日期和时间类型**

表示时间值的日期和时间类型为DATETIME、DATE、TIMESTAMP、TIME和YEAR。 

| 类型      | 大小(字节) | 范围                                                         | 格式                | 用途                     |
| --------- | ---------- | ------------------------------------------------------------ | ------------------- | ------------------------ |
| date      | 3          | 1000-01-01/9999-12-31                                        | YYYY-MM-DD          | 日期值                   |
| time      | 3          | -838:59:59'/'838:59:59'                                      | HH:MM:SS            | 时间值或持续时间         |
| year      | 1          | 1901/2155                                                    | YYYY                | 年份值                   |
| datetime  | 8          | 1000-01-01 00:00:00/9999-12-31 23:59:59                      | YYYY-MM-DD HH:MM:SS | 混合日期和时间值         |
| timestamp | 4          | 1970-01-01 00:00:00/2038结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYYMMDD HHMMSS     | 混合日期和时间值，时间戳 |

**四.枚举和集合**

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
| on update cascade |同步更新|

### **外键变种的三种关系**

- 一对一
- 一对多
- 多对多

### 单表查询

**语法:**select 字段1,字段2 from 表名

| 关键字  | 说明         |
| ------- | ------------ |
| from 表 | 要找的表     |
| where   | 指定约束条件 |

- 1.比较运算符 :>,<,>=,<=,!=
- 2.between 80 and 100 :值在80到100之间
- 3.in(80,90,100):值是80,90或100
- 4.like 'xiaomagepattern': pattern可以是%或者_。%小时任意多字符，_表示一个字符
- 5.逻辑运算符：在多个条件直接可以使用逻辑运算符 and or not

| **group by**  | **分组** |
| ------------- | -------- |
| **having**    | **过滤** |
| **select**    | **选择** |
| **distinct**  | **去重** |
| **order  by** | **排序** |

- asc:正序  小------>大
- DESC:倒序   大------>小
- limit :限制结果的显示条数
	- 第一个是:起始位置
	- 第二个是:显示的条数

**聚合函数**

| 函数名              | 说明                   |
| ------------------- | ---------------------- |
| max()               | 求最大值               |
| min()               | 求最小值               |
| avg()               | 求平均值               |
| sum()               | 求和                   |
| count()             | 求总个数               |
| group_concat(name): | 查找这个组里所有的名字 |

### 多表查询

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

### 视图

**1.视图的定义:**

​       视图是虚拟表或逻辑表，它被定义为具有连接的SQL SELECT查询语句。因为数据库视图与数据库表类似，它由行和列组成，因此可以根据数据库表查询数据。其内容由查询定义。
       但是，视图并不在数据库中以存储的数据值集形式存在，行和列数据来自由定义视图的查询所引用的表，并且在引用视图时动态生成。简单的来说视图是由其定义结果组成的表；

**2.视图优点**

​          1、数据库视图允许简化复杂查询，通过数据库视图，您只需使用简单的SQL语句，而不是使用具有多个连接的复杂的SQL语句。
          2、安全性。一般是这样做的:创建一个视图，定义好该视图所操作的数据。之后将用户权限与视图绑定。这样的方式是使用到了一个特性：grant语句可以针对视图进行授予权限。

**3.视图的缺点**

1、性能：从数据库视图查询数据可能会很慢，特别是如果视图是基于其他视图创建的。

2、表依赖关系：将根据数据库的基础表创建一个视图。每当更改与其相关联的表的结构时，都必须更改视图。

**4.创建视图**

**语法:** create view 视图名称 as sql语句

```sql
create view teacher_view as select tid from teacher where tname='李平老师';
select cname from course where teacher_id = (select tid from teacher_view);
```

**5.使用视图**

```
 往真实表中插入一条数据，查看一下视图，发现视图表也会跟着更新
 insert into course(cname,teacher_id) values('张三丰',2);
 更新一下数据，发现视图的数据也会跟着更新
 update course set cname='王五';
 不能修改视图的数据
```

**6.修改视图**

```
语法：ALTER VIEW 视图名称 AS SQL语句
alter view teacher_view as select * from course where cid>3;
```

**7.删除视图**

```
语法：DROP VIEW 视图名称
DROP VIEW teacher_view
```

### 触发器

**触发器:**触发器是一个特殊的存储过程，它是MySQL在insert、update、delete的时候自动执行的代码块。

**1.创建触发器**

```sql
# 插入前
CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 插入后
CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除前
CREATE TRIGGER tri_before_delete_tb1 BEFORE DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除后
CREATE TRIGGER tri_after_delete_tb1 AFTER DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新前
CREATE TRIGGER tri_before_update_tb1 BEFORE UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新后
CREATE TRIGGER tri_after_update_tb1 AFTER UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END
```

```sql
# 创建用户表
create table user(
    id int primary key auto_increment,
    name varchar(20) not null,
    reg_time datetime, # 注册用户的时间
    affirm enum('yes','no') # no表示该用户执行失败
);

#创建日志表
create table userLog(
    id int primary key auto_increment,
    u_name varchar(20) not null,
    u_reg_time datetime # 注册用户的时间
);

# 创建触发器 delimiter 默认情况下，delimiter是分号 触发器名称应遵循命名约定[trigger time]_[table name]_[trigger event]
delimiter //
create trigger after_user_insert after insert on user for each row
begin
    if new.affirm = 'yes' then
        insert into userLog(u_name,u_reg_time) values(new.name,new.reg_time);
    end if;

end //
delimiter ;


#往用户表中插入记录，触发触发器，根据if的条件决定是否插入数据
insert into user(name,reg_time,affirm) values ('张三',now(),'yes'),('李四',now(),'yes'),('王五',now(),'no');
```

**注意:**请注意，在为INSERT定义的触发器中，可以仅使用NEW关键字。不能使用OLD关键字。但是，在为DELETE定义的触发器中，没有新行，因此您只能使用OLD关键字。在UPDATE触发器中，OLD是指更新前的行，而NEW是更新后的行

**2.使用触发器**

触发器无法由用户直接调用,而只能由于对表的[增删改查]操作被动引起的

**3.删除触发器**

```
drop trigger trigger_userLog;
```

### 存储过程

**一.存储过程的定义**

**存储过程**是把一段代码封装起来，当要执行这一段代码的时候，可以通过调用该存储过程来实现（经过第一次编译后再次调用不需要再次编译，比一个个执行sql语句效率高）

**二.存储过程的优点**

1. 通常存储过程有助于提高应用程序的性能。当创建，存储过程被编译之后，就存储在数据库中。 但是，MySQL实现的存储过程略有不同。 MySQL存储过程按需编译。 在编译存储过程之后，MySQL将其放入缓存中。 MySQL为每个连接维护自己的存储过程高速缓存。 如果应用程序在单个连接中多次使用存储过程，则使用编译版本，否则存储过程的工作方式类似于查询。
2. 存储过程有助于减少应用程序和数据库服务器之间的流量，因为应用程序不必发送多个冗长的SQL语句，而只能发送存储过程的名称和参数。
3. 存储的程序对任何应用程序都是可重用的和透明的。 存储过程将数据库接口暴露给所有应用程序，以便开发人员不必开发存储过程中已支持的功能。
4. 存储的程序是安全的。 数据库管理员可以向访问数据库中存储过程的应用程序授予适当的权限，而不向基础数据库表提供任何权限。

**三.存储过程的缺点**

1. 如果使用大量存储过程，那么使用这些存储过程的每个连接的内存使用量将会大大增加。 此外，如果您在存储过程中过度使用大量逻辑操作，则CPU使用率也会增加，因为数据库服务器的设计不当于逻辑运算
2. 存储过程的构造使得开发具有复杂业务逻辑的存储过程变得更加困难。
3. 很难调试存储过程。只有少数数据库管理系统允许您调试存储过程。不幸的是，MySQL不提供调试存储过程的功能。
4. 开发和维护存储过程并不容易。开发和维护存储过程通常需要一个不是所有应用程序开发人员拥有的专业技能。这可能会导致应用程序开发和维护阶段的问题。

**四.一个简单的mysql存储过程示例**

```
delimiter //
 create procedure b1()
   begin
   select *  from blog;
   end //
delimiter ;
```

**解释:**

1. 第一个命令是delimiter //，它与存储过程语法无关。 delimter语句将标准分隔符 - 分号(;)更改为：//。 在这种情况下，分隔符从分号(;)更改为双斜杠//。为什么我们必须更改分隔符？ 因为我们想将存储过程作为整体传递给服务器，而不是让mysql工具一次解释每个语句。 在END关键字之后，使用分隔符//来指示存储过程的结束。 最后一个命令(DELIMITER;)将分隔符更改回分号(;)。 
2. .使用create procedure语句创建一个新的存储过程。在create procedure语句之后指定存储过程的名称。在这个示例中，存储过程的名称为：b1，并把括号放在存储过程的名字之后。 
3. begin和end之间的部分称为存储过程的主体。将声明性SQL语句放在主体中以处理业务逻辑。 在这个存储过程中，我们使用一个简单的select语句来查询blog表中的数据。 

```
mysql中调用存储过程 
call b1()

在python中基于pymysql调用
cursor.callproc('b1') 
print(cursor.fetchall())
```

**五.声明变量**

要在存储过程中声明变量，可以使用delclare语句，如下 

```
DECLARE variable_name datatype(size) DEFAULT default_value;
```

1. 在DECLARE关键字后面要指定变量名。变量名必须遵循MySQL表列名称的命名规则 
2. 指定变量的数据类型及其大小。变量可以有任何MySQL数据类型，如INT，VARCHAR，DATETIME等。 
3. 当声明一个变量时，它的初始值为NULL。但是可以使用DEFAULT关键字为变量分配默认值 

```
delimiter //
 create procedure b2()
   begin
   DECLARE n int DEFAULT 1;
   set n  = 5;
   select *  from blog where id = n;
   end //
delimiter ;

# mysql中调用存储过程
call b2();
```

**六.存储过程传参**

在现实应用中，开发的存储过程几乎都需要参数。这些参数使存储过程更加灵活和有用。 在MySQL中，参数有三种模式：IN，OUT或INOUT。 

**IN** - 是默认模式。在存储过程中定义IN参数时，调用程序必须将参数传递给存储过程。 另外，IN参数的值被保护。这意味着即使在存储过程中更改了IN参数的值，在存储过程结束后仍保留其原始值。换句话说，存储过程只使用IN参数的副本。 

**OUT** - 可以在存储过程中更改OUT参数的值，并将其更改后新值传递回调用程序。请注意，存储过程在启动时无法访问OUT参数的初始值。 

**INOUT** - INOUT参数是IN和OUT参数的组合。这意味着调用程序可以传递参数，并且存储过程可以修改INOUT参数并将新值传递回调用程序。 

在存储过程中定义参数的语法如下 

```
MODE param_name param_type(param_size)
```

根据存储过程中参数的目的，MODE可以是IN，OUT或INOUT。 param_name是参数的名称。参数的名称必须遵循MySQL中列名的命名规则。 在参数名之后是它的数据类型和大小。和变量一样，参数的数据类型可以是任何有效的MySQL数据类型 

如果存储过程有多个参数，则每个参数由逗号(,)分隔。 

```
# 1.in
delimiter //
 create procedure b3(
     in blogName varchar(30)
 )
   begin
   select *  from blog where NAME = blogName;
   end //
delimiter ;

#mysql中调用存储过程
call b3('第5篇');

#python中调用存储过程
cursor.callproc('b3',args = ('第5篇')); 


# 2.out
delimiter //
 create procedure b4(
     in year int,
     out count  int
 )
   begin
       SELECT COUNT(1) into count  FROM blog GROUP BY DATE_FORMAT(sub_time,'%Y') having max(DATE_FORMAT(sub_time,'%Y')) = year ;
       set count = 6;
   end //
delimiter ;

call b4(2016,@count);
select @count;
 
#out只能当返回值


 # 3.inout

delimiter //
 create procedure b5(
     inout n1 int
 )
   begin
    select * from blog where id > n1;
   end //
delimiter ;

#mysql中调用
set @n = 3;
call b5(@n);
select @n;

#在python中基于pymysql调用
cursor.callproc('b5',(4))
print(cursor.fetchall()) #查询select的查询结果

cursor.execute('select @n1') 
print(cursor.fetchall())
# inout:既可以传入又可以返回
```

### 事务

1、什么是事务：数据库中的事务是指逻辑上的一组操作，这组操作要么都执行成功，要么都不执行成功。 

2、事务的管理：默认情况下Mysql会自动管理事务，一条SQL语句独占一个事务。 

**事务的四大特性** 

- **原子性:**是指事务是一个不可分割的整体,事务中的操作要么就全部发生,要么都不成功
- **一致性:**事务处理前后数据的完整性必须保持一致,**完整性**是指一个数据在某个时间点完全满足数据库中的约束要求
- **隔离性:**是指多个用户访问一个数据库时,一个用户的事务处理不能被其他用户的事务所干扰,多个并发事务之间相互隔离
- **持久性:**是指一个事务一旦被提交,他对数据库中的数据改变是永久的

举例说明:

```
create table user2(
id int primary key auto_increment,
name char(32),
balance int
);

insert into user2(name,balance)
values
('wsb',1000),
('egon',1000),
('ysb',1000);


#原子操作
start transaction;
update user2 set balance=900 where name='wsb'; #买支付100元
update user2 set balance=1010 where name='egon'; #中介拿走10元
update user2 set balance=1090 where name='ysb'; #卖家拿到90元
commit;

#出现异常，回滚到初始状态
start transaction;
update user2 set balance=900 where name='wsb'; #买支付100元
update user2 set balance=1010 where name='egon'; #中介拿走10元
uppdate user2 set balance=1090 where name='ysb'; #卖家拿到90元,出现异常没有拿到
rollback;

```

下面是操作：**当p_return_code为1时，表示异常，立马回滚。当为2时，出现警告，立马回滚原始状态。0表示成功** 

```
delimiter //
create PROCEDURE b6(
    OUT p_return_code tinyint
)
BEGIN 
    DECLARE exit handler for sqlexception 
    BEGIN 
        -- ERROR 
        set p_return_code = 1; 
        rollback; 
    END; 

    DECLARE exit handler for sqlwarning 
    BEGIN 
        -- WARNING 
        set p_return_code = 2; 
        rollback; 
    END; 

    START TRANSACTION; 
        insert into blog(name,sub_time) values('yyy',now());
    COMMIT; 

    -- SUCCESS 
    set p_return_code = 0; #0代表执行成功

END //
delimiter ;

set @res=123;
call b6(@res);
select @res;
```

### 索引

**一.索引的介绍**

数据库中专门用于帮助用户快速查找数据的一种数据结构。类似于字典中的目录，查找字典内容时可以根据目录查找到数据的存放位置吗，然后直接获取。

**二.索引的作用**

约束和加速查找

**三.常见的几种索引**

- 普通索引
- 唯一索引
- 主键索引
- 联合索引
	- 联合主键索引
	- 联合唯一索引
	- 联合普通索引

**无索引**： 从前往后一条一条查询

**有索引**：创建索引的本质，就是创建额外的文件（某种格式存储，查询的时候，先去格外的文件找，定好位置，然后再去原始表中直接查询。但是创建索引越多，会对硬盘也是有损耗。

**建立索引的目的**：

- a.额外的文件保存特殊的数据结构
- b.查询快，但是插入更新删除依然慢
- c.创建索引之后，必须命中索引才能有效

**索引的种类**

hash索引和BTree索引

- hash类型的索引：查询单条快，范围查询慢
- btree类型的索引：b+树，层数越多，数据量指数级增长（我们就用它，因为innodb默认支持它）

**索引的实现原理**

**数据库索引**，是数据库管理系统中一个排序的数据结构，以协助快速查询、更新数据库表中数据。**索引的实现通常使用B树及其变种B+树**。 

为表设置索引要付出**代价**的

- 一是增加了数据库的存储空间,
- 二是在插入和修改数据的时候要花费较多的时间(因为索引也要随之变动)

**普通索引**

**作用:仅有一个加速查找**

```
创建表+普通索引
create table userinfo(
                   nid int not null auto_increment primary key,
                   name varchar(32) not null,
                   email varchar(64) not null,
                   index ix_name(name)
               );
```

```
普通索引
create index 索引的名字 on 表名(列名)
```

```
删除索引
drop index 索引的名字 on 表名
```

```
查看索引
show index from 表名
```

**唯一索引**

**唯一索引的两个功能:加速查找和唯一约束(可含null)**

```
创建表和唯一索引
create table userinfo(
                   id int not null auto_increment primary key,
                   name varchar(32) not null,
                   email varchar(64) not null,
                   unique  index  ix_name(name)
               );
```

```
唯一索引
create unique index 索引名 on 表名(列名)
```

```
删除唯一索引
drop index 索引名 on 表名;
```

**主键索引**

**主键索引的两个功能:加速查找和唯一约束(可含null)**

```
 创建表和主键索引
 create table userinfo(

                   id int not null auto_increment primary key,
                   name varchar(32) not null,
                   email varchar(64) not null,
                   unique  index  ix_name(name)
           )
          or

create table userinfo(
                   id int not null auto_increment,
                   name varchar(32) not null,
                   email varchar(64) not null,
                   primary key(nid),
                   unique  index  ix_name(name)
         )
```

```
创建主键索引
alter table 表名 add primary key(列名);
```

```
删除主键索引
alter table 表名 drop primary key;
alter table 表名  modify  列名 int, drop primary key;
```

**组合索引**

组合索引是将n个列组合成一个索引

```
联合普通索引
create index 索引名 on 表名(列名1,列名2);
```

**四.索引名词**

```
覆盖索引:在索引文件中直接获取数据
select name from userinfo where name = 'alex50000';
索引合并:把多个单例索引合并使用
select * from  userinfo where name = 'alex13131' and id = 13131;
```

**五.索引的注意事项**

```
(1)避免使用select *
(2)count(1)或count(列) 代替count(*)
(3)创建表时尽量使用char代替varchar
(4)表的字段顺序固定长度的字段优先
(5)组合索引代替多个单列索引（经常使用多个条件查询时）
(6)尽量使用短索引 （create index ix_title on tb(title(16));特殊的数据类型 text类型）
(7)使用连接（join）来代替子查询
(8)连表时注意条件类型需一致
(9)索引散列（重复少）不适用于建索引，例如：性别不合适
```

**六.执行计划**

explain + 查询SQL - 用于显示SQL执行信息参数，根据参考信息可以进行SQL优化 

```
参数说明
select_type：
     查询类型
         SIMPLE          简单查询
         PRIMARY         最外层查询
         SUBQUERY        映射为子查询
         DERIVED         子查询
         UNION           联合
         UNION RESULT    使用联合的结果
           
table：正在访问的表名            
type：查询时的访问方式
      性能：all < index < range < index_merge < ref_or_null < ref < eq_ref < system/const
       ALL             全表扫描，对于数据表从头到尾找一遍
       select * from userinfo;
        特别的：如果有limit限制，则找到之后就不在继续向下扫描
        select * from userinfo where email = 'alex112@oldboy'
        select * from userinfo where email = 'alex112@oldboy' limit 1;
        虽然上述两个语句都会进行全表扫描，第二句使用了limit，则找到一个后就不再继续扫描。
        
INDEX ： 全索引扫描，对索引从头到尾找一遍
         select nid from userinfo;

RANGE： 对索引列进行范围查找
      select *  from userinfo where name < 'alex';
      PS:
          between and
           in
           >   >=  <   <=  操作
           注意：!= 和 > 符号

INDEX_MERGE：  合并索引，使用多个单列索引搜索
     select *  from userinfo where name = 'alex' or nid in (11,22,33);
REF： 根据索引查找一个或多个值
    select *  from userinfo where name = 'alex112';

EQ_REF： 连接时使用primary key 或 unique类型
     select userinfo2.id,userinfo.name from userinfo2 left join tuserinfo on userinfo2.id = userinfo.id;

CONST：常量
           表最多有一个匹配行,因为仅有一行,在这行的列值可被优化器剩余部分认为是常数,const表很快,因为它们只读取一次。
     select id from userinfo where id = 2 ;

SYSTEM：系统
      表仅有一行(=系统表)。这是const联接类型的一个特例。
      select * from (select id from userinfo where id = 1) as A;

possible_keys：可能使用的索引

key：真实使用的

key_len：　　MySQL中使用索引字节长度

rows： mysql估计为了找到所需的行而要读取的行数 ------ 只是预估值

extra：
      该列包含MySQL解决查询的详细信息
      “Using index”
       此值表示mysql将使用覆盖索引，以避免访问表。不要把覆盖索引和index访问类型弄混了。
“Using where”
    这意味着mysql服务器将在存储引擎检索行后再进行过滤，许多where条件里涉及索引中的列，当（并且如果）它读取索引时，就能被存储引擎检验，因此不是所有带where子句的查询都会显示“Using where”。有时“Using where”的出现就是一个暗示：查询可受益于不同的索引。
“Using temporary”
       这意味着mysql在对查询结果排序时会使用一个临时表。
“Using filesort”
       这意味着mysql会对结果使用一个外部索引排序，而不是按索引次序从表里读取行。mysql有两种文件排序算法，这两种排序方式都可以在内存或者磁盘上完成，explain不会告诉你mysql将使用哪一种文件排序，也不会告诉你排序会在内存里还是磁盘上完成。
“Range checked for each record(index map: N)”
    这个意味着没有好用的索引，新的索引将在联接的每一行上重新估算，N是显示在possible_keys列中索引的位图，并且是冗余的
```

**七.慢日志记录**

开启慢查询日志，可以让MySQL记录下查询超过指定时间的语句，通过定位分析性能的瓶颈，才能更好的优化数据库系统的性能。 

```
(1) 进入MySql 查询是否开了慢查询
         show variables like 'slow_query%';
         参数解释：
             slow_query_log 慢查询开启状态  OFF 未开启 ON 为开启
        slow_query_log_file 慢查询日志存放的位置（这个目录需要MySQL的运行帐号的可写权限，一般设置为MySQL的数据存放目录）

（2）查看慢查询超时时间
       show variables like 'long%';
       ong_query_time 查询超过多少秒才记录   默认10秒 

（3）开启慢日志（1）（是否开启慢查询日志，1表示开启，0表示关闭。）
           set global slow_query_log=1;
（4）再次查看
              show variables like '%slow_query_log%';

（5）开启慢日志（2）：（推荐）
         在my.cnf 文件中
         找到[mysqld]下面添加：
           slow_query_log =1
   　　　　 slow_query_log_file=C:\mysql-5.6.40-winx64\data\localhost-slow.log
    　　　  long_query_time = 1

    参数说明：
        slow_query_log 慢查询开启状态  1 为开启
        slow_query_log_file 慢查询日志存放的位置
        long_query_time 查询超过多少秒才记录   默认10秒 修改为1秒
```

**分页功能**

```
（1）只有上一页和下一页
        做一个记录：记录当前页的最大id或最小id
        下一页：
        select * from userinfo where id>max_id limit 10;

        上一页：
        select * from userinfo where id<min_id order by id desc limit 10;

(2) 中间有页码的情况
           select * from userinfo where id in(
               select id from (select * from userinfo where id > pre_max_id limit (cur_max_id-pre_max_id)*10) as A order by A.id desc limit 10
           );    
```

### 数据库引擎

数据库中的表也应该有不同的类型,表的类型不一样,对应的mysql不同的存取机制,表类型又称为存储引擎

![](..\img\存储引擎.png)

**mysql支持的存储引擎**

```
show engines\G;查看所有支持的引擎
show variables like 'storage_engine%'; 查看正在使用的存储引擎
create table t1(id int)engine=innodb;# 指定表类型/存储引擎 默认不写就是innodb
```

**1.innoDB存储引擎**

支持事务,其设计目标主要面向联机事务处理(OLTP)的应用,其特点是行锁的设计,支持外键,并支持类似oracle的非锁定读,即默认读取操作不会产生锁,从mysql5.58版本开始是默认的存储引擎

**2.MylSAM存储引擎**

不支持事务,表锁设计,支持全文索引,主要面向一些OLAP数据库应用,在mysql5.58版本之前是默认的存储引擎,(除 Windows 版本外 )数据库系统 与文件系统一个很大的不同在于对事务的支持,MyISAM 存储引擎是不支持事务的。究其根 本,这也并不难理解。用户在所有的应用中是否都需要事务呢?在数据仓库中,如果没有 ETL 这些操作,只是简单地通过报表查询还需要事务的支持吗?此外,MyISAM 存储引擎的 另一个与众不同的地方是,它的缓冲池只缓存(cache)索引文件,而不缓存数据文件,这与 大多数的数据库都不相同。 

**3.NDB存储引擎**

 NDB 存储引擎是一个集群存储引擎,类似于 Oracle 的 RAC 集群,不过与 Oracle RAC 的 share everything 结构不同的是,其结构是 share nothing 的集群架构,因此能提供更高级别的 高可用性。NDB 存储引擎的特点是数据全部放在内存中(从 5.1 版本开始,可以将非索引数 据放在磁盘上),因此主键查找(primary key lookups)的速度极快,并且能够在线添加 NDB 数据存储节点(data node)以便线性地提高数据库性能。由此可见,NDB 存储引擎是高可用、 高性能、高可扩展性的数据库集群系统,其面向的也是 OLTP 的数据库应用类型。 

**4、Memory 存储引擎** 

正如其名,Memory 存储引擎中的数据都存放在内存中,数据库重 启或发生崩溃,表中的数据都将消失。它非常适合于存储 OLTP 数据库应用中临时数据的临时表,也可以作为 OLAP 数据库应用中数据仓库的维度表。Memory 存储引擎默认使用哈希 索引,而不是通常熟悉的 B+ 树索引。 

5.**Infobright 存储引擎** 

第三方的存储引擎。其特点是存储是按照列而非行的,因此非常 适合 OLAP 的数据库应用。其官方网站是 [http://www.infobright.org/,上面有不少成功的数据](http://www.infobright.org/,%E4%B8%8A%E9%9D%A2%E6%9C%89%E4%B8%8D%E5%B0%91%E6%88%90%E5%8A%9F%E7%9A%84%E6%95%B0%E6%8D%AE) 仓库案例可供分析。 

**6、NTSE 存储引擎** 

网易公司开发的面向其内部使用的存储引擎。目前的版本不支持事务, 但提供压缩、行级缓存等特性,不久的将来会实现面向内存的事务支持 

**7、BLACKHOLE** 

黑洞存储引擎，可以应用于主备复制中的分发主库。



### **pymysql的使用**

```python
import pymysql

1.连接  host:数据库地址  port:端口 user:用户名 password:密码 db:数据库 charset:指定类型
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='db8', charset='utf8')


 2.创建游标
cursor = conn.cursor()

防止注入
sql = "select * from userinfo where username='%s' and pwd='%s'" 
cursor.execute(sql,[user,pwd])

增

一条
sql = "insert into userinfo(username,pwd,) values(xx,oo)" 
cursor.execute(sql)
多条
cursor.executemany(sql,[(),(),()])

删
sql = "delete from userinfo where id = 2"
cursor.execute(sql)

改
sql = "update userinfo set userinfo=%s where id = 2"
cursor.execute(sql,username)

查
fetchone():获取下一行数据，第一次为首行；
fetchall():获取所有行数据源
fetchmany(4):获取4行数据

sql = 'select * from userinfo'
cursor.execute(sql)

 查询第一行的数据
row = cursor.fetchone()

移动指针
cursor.scroll(1,mode='relative')  # 相对当前位置移动
cursor.scroll(2,mode='absolute') # 相对绝对位置移动
第一个值为移动的行数，整数为向下移动，负数为向上移动，mode指定了是相对当前位置移动，还是相对于首行移动

# 关闭连接，游标和连接都要关闭
cursor.close()
conn.close()
复制代码
```

### **数据库的锁**

**表级别锁**(table-level)

表级别的锁定是mysql个存储引擎中最大颗粒度的锁定机制,该锁定最大的特点就是实现逻辑非常简单,带来的系统负面影响最小,所以获取锁和释放锁都非常快,由于表级锁一次会将整个表都锁住,所以可以很好的避免死锁的问题

使用表级锁的主要是:myiSAM,MEMORY,CSV等一些非事务型存储引擎

**行级锁**(row-level)

行级锁最大的特点就是锁定对象的颗粒度很小,也是目前各大数据库管理软件所实现的锁定颗粒度最小的,由于颗粒度很小,所以发生多锁定字段争用的概率也是最小的,能够给予应用程序尽可能大的并发处理能力而提高一些需要高并发应用系统的整体性能

虽然在并发处理上有很大的优势,但是行级索引也因此带来很多的弊端,由于锁定资源的颗粒度很小,所以每次获取和释放锁需要做的事情也多了,因此带来的消耗也就大了,行级锁很容易带来死锁

使用行级锁的主要是innoDB存储引擎

**3.页级锁定**(page-level)

页级锁定是mysql中比较独特的一种锁定级别,在其他的数据库管理中不是太常见,页级锁定的特点:**锁定颗粒度介于行级锁和表级锁之间的**,所以获取锁定所需要的开销以及所能够提供的并发处理能力也是介于上面两者之间的,

使用页级锁定的主要是berkeleyDB存储引擎

**总结**

**表级锁:**开销小.加锁快,不会出现死锁;锁定粒度大,发生锁冲突的概率最高,并发度最低

**行级锁**:开销大,加锁慢,会出现死锁,锁定粒度最小,发生锁冲突概率最低,并发程度最高

**页面锁:**开锁和加锁时间介于表锁和行锁之间,会出现死锁;锁定粒度介于表锁和行锁之间,并发一般

**应用**

三个锁之间各有各的特点,如果从锁的角度来说,表级锁更适合查询为主,只有少量按索引条件更新数据的应用 ,如web应用;航迹锁更适用于有大量按索引条件,并发更新少量不同数据,同时又有并发查询的应用,如一些在线事务处理(OLTP)系统

**MYSQL表级锁有两种模式**

1. 表共享读锁(Table Read Lock) 对mylSAM表进行读取操作时不会阻塞其他用户对同一表的写操作
2. 表独占写锁(Table write Lock) 对MylSAM表的写操作,则会阻塞对其他用户对同一表的读写操作

innoDB和MyiSAM锁最大的不同

- 支持事务
- 采用了行级锁

**事务的四大特性(简称ACID)**

- **原子性(Atomicity)**:事务是一个原子操作单位,其对数据的修改,要么全部都执行,要么全都不执行
- **一致性(Consistent)**:在事务开始和完成时,数据必须保持一致状态
- **隔离性(Islation):**数据库系统提供一定的隔离机制,保证事务在不受外部并发操作影响的情况的"独立"环境执行
- **持久性(Durable)**:事务完成之后,他对于数据的修改是永久性的,即使出现系统故障也能够保持

**并发事务处理带来的问题**

- **更新丢失**当两个或多个事务选择同一行,由于每个事务都不知道其他事务的存在,就会发生丢失更新问题,最后的更新还会覆盖由其他事务所做的更新
- **脏读:**一个事务正在对一条记录做修改,在这个事务完成并提交前,这条记录就处在不一致的状态,这时另一个事务也来读取同一条记录,如果不控制的话,第二个事务读取数据并做了一些处理,就会产生未提交的数据依赖关系,这种现象就被称为**脏读**
- **不可重复读**一个事务在读取某些数据后的某个时间,再次读取以前读过的数据,却发现其读出的数据已经发生了改变,或某些记录已经被删除了,这种现象叫不可重复读
- **幻读**:一个事务按相同的查询条件重新读取以前检索过的数据,却发现其他事务插入了满足其查询条件的新数据,这种现象称为幻读

```
表锁
Lock tables orders read local, order_detail read local;
Select sum(total) from orders;
Select sum(subtotal) from order_detail;
Unlock tables;

行锁
共享锁（S）：SELECT * FROM table_name WHERE ... LOCK IN SHARE MODE。
排他锁（X)：SELECT * FROM table_name WHERE ... FOR UPDATE。
```
