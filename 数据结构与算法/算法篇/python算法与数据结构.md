#### collections模块

##### namedtuple（）   可以使用名称访问tuple

```python
import collections
point = collections.namedtuple('porint','x,y')
p = point(1,2)
print(p.x)
```

##### deque（）         双端队列

```python
import collections           
de = collections.deque()
de.append(1)
de.appendleft(2)
de.pop()
de.popleft()
```

##### counter（）       计数器

```python
import collections  
c= collections.Counter('sadsafdsjfhdgjhdjfgbdfjbjvkdhf')
print(c)
```

##### ordereDict         有序字典

```python
import collections 
dic = collections.OrderedDict()
dic['1'] = 1
dic['2'] = 2
print(dic)
```

##### defaultdict         给dict做一个初始化

```python
import collections 
dd = collections.defaultdict(int)
dd['a'] += 1
print(dd)
```

#### python dict底层结构

- dict 底层使用哈希表
- 为了快速查找使用哈希表作为底层结构
- 哈希表平均查找时间复杂度O(1)
- cpython 解释器使用二次探查解决哈希冲突
  - 解决哈希冲突：
    - 链接法
      - 元素key冲突之后使用一个链表，填充形同key的元素
    - 探查法（开放寻址法） 
      - 探查法又分为：线性探查和二次探查等
      - 开放寻址法是冲突之后根据一种方式（二次探查）寻找下一个可用的槽
      - cpython使用的是二次探查的
- 哈希表扩容

#### python的list和tuple的区别

- 都是线性结构，支持下标访问
- list是可变对象，tuple保存的引用不可变
  - 保存引用不可变是指你没法替换掉这个对象，但是如果对象本身是一个可变对象，是可以修改这个引用指向的可变对象的
- list 没法作为字典的key，tuple可以（可变对象不可hash）

#### LRUCache

- least-Recently-Used 替换掉最近最少使用的对象
-  缓存剔除策略，当缓存空间不够用的时候，需要一种方式剔除key
- 常见的有LRU LFU
- LRU通过使用一个循环双端队列不断把最新访问的key放在表头实现

#### 实现LRUCache

- 字典用来缓存，循环双端链表用来记录访问顺序
- 利用python内置的dict+collections.OrderedDict（）实现
- dict 用来当做k、v键值对的缓存
- OrderedDict 用来实现最新最近访问的key

#### 算法常考题

- 排序+查找，重中之重
-  常考排序算法：冒泡排序，快速排序，归并排序，堆排序
- 线性查找+二分查找
- 能独立实现代码（手写） 能够分析时间空间复杂度

#### python数据结构常考题

##### python web后端常考数据结构

- 常见的数据结构链表，队列，栈，二叉树，堆
- 使用内置数据结构实现高级数据结构，比如内置的list，deque实现栈

![](https://github.com/haoqihan/gallery/blob/master/python%E9%9D%A2%E8%AF%95/%E5%B8%B8%E8%A7%81%E7%9A%84%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%92%8C%E7%AE%97%E6%B3%95.png?raw=true)

![](https://github.com/haoqihan/gallery/blob/master/python%E9%9D%A2%E8%AF%95/%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E7%A9%BA%E5%A4%8D%E6%9D%82%E5%BA%A6.png?raw=true)

##### 链表

-  链表有单链表，双链表，循环双链表
- 如何使用python来标示链表结构
- 实现链表常见操作，比如插入节点，反转链表，合并多个链表等
- 链表涉及到指针操作比较复杂，容易出错，经常用做考题
- 熟悉链表的定义和常用操作
- 常考题：删除一个链表节点
- 常考题：合并两个有序链表
- 常考题：反转一个链表

##### 队列

- 队列（queue） 是先进先出结构
- 实现队列的apend和pop操作，如何做到先进先出
- 使用python的list或者collections.deque实现队列
- 常考题：用栈实现一个队列

##### 栈

- 栈（stack） 是后进先出
- 实现栈的push和pop操作，如何实现
- 同样使用python的list或者collections.deque实现栈
- 常考题：用队列实现一个栈

##### 字典和集合

- python dict、set底层都是哈希表
- 哈希表的实现原理，底层就是一个数组
- 根据哈希函数快速定位一个元素，平均查找O（1）
- 不断加入元素会引起哈希表重新开辟空间，拷贝之前元素到新的数组

##### 二叉树

- 先序，中序，后序遍历
- 先序：先处理根，之后是左子树，然后是右子树
- 中序：先处理左子树，然后是根，然后是右子树
- 后序：先处理左子树，然后是右子树，最后是根
- 二叉树涉及到递归和指针操作，常结合递归考察
- 二叉树的操作很多可以用递归方式解决，不了解递归会比较吃力
- 常考题：二叉树的镜像
- 常考题：如何层序便利二叉树（广度优先）

##### 堆

- 堆其实就是一个完全二叉树，有最大堆和最小堆
- 最大堆：对于每个非叶子节点v，v的值都比他的两个孩子大
- 最小堆：对于每个非叶子节点v，v的值都比他的两个孩子小
- 最大堆支持每次pop操作获取最大的元素，最小堆获取最小元素
-  堆的常考题基本围绕在合并多个有序（数组，链表）；topk问题
- 理解堆的概念，堆是完全二叉树，有最大堆和最小堆
- 会使用python内置的heapq模块实现堆的操作

##### 字符串

- 反转一个字符串
- 判断一个数字是否是回环数字