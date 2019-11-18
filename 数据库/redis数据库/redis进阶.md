### 什么是redis

**redis**是一个基于内存的高性能key-value**数据库**

### 2.redis的特点

**Redis本质**是一个key-value类型的数据库,就像memcached,整个数据库统统加载在内存中进行操作,定期通过异步把数据库数据push到硬盘上进行保存,因为是纯内存操作所以redis的性能非常出色,每秒可以处理10万次读写操作,是已知性能最快的key-value DB

Redis的出色之处不仅仅只有他的性能,Redis最大的魅力是支持多种数据结构,此外单个value的最大限制是1GB,不像memcached只能保存1MB的数据,因此redis可以用来实现很多有用的功能,**比如:用他的List来做FIFO双向链表实现一个轻量级的高性能消息队列服务**,**用他的set可以做高性能的tag系统等等**,另外Redis也可以对存入的key-value设置expire(过期)时间,因此也可以当做一个加强版的memcached来用.

**Redis主要缺点**是数据库容量受物理内存限制,不能做海量数据的高性能读写,因此它只适合在较小数据量的高性能操作和运算上

**PS----->memcached:**是一个高性能的分布式内存对象缓存系统，用于动态Web应用以减轻数据库负载。它通过在内存中缓存数据和对象来减少读取数据库的次数，从而提高动态、数据库驱动网站的速度。Memcached基于一个存储键/值对的[hashmap](https://baike.baidu.com/item/hashmap/1167707)。其[守护进程](https://baike.baidu.com/item/%E5%AE%88%E6%8A%A4%E8%BF%9B%E7%A8%8B/966835)（daemon ）是用[C](https://baike.baidu.com/item/C/7252092)写的，但是客户端可以用任何语言来编写，并通过memcached协议与守护进程通信。 

### 3.Redis支持的数据类型

Redis通过key-value的单值不同类型区分

- strings
- Lists
- sets
- sorted set
- hashes

### 4.为什么redis需要把所有数据放到内存中

redis为了达到最快的读写速度将数据都读到内存中,并通过异步的方式将数据写入磁盘,所以redis具有快速和数据持久化的特性,如果不将数据放在内存中,磁盘I/O速度会影响redis的性能,

如果设置最大使用的内存,则数据已有记录达到内存限值后不能继续插入新值

### 5.Redis是单进程单线程的

redis利用队列技术将并发访问变成为串行访问,消除了传统数据库串行控制开销

### 6.虚拟内存

当你的key很小而value很大时,使用vm的效果会比较好,因为这样节约内存比较大

当你的key不小时,可以考虑一些非常方法将很大的key变成value,比如你可以将key-value变成一个value

vm-max-threads这个参数,可以设置访问swap文件的线程数,设置最好不要超过机器的核数,如果设置为0,那么所有对swap文件的操作都是串行的.可能会造成比较长时间的延迟,但是对数据完整性有很好的保证. 

### 7.分布式

redis支持主从的模式,原则:master(控制)会将数据同步到slave,而slave不会讲数据同步到master,slave启动时会连接master来同步数据

这是一个典型的分布式读写分离模型,我们可以利用master来插入数据,slave提供检索服务,这样可以有效减少单个机器的并发访问数量

### 8.读写分离模型

通过增加slave DB的数量,读的性能可以线性增长,为了避免master DB的单点故障,集群一般都会采用两台master DB做双机热备所以整个集群的读和写的可用性都非常高

**读写分离的缺陷**:不管master还是slave,每个节点都必须保存完整的数据,如果在数据量很大的时候,集群的扩展能力还是受限于每个节点 的存储能力,而且对于write-intensive类型的应用,读写分离的架构并不合适

### 9.数据分片模型

为了解决读写分离模型的缺陷,可以将数据分片模型应用进来

可以将每个节点都看成独立的master,然后通过业务实现数据分片

结合上面两种模型,可以将每个master设计由一个master和多个slave组成的模型

### 10.Redis的回收策略

- volatile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最少使用的数据淘汰 
- volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰 
- volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰 
- allkeys-lru：从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰 
- allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰 
- no-enviction（驱逐）：禁止驱逐数据 

### 11.使用redis有哪些好处

1. 速度快，因为数据存在内存中，类似于HashMap，HashMap的优势就是查找和操作的时间复杂度都是O(1) 
2. 支持丰富数据类型，支持string，list，set，sorted set，hash 
3. 支持事务，操作都是原子性，所谓的原子性就是对数据的更改要么全部执行，要么全部不执行 
4. 丰富的特性：可用于缓存，消息，按key设置过期时间，过期后将会自动删除 

### 12.**redis相比memcached有哪些优势？**

1. memcached所有的值均是简单的字符串，redis作为其替代者，支持更为丰富的数据类型 
2. redis的速度比memcached快很多 
3. redis可以持久化其数据 

### 13.**redis常见性能问题和解决方案：**

1. Master最好不要做任何持久化工作，如RDB内存快照和AOF日志文件 
2. 如果数据比较重要，某个Slave开启AOF备份数据，策略设置为每秒同步一次 
3. 为了主从复制的速度和连接的稳定性，Master和Slave最好在同一个局域网内 
4. 尽量避免在压力很大的主库上增加从库 
5. 主从复制不要用图状结构，用单向链表结构更为稳定，即：Master <- Slave1 <- Slave2 <- Slave3... 

这样的结构方便解决单点故障问题，实现Slave对Master的替换。如果Master挂了，可以立刻启用Slave1做Master，其他不变 

### 14.**MySQL里有2000w数据，redis中只存20w的数据，如何保证redis中的数据都是热点数据**

相关知识：redis 内存数据集大小上升到一定大小的时候，就会施行数据淘汰策略。详情见 **redis的回收策略**

### 15.redis常见的性能问题有哪些?如何解决

1. Master写内存快照，save命令调度rdbSave函数，会阻塞主线程的工作，当快照比较大时对性能影响是非常大的，会间断性暂停服务，所以Master最好不要写内存快照。 
2. Master AOF持久化，如果不重写AOF文件，这个持久化方式对性能的影响是最小的，但是AOF文件会不断增大，AOF文件过大会影响Master重启的恢复速度。Master最好不要做任何持久化工作，包括内存快照和AOF日志文件，特别是不要启用内存快照做持久化,如果数据比较关键，某个Slave开启AOF备份数据，策略为每秒同步一次。 
3. Master调用BGREWRITEAOF重写AOF文件，AOF在重写的时候会占大量的CPU和内存资源，导致服务load过高，出现短暂服务暂停现象。 
4. Redis主从复制的性能问题，为了主从复制的速度和连接的稳定性，Slave和Master最好在同一个局域网内 

### 16.redis适合的场景

Redis最适合所有数据in-momory的场景，虽然Redis也提供持久化功能，但实际更多的是一个disk-backed的功能，跟传统意义上的持久化有比较大的差别，那么可能大家就会有疑问，似乎Redis更像一个加强版的Memcached，那么何时使用Memcached,何时使用Redis呢? 

1. Redis不仅仅支持简单的k/v类型的数据，同时还提供list，set，zset，hash等数据结构的存储。 
2. 、Redis支持数据的备份，即master-slave模式的数据备份。 
3. Redis支持数据的持久化，可以将内存中的数据保持在磁盘中，重启的时候可以再次加载进行使用。 

### 17、会话缓存（Session Cache）

最常用的一种使用Redis的情景是会话缓存（session cache）。用Redis缓存会话比其他存储（如Memcached）的优势在于：Redis提供持久化。当维护一个不是严格要求一致性的缓存时，如果用户的购物车信息全部丢失，大部分人都会不高兴的，现在，他们还会这样吗？

幸运的是，随着 Redis 这些年的改进，很容易找到怎么恰当的使用Redis来缓存会话的文档。甚至广为人知的商业平台Magento也提供Redis的插件。

### 18、全页缓存（FPC）

除基本的会话token之外，Redis还提供很简便的FPC平台。回到一致性问题，即使重启了Redis实例，因为有磁盘的持久化，用户也不会看到页面加载速度的下降，这是一个极大改进，类似[PHP](http://lib.csdn.net/base/php)本地FPC。

再次以Magento为例，Magento提供一个插件来使用Redis作为[全页缓存后端](https://github.com/colinmollenhour/Cm_Cache_Backend_Redis)。

此外，对WordPress的用户来说，Pantheon有一个非常好的插件  [wp-redis](https://wordpress.org/plugins/wp-redis/)，这个插件能帮助你以最快速度加载你曾浏览过的页面。

### 19、队列

Reids在内存存储引擎领域的一大优点是提供 list 和 set 操作，这使得Redis能作为一个很好的消息队列平台来使用。Redis作为队列使用的操作，就类似于本地程序语言（如[Python](http://lib.csdn.net/base/python)）对 list 的 push/pop 操作。

如果你快速的在Google中搜索“Redis queues”，你马上就能找到大量的开源项目，这些项目的目的就是利用Redis创建非常好的后端工具，以满足各种队列需求。例如，Celery有一个后台就是使用Redis作为broker，你可以从[这里](http://celery.readthedocs.org/en/latest/getting-started/brokers/redis.html)去查看。

### 20，排行榜/计数器

Redis在内存中对数字进行递增或递减的操作实现的非常好。集合（Set）和有序集合（Sorted Set）也使得我们在执行这些操作的时候变的非常简单，Redis只是正好提供了这两种数据结构。所以，我们要从排序集合中获取到排名最靠前的10个用户–我们称之为“user_scores”，我们只需要像下面一样执行即可：

当然，这是假定你是根据你用户的分数做递增的排序。如果你想返回用户及用户的分数，你需要这样执行：

ZRANGE user_scores 0 10 WITHSCORES



### 21、发布/订阅

最后（但肯定不是最不重要的）是Redis的发布/订阅功能。发布/订阅的使用场景确实非常多。我已看见人们在社交网络连接中使用，还可作为基于发布/订阅的脚本触发器，甚至用Redis的发布/订阅功能来建立聊天系统！（不，这是真的，你可以去核实）。

