---
title: celery的基本使用
date: 2019-01-15 16:22:18
tags: [消息队列]
categories: [消息队列]
---

### celery是什么?

​	celery是一个基于python实现的模块,模块可以帮助我们实现任务管理

### 什么情况下使用celery?

一个请求的处理时间特别长,可以使用celery(例如:发送邮件,短信等)

### 安装celery

```shell
pip install celery
```

### 快速入门

#### 目录结构

```shqll
- celery_app
	-- __init__.py
	-- celeryconfig.py
	-- task1.py
	-- task2.py
--demo.py
```

__ init __.py

```python
from celery import Celery

app = Celery('demo') # demo名称,可以是任意修改
app.config_from_object('celery_app.celeryconfig')  # 通过celery实例加载配置模块

```

celeryconfig.py配置文件

```python
from datetime import timedelta

from celery.schedules import crontab
BROKER_URL = 'redis://localhost:6379/1'  # 设置broker存储的位置

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0' #设置backend的位置

CELERY_TIMEZONE = 'Asia/Shanghai'  # 设置时区
# UTC

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)


# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1':{
        'task':'celery_app.task1.add',
        'schedule': timedelta(seconds=10), # 每10秒执行一次
        'args':(2, 8)
    },
    'task2':{
        'task':'celery_app.task2.multiply',
        'schedule': crontab(hour=17,minute=27), # 每天的17点27分执行一次
        'args':(4,5)
    }
}
```

task1.py

```python
from celery_app import app

@app.task                 # 设置一个处理任务的函数
def add(x,y):
    return x + y
```

task2.py

```python
from celery_app import app


@app.task
def multiply(x , y):     # 设置第二个
    return x * y
```

demo.py

```python
# 发起任务
from celery_app import task1
from celery_app import task2

# 第一种 参数:args是存放数据   eta=datetime(2018, 4, 11, 2, 32, 0):可以设置定时任务
task1.add.apply_async() 
task1.add.delay(2,4)

xx = task2.multiply.delay(4,5) # 第二种 直接传入参数



# 获取结果
from celery.result import AsyncResult
from celery_app import app

res = AsyncResult(id=xx.id,app=app)
if res.ready():  # 判断结果是否返回
    return res.get()  # 返回的话把结果返回
```




















