基本配置
1、心跳注册
2、制作一个自环的环境
3、访问日志测试配置
4、信安日志测试配置

#### 心跳注册部分

##### DPI部分

```shell
# 心跳注册
# cnm 下
 manage platform ipver ipv4 ipaddress 10.105.139.118 port 14000
```

##### 接口机部分

```shell
# 配置CMP的心跳IP
# 第一步：进入数据库
mysql -urrot -p 密码

# 第二步：使用mp数据库，数据库操作必须以 ; 结尾
use mp； 

# 第三步：插入内容
insert into sys_service_port(id,name,ip_pri,port_pri,ip,port) VALUES ('1','ftp','10.105.139.118','21','10.105.139.118','21');
insert into sys_service_port(id,name,ip_pri,port_pri,ip,port) VALUES ('2','heartbeat','10.105.139.118','14000','10.105.139.118','14000');

# 第四步：查看是否插入成功
 select * from sys_service_port;
 
 # 第五步：修改状态
 UPDATE ne_register set valid=1;
UPDATE ne_register set negroup_id=1;

# 第六步：查看dpi是否注册成功，当status字段为1时，就成功了
select * from ne_register；

# 第七步：接口机连接数据库
# pm模式下
cmp-db host 10.105.139.118 port 3306 username root password byzoro dbname mp
# uc模式下
cmp-db host 10.105.139.118 port 3306 username root password byzoro dbname mp

# 第八步：查看是否配置成功，注释：如果没有看到，需要保存配置：save config
show running-config



# 注释：如果status没有为1，需要重启一下接口机试一下
cd /byzoro/os/bin   
killall *		# 杀死所有进程
 ./daemon		# 重启进程

```

#### 制作一个闭环环境

##### tilera 设备自环

###### DPI部分

```shell
# 第一步：端口网线或者光纤自环
# 第二步：DPI上查看up状态的端口
进入 mp下
show  interface all
# 第三步：查看真实网卡名称与软件定义网卡名称之间的对应关系
mp---debug模式下

dump dpintf-internal-name 
# 第四步：将自环的一个口通过ifconfig 强制up
# 第五步：看文档安装tcpreplay 软件

```

#### 访问日志测试

##### 接口机

######  第一步：创建一个SFTP

```shell
useradd sftptest
passwd sftptest
```

###### 第二步：配置访问日志绝对路径

```shell
# uc模式下
config scanlog path /home/sftptest/   # 配置访问日志路径
config filesize 30    # 配置访问日志文件大小，表示访问日志达到30M写文件
config filecycle 300  # 配置访问日志生产周期，表示达到300秒（5分钟）写文件
config company xxx     # 访问日志名字中有设备提供厂商

show running config    # 查看访问日志配置
config house_ip enable|disable  # 控制是否进行机房ip匹配，默认是关闭
show policy isms-ip-mapping     # 查看下发的ip段
```

###### 第三步：模拟cu下发策略

```shell
因为模拟测试，用python 脚本模拟CU下发策略，需要下发的策略如下
访问日志上报开关、访问日志上报策略、策略与机房绑定策略、DPI设备通用策略
```

###### 第四步：接口机查看下发的策略

```shell
# 1、DPI设备通用策略
# uc模式下
show policy isms-eu-comm 
# 结果
--------information of policy (isms-eu-comm)--------
***EU COMM POLICY INFO****
[DPI-Collection    types] : eu-dev
[DPI-Collection  devname] : byzoro
[DPI-Collection  sitename]: hzl
[DPI-Collection  house_id]: byzorodpi

# 2、 查看访问日志上报策略
# uc模式下
show policy isms-report 
# 结果：
--------information of policy (isms-report)--------
====== msg no(22) ======
===newest msg serialno : (4)===
--------------------------------
--------------------------------
EU isms traffic upload policy: msg_no       = 22
EU isms traffic upload policy: Info         = 1
EU isms traffic upload policy: scanlog flag = 1
EU isms traffic upload policy: bind valid   = 1
EU isms traffic upload policy: bind all-house
EU isms traffic upload policy: valid      = 0x03
EU isms traffic upload policy: pcktype    = 0x3
EU isms traffic upload policy: pcksubtype = 0xa0
EU isms traffic upload policy: servercnt  = 1
============[service 0]===========
EU isms traffic upload policy: iplength   = 4
EU isms traffic upload policy: destip     = 10.105.139.118
EU isms traffic upload policy: destport   = 22
EU isms traffic upload policy: username   = sftptest
EU isms traffic upload policy: password   = 12345678
====== [plcy-total-count : 1] ======

# 3、查看策略与机房绑定
# uc模式下
show policy isms-idc-bind 

# 结果
--------information of policy (isms-idc-bind)--------
========[report-policy]=========
bind_house_type :all-house
bind_msg_type   :11
bind_msg_no     :22
bind_house_cnt  :0
========[scanlog-policy]=========
bind_house_type :all-house
bind_msg_type   :15
bind_msg_no     :1
bind_house_cnt  :0

# 4. 查看访问日志开关策略
# uc模式下
show policy isms-scanlog 
# 结果
--------information of policy (isms-scanlog)--------
====== msg no(1) ======
===newest msg serialno : (4)===
 =========[MSG NO : 1]=======
 bind          : all-house
 scang_log status : open flag
====== [plcy-total-count : 1] ======
```

##### DPI部分

```shell
# DPI上查看下发的策略
# cp模式下
show rpt-plcy
# 结果
[Plcy          ID]: 17
[Plcy   Refer  ID]: "0"
[Cndt   Rcv   Cnt]: 0
[Cndt   Cur   Cnt]: 0
[UPLoad      Type]: "snap"
[UPLoad Sub  Type]: "snap_http"
[Template      ID]: 3
[Template   Index]: 0x202
[UPLoad      Freq]: 0(s)
[UPLoad      Size]: 0(B)
[UPLoad      Line]: 0
[UPLoad      Path]: "/home/testlog/"
[UPLoad  FP Index]: 0x14
[Exec Time  Index]: 0x0
[UPLoad Delimiter]: ""
[Upload    Field]: ""
[Stats    Object]: ""

# 查看访问日志策略加载
show config-info

[Company]: "IDC"
[Device Id]: "066"
[Scanlog Path]: "/home/sftptest/"
[Snap Path]: "/"
[Site Name]: "hzl"
[Monitor Priority]: "enable"

# 查看下发的ip段
show house_ip plcy

# DPI流量统计控制
trafficctrl_function enable | disable   进行控制

# DPI上报模板查询
show datarpt templt




# 安装知识库
/byzoro/version/knowledge/dpi  地址
放入：kb.build.20171115.pack 文件
重启会生成
kb.build.20171115.desc

# 回流
/byzoro/tcpdump 下
./tilera-tcpreplay -i gbe9 -p 100 /root/baowen/http.pcap # 回放报文
```



### 信安策略和日志

#### 接口机部分

```shell
# uc模式下
# 1.查看信安策略
show policy isms-security
===newest msg serialno : (1)===
msg_no 		: 1
command_id 	: 30303030303030303136
level 		: 272
info  		: 1
act  		: block
report  	: open
key[0]		: 榆林市疾病预防控制中心    # 关键字
protocol 	: tcp and udp
b_time		: 1969-12-31 19:00:01
e_time		: 2106-02-07 01:28:15
allhouse 	: 1
bind 		: yes
valid 		: 1
msg_serialno 	: 1

# 2.查看信安日志上报策略
# 在加载结果中pcktype必须为1，信安日志，pcksubtype必须为e0，表示是信安日志，而上报端口必须为60001，管控日志统一通过60001端口上报
show policy isms-report


```

#### DPI部分

```shell
# cp模式下
# 查看下发的策略
show ctrl-plcy

# 回流
/byzoro/tcpdump 下
./tilera-tcpreplay -i gbe9 -p 100 /root/baowen/http.pcap # 回放报文

```

### 快照

#### 注意

```shell
# 在下发快照策略的时候必须先下发
0x0b,0x0f,0x10,0xd1

```



```shell
# 接口机需要配置快照的上报路径
config snap path /home/sftptest/

```









 

