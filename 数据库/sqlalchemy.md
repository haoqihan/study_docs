### SQLAlchemy

SQLAlchemy是python语言下的一个orm框架,该框架简历在API之上,使用关系对象映射进行数据操作,简而言之:将对象换成SQL,然后使用API执行SQL并获取执行结果

### 数据库连接方式

```python
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
 
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
 
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
 
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
```

**步骤一:**

使用 Engine/ConnectionPooling/Dialect 进行数据库操作，Engine使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句。 

```
from sqlalchemy import create_engine
 
 
engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/s11", max_overflow=5)
 
engine.execute(
    "INSERT INTO ts_test (a, b) VALUES ('2', 'v1')"
)
 
engine.execute(
     "INSERT INTO ts_test (a, b) VALUES (%s, %s)",
    ((555, "v1"),(666, "v1"),)
)
engine.execute(
    "INSERT INTO ts_test (a, b) VALUES (%(id)s, %(name)s)",
    id=999, name="v1"
)
 
result = engine.execute('select * from ts_test')
result.fetchall()
```

**事务操作**

```python
from sqlalchemy import create_engine


engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/s11", max_overflow=5)


# 事务操作
with engine.begin() as conn:
    conn.execute("insert into table (x, y, z) values (1, 2, 3)")
    conn.execute("my_special_procedure(5)")
    
    
conn = engine.connect()
# 事务操作 
with conn.begin():
       conn.execute("some statement", {'x':5, 'y':10})
```

1.创建

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

#创建基类,相当于Django中的 models.Model,被各个数据表类所继承
Base = declarative_base()


# ##################### 单表示例 #########################
# 创建一张数据表
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)

    __table_args__ = (
        # UniqueConstraint('id', 'name', name='uix_id_name'),
        # Index('ix_id_name', 'name', 'extra'),
    )

# 创建另一张数据表
class School(Base):
    __tablename__ = "school"

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,unique=True)


# 创建数据库链接
engine = create_engine(
        "mysql+pymysql://root:DragonFire@localhost:3306/dragon?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )


# 通过Base.metadata找到所有继承 Base 的数据表class
Base.metadata.create_all(engine)

# SQLAlchemy数据表进行修改后,无法直接进行更新,只能删除表后进行操作,重新进行操作

创建基类和第一张数据表
```

2.增删改查

```python
from CreateDB import Users, School

# 1. 创建一个用户添加到数据库
# 创建连接
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:DragonFire@127.0.0.1:3306/dragon?charset=utf8",
                       )

# 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

 1.增加 操作数据表
 单行操作
 obj1 = Users(name="123") # 通过 Users数据表类创建一条数据
 db_session.add(obj1) # 将创建好的数据添加到 数据表操作对象的内存中,此时数据库还并不知道要添加数据
 db_session.commit() # 将数据表操作对象内存中的所有数据及操作提交到数据库中
 多行操作
 db_session.add_all([
     Users(name="zhangsan"),
     Users(name="lisi"),
 ])
db_session.commit()

 2.查询 数据表操作
 user_list = db_session.query(Users).all()  查询所有数据
 user_list = db_session.query(Users).filter(Users.id >=2 )  查询带有条件的数据 表达式 返回sql语句,循环依然可以获取到数据
 user_list = db_session.query(Users).filter(Users.id >=2 ).all() 查询带有条件的数据 表达式 返回数据列表
 print(user_list)
 for row in user_list:
     print(row.id,row.name)

 3.删除数据 数据表操作
 db_session.query(Users).filter(Users.id == 1).delete() # 删除带有条件的数据
 db_session.commit()

 4.修改
 db_session.query(Users).filter(Users.id == 3).update({"name":"alexDSB"}) # 更新id=3的数据
 db_session.commit()

 关闭连接
db_session.close()

增删改查
```

3.高级版查询

```python
from CreateDB import Users, School

# 1. 创建一个用户添加到数据库
# 创建连接
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:DragonFire@127.0.0.1:3306/dragon?charset=utf8",
                       )

# 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 查询数据表操作
"""
r1 = session.query(Users).all()
r2 = session.query(Users.name.label('xx'), Users.age).all()
r3 = session.query(Users).filter(Users.name == "alex").all()
r4 = session.query(Users).filter_by(name='alex').all()
r5 = session.query(Users).filter_by(name='alex').first()
r6 = session.query(Users).filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(Users.id).all()
r7 = session.query(Users).from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()
"""
# 筛选查询列
# user_list = db_session.query(Users.name).all()
# print(user_list) # [('alexDSB',), ('zhangsan',)] 虽然看到的是元祖,但是依然可以通过对象打点儿调用属性
# for row in user_list:
#     print(row.name)

# 别名映射  name as nick
# user_list = db_session.query(Users.name.label("nick")).all()
# print(user_list) # [('alexDSB',), ('zhangsan',)] 虽然看到的是元祖,但是依然可以通过对象打点儿调用属性
# for row in user_list:
#     print(row.nick) # 这里要写别名了

# 筛选条件格式
# user_list = db_session.query(Users).filter(Users.name == "alexDSB").all()
# user_list = db_session.query(Users).filter(Users.name == "alexDSB").first()
# user_list = db_session.query(Users).filter_by(name="alexDSB").first()
# for row in user_list:
#     print(row.nick)

# 复杂查询
# from sqlalchemy.sql import text
# user_list = db_session.query(Users).filter(text("id<:value and name=:name")).params(value=3,name="alexDSB")

# 查询语句
# from sqlalchemy.sql import text
# user_list = db_session.query(Users).filter(text("select * from users id<:value and name=:name")).params(value=3,name="alexDSB")

# 排序 :
# user_list = db_session.query(Users).order_by(Users.id).all()
# user_list = db_session.query(Users).order_by(Users.id.desc()).all()
# for row in user_list:
#     print(row.name,row.id)

#其他查询条件
"""
ret = session.query(Users).filter_by(name='alex').all()
ret = session.query(Users).filter(Users.id > 1, Users.name == 'eric').all()
ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'eric').all() # between 大于1小于3的
ret = session.query(Users).filter(Users.id.in_([1,3,4])).all() # in_([1,3,4]) 只查询id等于1,3,4的
ret = session.query(Users).filter(~Users.id.in_([1,3,4])).all() # ~xxxx.in_([1,3,4]) 查询不等于1,3,4的
ret = session.query(Users).filter(Users.id.in_(session.query(Users.id).filter_by(name='eric'))).all() 子查询
from sqlalchemy import and_, or_
ret = session.query(Users).filter(and_(Users.id > 3, Users.name == 'eric')).all()
ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric')).all()
ret = session.query(Users).filter(
    or_(
        Users.id < 2,
        and_(Users.name == 'eric', Users.id > 3),
        Users.extra != ""
    )).all()
# select * from users where id<2 or (name="eric" and id>3) or extra != "" 
"""

# 关闭连接
db_session.close()

高级版查询操作
```

4.高级版更新操作 

```
"""
db_session.query(Users).filter(Users.id > 0).update({"name" : "099"})
db_session.query(Users).filter(Users.id > 0).update({Users.name: Users.name + "099"}, synchronize_session=False)
db_session.query(Users).filter(Users.id > 0).update({"age": Users.age + 1}, synchronize_session="evaluate")
db_session.commit()
"""


```

5.扩展内容

```
# 通配符
ret = session.query(Users).filter(Users.name.like('e%')).all()
ret = session.query(Users).filter(~Users.name.like('e%')).all()

# 限制
ret = session.query(Users)[1:2]

# 排序
ret = session.query(Users).order_by(Users.name.desc()).all()
ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()

# 分组
from sqlalchemy.sql import func

ret = session.query(Users).group_by(Users.extra).all()
ret = session.query(
    func.max(Users.id),
    func.sum(Users.id),
    func.min(Users.id)).group_by(Users.name).all()

ret = session.query(
    func.max(Users.id),
    func.sum(Users.id),
    func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) >2).all()

排序分组选取通配符
```

### 一对一操作

创建表

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

#创建基类,相当于Django中的 models.Model,被各个数据表类所继承
Base = declarative_base()


# ##################### 多表示例 #########################
# 创建一张数据表
class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)


#  创建另一张数据表
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)

    author_id = Column(Integer,ForeignKey("author.id"))

    # relationshi 不会单独生成字段 ,只用于增加查询操作
    user = relationship("Author",backref="author2book") # backref 反向查找的名字




# 创建数据库链接
engine = create_engine(
        "mysql+pymysql://root:DragonFire@localhost:3306/dragon?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

# 通过Base.metadata找到所有继承 Base 的数据表class
Base.metadata.create_all(engine)

创建多表并建立关系
```

**2.增删改查**

```
from SQLAlchemy_ready.ss2_ForeignKey_relationship import Author, Book

# 1. 创建一个用户添加到数据库
# 创建连接
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:DragonFire@127.0.0.1:3306/dragon?charset=utf8",
                       )

# 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 1.增加 操作数据表
# 添加两个作者:
# db_session.add_all([
#     Author(name="alex"),
#     Author(name="yinwangba")
# ])
# db_session.commit()
# 添加一本书 jinpingmei 作者是 yinwangba
# author = db_session.query(Author).filter(Author.name == "yinwangba").first()
# db_session.add(Book(name="jinpingmei",author_id=author.id))
# db_session.commit()

# 2.查询所有数据,并显示作者名称,连表查询
# book_list = db_session.query(Book).all()
# for row in book_list:
#     print(row.name,row.author_id)

# book_list = db_session.query(Book.name.label("bname"),Author.name.label ("aname")).join(Author,Book.author_id == Author.id,isouter=True).all()
# print(book_list)
# for row in book_list:
#     print(row.aname,row.bname)

# 查询之relationship 快速连表
# 创建表的时候加入 relationship
#普通版添加
# obj = Author(name="yinwangba")
# db_session.add(obj)
# db_session.commit()
# print(obj.id,obj.name)
#
# obj_book = Book(name="jinpingmei",author_id=obj.id)
# db_session.add(obj_book)
# db_session.commit()
# obj = Author(name="yinwangba")

# relationship版 添加
# bobj = Book(name="jinpingmei",user=Author(name="yinwangba"))
# db_session.add(bobj)
# db_session.commit()

# 查询之relationship 快速连表
# book_list = db_session.query(Book).all()
# for row in book_list:
#     print(row.name,row.user.name)

# 查询作者的所有书籍
# obj = db_session.query(Author).filter(Author.name=="yinwangba").first()
# print(obj.author2book)

# 反向字段添加
# author_obj = Author(name="alex")
# author_obj.author2book = [Book(name="儒林外史之银林大战"),Book(name="邻家小妹妹")]
# db_session.add(author_obj)
# db_session.commit()

# 关闭连接
db_session.close()

增删改查
```

### 多对多

1.创建表

```
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import relationship

#创建基类,相当于Django中的 models.Model,被各个数据表类所继承
Base = declarative_base()

# 创建第三张表 Boys and Girls
class Hotel(Base):
    __tablename__ = "hotel"

    id = Column(Integer,primary_key=True)
    boy_id = Column(Integer,ForeignKey("boys.id"))
    girl_id = Column(Integer,ForeignKey("girls.id"))

# 创建一张数据表
class Boys(Base):
    __tablename__ = 'boys'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)

    # 创建于酒店的关系
    girls = relationship("Girls",secondary="hotel",backref="boys")

# 创建另一张数据表
class Girls(Base):
    __tablename__ = "girls"

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),index  =True)

    # 创建于酒店的关系
    # boy = relationship("Boys",secondary="hotel",backref="toHotel")









# 创建数据库链接
engine = create_engine(
        "mysql+pymysql://root:DragonFire@localhost:3306/dragon?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

# 通过Base.metadata找到所有继承 Base 的数据表class
Base.metadata.create_all(engine)


# SQLAlchemy数据表进行修改后,无法直接进行更新,只能删除表后进行操作,重新进行操作,
# 但Flask-SQLAlchemy + Flask-migrate + Flask-script 就可以实现 Django 的数据迁移 MakeMigration migrate

#

多对多关系建立
```

**2.操作**

```
from SQLAlchemy_ready.ss4_M2M import Girls, Boys,Hotel

# 1. 创建一个用户添加到数据库
# 创建连接
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:DragonFire@127.0.0.1:3306/dragon?charset=utf8")


# 创建数据表操作对象 sessionmaker
DB_session = sessionmaker(engine)
db_session = DB_session()

# 1.增加 操作数据表
# boy = Boys(name="jinwangba")
# boy.girls = [Girls(name="fengjie"),Girls(name="juaner")]
# db_session.add(boy)
# db_session.commit()

# 2.查询
# 使用relationship正向查询
# boy = db_session.query(Boys).first()
# print(boy.name,boy.girls[0].name)

# 使用relationship反向查询
# girls = db_session.query(Girls).first()
# print(girls.boys[0].name , girls.name)


# 关闭连接
db_session.close()

多对多操作
```

