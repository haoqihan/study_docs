---
title: SQLAlchemy的使用
date: 2019-01-15 15:48:22
tags: [sqlAlchemy]
categories: [数据库]
---

### 什么是sqlalchemy?

SQLAlchemy是[Python](http://baike.baidu.com/subview/21087/21087.htm)编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。 

### 连接数据库

首先需要导入 sqlalchemy 库，然后建立数据库连接，这里使用 `mysql`。通过`create_engine`方法进行 

```python
from sqlalchemy import create_engine
engine = create_engine("mysql://root:@localhost:3306/webpy?charset=utf8",encoding="utf-8", echo=True)
```

### 基本使用

```python
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
```

引用: https://github.com/michaelliao/learn-python3/blob/master/samples/db/do_sqlalchemy.py

