---
title: mysql进阶
date: 2019-01-14 22:38:44
tags: [mysql]
categories: [数据库]
---

### 存储过程

#### 一.存储过程的定义

**存储过程**是把一段代码封装起来，当要执行这一段代码的时候，可以通过调用该存储过程来实现（经过第一次编译后再次调用不需要再次编译，比一个个执行sql语句效率高）

#### **二.存储过程的优点**

1. 通常存储过程有助于提高应用程序的性能。当创建，存储过程被编译之后，就存储在数据库中。 但是，MySQL实现的存储过程略有不同。 MySQL存储过程按需编译。 在编译存储过程之后，MySQL将其放入缓存中。 MySQL为每个连接维护自己的存储过程高速缓存。 如果应用程序在单个连接中多次使用存储过程，则使用编译版本，否则存储过程的工作方式类似于查询。
2. 存储过程有助于减少应用程序和数据库服务器之间的流量，因为应用程序不必发送多个冗长的SQL语句，而只能发送存储过程的名称和参数。
3. 存储的程序对任何应用程序都是可重用的和透明的。 存储过程将数据库接口暴露给所有应用程序，以便开发人员不必开发存储过程中已支持的功能。
4. 存储的程序是安全的。 数据库管理员可以向访问数据库中存储过程的应用程序授予适当的权限，而不向基础数据库表提供任何权限。

#### 三.存储过程的缺点

1. 如果使用大量存储过程，那么使用这些存储过程的每个连接的内存使用量将会大大增加。 此外，如果您在存储过程中过度使用大量逻辑操作，则CPU使用率也会增加，因为数据库服务器的设计不当于逻辑运算
2. 存储过程的构造使得开发具有复杂业务逻辑的存储过程变得更加困难。
3. 很难调试存储过程。只有少数数据库管理系统允许您调试存储过程。不幸的是，MySQL不提供调试存储过程的功能。
4. 开发和维护存储过程并不容易。开发和维护存储过程通常需要一个不是所有应用程序开发人员拥有的专业技能。这可能会导致应用程序开发和维护阶段的问题。

#### **四.一个简单的mysql存储过程示例**

```sql
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

```python
mysql中调用存储过程 
call b1()

在python中基于pymysql调用
cursor.callproc('b1') 
print(cursor.fetchall())
```

#### 五.声明变量

要在存储过程中声明变量，可以使用delclare语句，如下 

```python
DECLARE variable_name datatype(size) DEFAULT default_value;
```

1. 在DECLARE关键字后面要指定变量名。变量名必须遵循MySQL表列名称的命名规则 
2. 指定变量的数据类型及其大小。变量可以有任何MySQL数据类型，如INT，VARCHAR，DATETIME等。 
3. 当声明一个变量时，它的初始值为NULL。但是可以使用DEFAULT关键字为变量分配默认值 

```python
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

#### 六.存储过程传参

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

```python
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

事务用于将某些操作的多个sql作为原子性操作,一旦有某一个出现错误,即可回滚到原来的状态,从而保证数据库的完整性

#### 事务的四大特性

- **原子性:**是指事务是一个不可分割的整体,事务中的操作要么就全部发生,要么都不成功
- **一致性:**事务处理前后数据的完整性必须保持一致,**完整性**是指一个数据在某个时间点完全满足数据库中的约束要求
- **隔离性:**是指多个用户访问一个数据库时,一个用户的事务处理不能被其他用户的事务所干扰,多个并发事务之间相互隔离
- **持久性:**是指一个事务一旦被提交,他对数据库中的数据改变是永久的

**举例说明**

```sql
create table user2(
id int primary key auto_increment,
name char(32),
balance int
);

insert into user2(name,balance)
values
('wsb',1000),
('egn',1000),
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

#### 一.索引的介绍

数据库中专门用于帮助用户快速查找数据的一种数据结构。类似于字典中的目录，查找字典内容时可以根据目录查找到数据的存放位置吗，然后直接获取。

#### 二.索引的作用

约束和加速查找

#### 三.常见的几种索引

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

#### **四.索引的种类**

hash索引和BTree索引

- hash类型的索引：查询单条快，范围查询慢
- btree类型的索引：b+树，层数越多，数据量指数级增长（我们就用它，因为innodb默认支持它）

#### **五.索引的实现原理**

**数据库索引**，是数据库管理系统中一个排序的数据结构，以协助快速查询、更新数据库表中数据。**索引的实现通常使用B树及其变种B+树**。 

为表设置索引要付出**代价**的

- 一是增加了数据库的存储空间,
- 二是在插入和修改数据的时候要花费较多的时间(因为索引也要随之变动)

#### 六.索引详细解释

##### **普通索引**

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

##### **唯一索引**

**唯一索引的两个功能:加速查找和唯一约束(可含null)**

```sql
创建表和唯一索引
create table userinfo(
                   id int not null auto_increment primary key,
                   name varchar(32) not null,
                   email varchar(64) not null,
                   unique  index  ix_name(name)
               );
```

```sql
唯一索引
create unique index 索引名 on 表名(列名)
```

```sql
删除唯一索引
drop index 索引名 on 表名;
```

##### 主键索引

**主键索引的两个功能:加速查找和唯一约束(可含null)**

```sql
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

```sql
创建主键索引
alter table 表名 add primary key(列名);
```

```sql
删除主键索引
alter table 表名 drop primary key;
alter table 表名  modify  列名 int, drop primary key;
```

##### 组合索引

组合索引是将n个列组合成一个索引

```sql
联合普通索引
create index 索引名 on 表名(列名1,列名2);
```

#### 七.索引名词

```sql
覆盖索引:在索引文件中直接获取数据
select name from userinfo where name = 'alex50000';
索引合并:把多个单例索引合并使用
select * from  userinfo where name = 'alex13131' and id = 13131;
```

#### 八.索引注意事项

```sql
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

### 数据库的引擎

#### mysql所支持的引擎

```sql
show engines\G;查看所有支持的引擎
show variables like 'storage_engine%'; 查看正在使用的存储引擎
create table t1(id int)engine=innodb;# 指定表类型/存储引擎 默认不写就是innodb
```

#### **1.innoDB存储引擎**

支持事务,其设计目标主要面向联机事务处理(OLTP)的应用,其特点是行锁的设计,支持外键,并支持类似oracle的非锁定读,即默认读取操作不会产生锁,从mysql5.58版本开始是默认的存储引擎

#### **2.MylSAM存储引擎**

不支持事务,表锁设计,支持全文索引,主要面向一些OLAP数据库应用,在mysql5.58版本之前是默认的存储引擎,(除 Windows 版本外 )数据库系统 与文件系统一个很大的不同在于对事务的支持,MyISAM 存储引擎是不支持事务的。究其根 本,这也并不难理解。用户在所有的应用中是否都需要事务呢?在数据仓库中,如果没有 ETL 这些操作,只是简单地通过报表查询还需要事务的支持吗?此外,MyISAM 存储引擎的 另一个与众不同的地方是,它的缓冲池只缓存(cache)索引文件,而不缓存数据文件,这与 大多数的数据库都不相同。 

#### **3.NDB存储引擎**

 NDB 存储引擎是一个集群存储引擎,类似于 Oracle 的 RAC 集群,不过与 Oracle RAC 的 share everything 结构不同的是,其结构是 share nothing 的集群架构,因此能提供更高级别的 高可用性。NDB 存储引擎的特点是数据全部放在内存中(从 5.1 版本开始,可以将非索引数 据放在磁盘上),因此主键查找(primary key lookups)的速度极快,并且能够在线添加 NDB 数据存储节点(data node)以便线性地提高数据库性能。由此可见,NDB 存储引擎是高可用、 高性能、高可扩展性的数据库集群系统,其面向的也是 OLTP 的数据库应用类型。 

#### **4、Memory 存储引擎** 

正如其名,Memory 存储引擎中的数据都存放在内存中,数据库重 启或发生崩溃,表中的数据都将消失。它非常适合于存储 OLTP 数据库应用中临时数据的临时表,也可以作为 OLAP 数据库应用中数据仓库的维度表。Memory 存储引擎默认使用哈希 索引,而不是通常熟悉的 B+ 树索引。 

#### 5.**Infobright 存储引擎** 

第三方的存储引擎。其特点是存储是按照列而非行的,因此非常 适合 OLAP 的数据库应用。其官方网站是 [http://www.infobright.org/,上面有不少成功的数据](http://www.infobright.org/,%E4%B8%8A%E9%9D%A2%E6%9C%89%E4%B8%8D%E5%B0%91%E6%88%90%E5%8A%9F%E7%9A%84%E6%95%B0%E6%8D%AE) 仓库案例可供分析。 

#### **6、NTSE 存储引擎** 

网易公司开发的面向其内部使用的存储引擎。目前的版本不支持事务, 但提供压缩、行级缓存等特性,不久的将来会实现面向内存的事务支持 

#### **7、BLACKHOLE** 

黑洞存储引擎，可以应用于主备复制中的分发主库。

### 数据库的锁

#### **表级别锁**(table-level)

表级别的锁定是mysql个存储引擎中最大颗粒度的锁定机制,该锁定最大的特点就是实现逻辑非常简单,带来的系统负面影响最小,所以获取锁和释放锁都非常快,由于表级锁一次会将整个表都锁住,所以可以很好的避免死锁的问题

使用表级锁的主要是:myiSAM,MEMORY,CSV等一些非事务型存储引擎

#### **行级锁**(row-level)

行级锁最大的特点就是锁定对象的颗粒度很小,也是目前各大数据库管理软件所实现的锁定颗粒度最小的,由于颗粒度很小,所以发生多锁定字段争用的概率也是最小的,能够给予应用程序尽可能大的并发处理能力而提高一些需要高并发应用系统的整体性能

虽然在并发处理上有很大的优势,但是行级索引也因此带来很多的弊端,由于锁定资源的颗粒度很小,所以每次获取和释放锁需要做的事情也多了,因此带来的消耗也就大了,行级锁很容易带来死锁

使用行级锁的主要是innoDB存储引擎

#### **页级锁定**(page-level)

页级锁定是mysql中比较独特的一种锁定级别,在其他的数据库管理中不是太常见,页级锁定的特点:**锁定颗粒度介于行级锁和表级锁之间的**,所以获取锁定所需要的开销以及所能够提供的并发处理能力也是介于上面两者之间的,

使用页级锁定的主要是berkeleyDB存储引擎

#### **总结**

**表级锁:**开销小.加锁快,不会出现死锁;锁定粒度大,发生锁冲突的概率最高,并发度最低

**行级锁**:开销大,加锁慢,会出现死锁,锁定粒度最小,发生锁冲突概率最低,并发程度最高

**页面锁:**开锁和加锁时间介于表锁和行锁之间,会出现死锁;锁定粒度介于表锁和行锁之间,并发一般

#### **应用**

三个锁之间各有各的特点,如果从锁的角度来说,表级锁更适合查询为主,只有少量按索引条件更新数据的应用 ,如web应用;航迹锁更适用于有大量按索引条件,并发更新少量不同数据,同时又有并发查询的应用,如一些在线事务处理(OLTP)系统

#### **MYSQL表级锁有两种模式**

1. 表共享读锁(Table Read Lock) 对mylSAM表进行读取操作时不会阻塞其他用户对同一表的写操作
2. 表独占写锁(Table write Lock) 对MylSAM表的写操作,则会阻塞对其他用户对同一表的读写操作

#### innoDB和MyiSAM锁最大的不同

- InnoDB支持事务,Myisam不支持
- innoDB可以使用行级锁和表锁,MyiSAM只支持表锁

### 视图

#### 1.视图的定义

视图是虚拟表或逻辑表，它被定义为具有连接的SQL SELECT查询语句。因为数据库视图与数据库表类似，它由行和列组成，因此可以根据数据库表查询数据。其内容由查询定义。
       但是，视图并不在数据库中以存储的数据值集形式存在，行和列数据来自由定义视图的查询所引用的表，并且在引用视图时动态生成。简单的来说视图是由其定义结果组成的表；

#### 2.视图的优点

1.数据库视图允许简化复杂查询，通过数据库视图，您只需使用简单的SQL语句，而不是使用具有多个连接的复杂的SQL语句。
2.安全性。一般是这样做的:创建一个视图，定义好该视图所操作的数据。之后将用户权限与视图绑定。这样的方式是使用到了一个特性：grant语句可以针对视图进行授予权限。

#### **3.视图的缺点**

1、性能：从数据库视图查询数据可能会很慢，特别是如果视图是基于其他视图创建的。

2、表依赖关系：将根据数据库的基础表创建一个视图。每当更改与其相关联的表的结构时，都必须更改视图。

#### **4.创建视图**

**语法:** create view 视图名称 as sql语句

```sql
create view teacher_view as select tid from teacher where tname='李平老师';
select cname from course where teacher_id = (select tid from teacher_view);
```

#### **5.使用视图**

```
 往真实表中插入一条数据，查看一下视图，发现视图表也会跟着更新
 insert into course(cname,teacher_id) values('张三丰',2);
 更新一下数据，发现视图的数据也会跟着更新
 update course set cname='王五';
 不能修改视图的数据
```

#### **6.修改视图**

```
语法：ALTER VIEW 视图名称 AS SQL语句
alter view teacher_view as select * from course where cid>3;
```

#### **7.删除视图**

```
语法：DROP VIEW 视图名称
DROP VIEW teacher_view
```

### 触发器

**触发器:**触发器是一个特殊的存储过程，它是MySQL在insert、update、delete的时候自动执行的代码块。

#### 1.创建触发器

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

#### **2.使用触发器**

触发器无法由用户直接调用,而只能由于对表的[增删改查]操作被动引起的

#### **3.删除触发器**

```
drop trigger trigger_userLog;
```



