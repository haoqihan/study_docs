#### kafka概念解析

```shell
`producer` :消息和数据的生产者，向kafka的一个topic发布消息的进程、代码、服务
`Consumer`： 消息和数据的消费者，订阅数据（Topic）并且处理其发布的消息的进程、代码、服务
`Consumer Group`：逻辑概念，对同一个topic，会广播给不同的group，一个group中，只有一个consumer可以消费该信息
`broker`：物理概念，kafka集群中每个kafka节点
`Topic`：逻辑概念，kafka消息的类别，对数据进行区分，隔离
`Partition`：物理概念，kafka下数据存储的接班单元，一个Topic的数据，会分散存储到多个Partition，每个Partition是有序的
`Replication`：同一个Partition下可能会有多个Replica，多个Replica之间是一样的
`Replication Leader`：一个Partition的多个Replica上，需要个leader负责该Partition与Produce和consumer交互

`ReplicaManager`:负责观念里当前broker所有分区和副本的信息，处理KafkaController发起的一些请求，副本状态的切换、添加、读取消息
```

##### Partition

```shell
- 每一个Topic被切分为多个Partitions
- 消费者数目小于或等于Partition的数目
- Broker Group中的每一个Broker保存Topic的一个或多个Partitions
- Consumer Group 中仅有一个Consumer读取Topic的一个或多个Partitions，并且是唯一的Consumer
```

##### Replication

```shell
当集群中有Broker挂掉的情况，系统可以主动地使用Replicas提供服务
系统默认设置每一个Topic的replication系数为1，可以在创建Topic时单独设置

Replcation的基本单位是Topic的Partition
所有的读和写都是从Leader进，Followers只是做备份
Follower必须能及时复制Leader的数据
增加容错性和可扩展性
```

#### kafka结构设计

#### kafka特点

分布式

- 多分区
- 多副本
- 多订阅者
- 基于zookeeper调度

高性能

- 高吞吐量
- 低延迟
- 高并发
- 时间复杂度O(1)

持久性与扩展性

- 数据可持久化
- 容错性
- 支持在线水平扩展
- 消息自动平衡

#### kafka场景及应用

- 消息队列
- 行为跟踪
- 云数据监控
- 日志收集
- 流处理
- 事件源
- 持久性日志（Commit log）

#### kafka高级特性







