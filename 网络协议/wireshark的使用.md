wireshark过滤器

- 捕获过滤器
  - 用于减少抓取的报文体积
  - 使用BPF语法，功能相对有限
- 显示过滤器
  - 对已经抓取到的我报文过滤显示
  - 功能强大

BPF 过滤器：Wireshark 捕获过滤器

• Berkeley Packet Filter，在设备驱动级别提供抓包过滤接口，多数抓包工具都支持
此语法
• expression 表达式：由多个原语组成

Expression 表达式

- primitives 原语：由名称或数字，以及描述它的多个限定词组成
- qualifiers 限定词
  - Type：设置数字或者名称所指示类型，例如 host www.baidu.com
  - Dir：设置网络出入方向，例如 dst port 80
  - Proto：指定协议类型，例如 udp
  - 其他
-  原语运算符
  -  与：&& 或者 and
  - 或：|| 或者 or
  - 非：! 或者 not

```shell
# 例子：src or dst portrange 6000-8000 && tcp or ip6
```

### 限定词

Type：设置数字或者名称所指示类型

- host、port
- net，设定子网 net 192.168.0.0 mask 255.255.255.0 等价于 net 192.168.0.0/24
- portrange，设置端口范围，例如 portrange 6000-8000

Dir：设置网络出入方向

- src（源端口） 、dst（目的端口）、src or dst 、src and dst（源和目的都得是这样）
- ra、ta、addr1、addr2、addr3、addr4（仅对 IEEE 802.11 Wireless LAN 有效）

Proto：指定协议类型

- ether、fddi、tr、 wlan、 ip、 ip6、 arp、 rarp、 decnet、 tcp、udp、icmp、igmp、icmp、igrp、pim、ah、esp、vrrp

其他

- gateway：指明网关 IP 地址，等价于 ether host ehost and not host host
- broadcast：广播报文，例如 ether broadcast 或者 ip broadcast
- multicast：多播报文，例如 ip multicast 或者 ip6 multicast
- ess, greater：小于或者大于

```shell
port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420
```

显示过滤器的过滤属性

- 任何在报文细节面板中解析出的字段名，都可以作为过滤属性
- 在视图->内部->支持的协议面板里，可以看到各字段名对应的属性名
  - 例如，在报文细节面板中 TCP 协议头中的 Source Port，对应着过滤属性为 tcp.srcport

过滤值比较符号

| 英文        | 符号 | 描述及示例                        |
| ----------- | ---- | --------------------------------- |
| eq          | ==   | 等于.ip.src == 10.0.0.5           |
| ne          | !=   | 不等于于. ip.src!=10.0.0.5        |
| gt          | >    | 大于. frame.len > 10              |
| lt          | <    | 小于. frame.len < 12              |
| ge          | >=   | 大于等于. frame.len ge 0x100      |
| le          | <=   | 小于等于. frame.len ⇐ 0x20        |
| contains    |      | 包含. sip.To contains "a1762"     |
| matches     | ~    | 正则匹配.host matches "acme\.(org |
| bitwise_and | &    | 位与操作. tcp.flags & 0x02        |

过滤值类型

- Unsigned integer：无符号整型，例如 ip.len le 1500
- Signed integer：有符号整型
-  Boolean：布尔值，例如 tcp.flags.syn
- Ethernet address：以:、-或者.分隔的 6 字节地址，例如 eth.dst == ff:ff:ff:ff:ff:ff
-  IPv4 address：例如 ip.addr == 192.168.0.1
-  IPv6 address：例如 ipv6.addr == ::1
- Text string：例如 http.request.uri == "https://www.wireshark.org/"

多个表达式间的组合

| 英文 | 符号 | 意义及示例                                                   |
| ---- | ---- | ------------------------------------------------------------ |
| and  | &&   | AND逻辑与. ip.src==10.0.0.5 and tcp.flags.fin                |
| or   | \|\| | OR 逻辑或. ip.scr==10.0.0.5 or ip.src==192.1.1.1             |
| xor  | ^^   | XOR逻辑异或. tr.dst[0:3] == 0.6.29 xor tr.src[0:3] == 0.6.29 |
| not  | !    | NOT 逻辑非. not llc                                          |
| […]  |      | 见 Slice 切片操作符.                                         |
| in   |      | 见集合操作符                                                 |

其他常用操作符

- 大括号{}集合操作符
  - 例如 tcp.port in {443 4430..4434} ，实际等价于 tcp.port == 443 || (tcp.port >= 4430 && tcp.port ⇐ 4434)
- 中括号[]Slice 切片操作符
  - [n:m]表示 n 是起始偏移量，m 是切片长度
  - eth.src[0:3] == 00:00:83
- [n-m]表示 n 是起始偏移量，m 是截止偏移量
  - eth.src[1-2] == 00:83
- [:m]表示从开始处至 m 截止偏移量
  - eth.src[:4] == 00:00:83:00
-  [m:]表示 m 是起始偏移量，至字段结尾
  -  eth.src[4:] == 20:20
-  [m]表示取偏移量 m 处的字节
  -  eth.src[2] == 83
-  [,]使用逗号分隔时，允许以上方式同时出现
  -  eth.src[0:3,1-2,:4,4:,2] ==00:00:83:00:83:00:00:83:00:20:20:83

可用函数

| 函数   | 意义                                               |
| ------ | -------------------------------------------------- |
| upper  | Converts a string field to uppercase               |
| lower  | Converts a string field to lowercase               |
| len    | Returns the byte length of a string or bytes field |
| count  | Returns the number of field occurrences in a frame |
| string | Converts a non-string field to a string            |



