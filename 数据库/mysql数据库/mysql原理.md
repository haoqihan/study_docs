#### mysql基本架构示意图

![UTOOLS1572833144421.png](https://i.loli.net/2019/11/04/vJr2oFS73INUCTq.png)

### 一条sql语句是如何执行的

```shell
# 设置存储引擎的类型
engine=memory 

# 连接器
mysql -h$ip -P$port -u$user -p

# 查看链接
show processlist

# 使用查询缓存
query_cache_type

# Unknown column ‘k’ in ‘where clause 在哪个阶段报错的
答案:分析器。Oracle会在分析阶段判断语句是否正确，表是否存在，列是否存在等。猜测MySQL也这样。

```

### 一条更新语句是如何执行的

```shell
redo log（重做日志）
binlog（归档日志）
```

