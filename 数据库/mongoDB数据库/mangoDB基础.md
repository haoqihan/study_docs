---
title: mangoDB基础
date: 2019-01-14 22:39:24
tags: [MangoDB]
categories: [数据库]
---

## 数据库中的用法

### MangoDB的对应关系

引用了不存在的对象来创建改对象

```python
database  ------>  Database
table         ------->  Collection
字段         --------> Field
row         --------->  Document
```

### mangoDB增删改查

```sql
增:
    官方不推荐写法:
        db.users.insert([{}])
        db.users.insert({})
    官方支持写法
        db.users.insertMany([{'name':'ccc','age':88},{'name':'ddd','age':88}])
        db.users.insertOne({name:"xxx",age:"73"})
查:
    db.users.find({age:73,name:"xxx"})
    db.users.findOne({age:73})

改：MongoDB修改器 $set $unset:删除字段的
    db.users.updateOne({age:73},{$set:{age:74}})
    db.users.updateMany({age:74},{$set:{age:73}})
    
删:
    db.users.deleteOne({age:"84"})
    db.users.deleteMany({age:"84"})
```

### MongoDB的数据类型

```sql
Object ID ：Documents 自生成的 _id
String： 字符串，必须是utf-8
Boolean：布尔值，true 或者false (这里有坑哦~在Python中 True False 首字母大写)
Integer：整数 (Int32 Int64 你们就知道有个Int就行了,一般我们用Int32)
Double：浮点数 (没有float类型,所有小数都是Double)
Arrays：数组或者列表，多个值存储到一个键 (list哦,大Python中的List哦)
Object：如果你学过Python的话,那么这个概念特别好理解,就是Python中的字典,这个数据类型就是字典
Null：空数据类型 , 一个特殊的概念,None Null
Timestamp：时间戳
Date：存储当前日期或时间unix时间格式 (我们一般不用这个Date类型,时间戳可以秒杀一切时间类型)
```

### $关键字

```sql
修改器
        $set : 强制覆盖
        $unset : 删除字段
        $inc ：引用自增 $inc:{age:-1}

        $push append(7) db.sss.updateOne({name:"xxx"},{$push:{hobby_1:7}})
        $pull remove(1) db.sss.updateOne({name:"xxx"},{$pull:{hobby_1:1}})
        $pop  pop() db.sss.updateOne({name:"xxx"},{$pop:{hobby_1:1/-1}}) 1删除最后一个,-1代表删除第一个
    
    查询关键：
        $or  $or:[{age:1},{name:2}]
        $all {u_list:{$all:[321,123]}}
        $in  {age:{$in:[10,15]}}

    
    数学比较符：
        $lt {age:{$gt:10}}
        $lte
        $gt
        $gte
        $eq : 
        $ne {age:{$ne:15}}
        
    4. $
        ({name:"xxx","hobby.name":"个人计算机"},{$set:{"hobby.$.name":"PC"}})
```

### skip  limit  sort

```sql
sort:    sort({ age:1 / -1}) -1:倒序  1:正序    
skip:    skip(2) 跳过两条
limit： limit(2) 选取两条
优先级:
    1.sort 2.skip 3.limit
```

## python中使用MangoDB

#### 连接MongoDBClient

```python
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
```

#### 获取数据库

```python
db = Client.test_database
db = Client['test_database']
```

#### **获取Collection** 

Collection是存储在MongoDB中的一组文件，同获取database一样，你可以用点取属性的方式或者字典的方法获取： 

```python
collection = db.test_collection
collection = db['test_collection']
```

**其他操作和上面一样**