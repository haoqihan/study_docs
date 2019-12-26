#### 设备注册

第一步：在DPI端进入cnm节点配置，输入

```shell
manage platform ipver ipv4 ipaddress 10.14.3.66 port 13000    # 端口必须是13000
```

第二步：DPI配置完成之后进入接口机的mysql数据库

```shell
# 进入数据库
mysql -uroot -p
# 激活mp表
use mp；
# 把注册DPI的valid和negroup都设置为1
UPDATE ne_register set negroup_id=1 and valid=1;
# 然后配置sys_service_port表
insert into sys_service_port(id,name,ip_pri,port_pri,ip,port) VALUES ('1','ftp','接口机IP','21','接口机IP','21');

insert into sys_service_port(id,name,ip_pri,port_pri,ip,port) VALUES ('2','heartbeat','接口机IP','14000','接口机IP','14000');
```

#### 策略下发配置

```shell
# 接口机

# 进入uc
cmp-db host xx.xx.xx.xx port 3306 username root password byzoro dbname mp
# 进入pm
cmp-db host xx.xx.xx.xx port 3306 username root password byzoro dbname mp

```

#### 排查流程

```shell
# 接口机下的/home/test/action_desc/目录，查看后缀，如果后缀是xml代表dpi没有下载策略，如果下载了，那么后缀就会变为.read
```

#### dpi设备型号与基本操作命令

```shell
# 抓包命令
# 方法一
# 使用场景
当下发策略之后，无封堵效果，需要查看流量中是否满足策略里包所含的条件时可以在cp节点debug模式下测使用sniffer 命令来进行抓包。
# 使用方法
在cp节点debug模式下输入：sniffer  filter  ip srcip 0.0.0.0 dstip 0.0.0.0
设置抓包的会话数大小，然后使用 sniffer start ip 命令开始抓包
抓包完成之后使用 sniffer stop 命令来进行停止抓包，
停止抓包后就会在底层/byzoro/pcap/目录下产生一个包文件
	
# 方法2
# 使用场景
当需要抓链路原始流量的时候，可以在底层通过tcpdump命令来抓取
# 使用方法
首先进入/run/os/bin/ 目录，输入killall * 来杀死设备进程，
然后使用ifconfig xgbe1 up来将所要抓取流量的端口进行强制up，
最后输入tcpdump  -s 0 -i xgbe1 -w 111.pcap命令来进行抓取端口的原始报文，
抓取完成之后使用ctrl+z来停止抓包。
```

#### 设备流量大小计算方法

```shell
# 计算公式
（第二次查看流量的字节数-首次查看流量的字节数）*8 /1024/1024/1024/60=每秒经过设备流量的大小

# 查看方法
在mp节点debug模式下输入 show mpipe-stat xgbe1 来进行查看进入设备总流量的字节数

```

#### 查看设备常用命令

```shell
# mp下
# 查看内存利用率
show memusage
# 查看设备硬盘的使用率
show diskusage
# 查看设备cpu使用率
show cpuusage

# debug
# 查看设备监听的端口状态
show netstat info
```

#### 信安功能

##### 服务端查看策略

```shell
#uc
show policy isms-scanlog 
# 查看cu下发的访问日志开关策略中最主要包含绑定机房个数，机房的id以及日志开关是否开启，此策略需要下发绑定策略才会是open flag状态，没有的话则是close flag状态


# 查看cu下发的访问日志绑定策略
show policy isms-idc-bind
# 查看cu下发的访问日志上报策略
# 包含：策略号，机房编号，当前流所属包类型，当前流所属包子类型，上报服务器数量，ip长度，上报的目的ip地址，上报的目的ip端口，上报服务器的账号和密码
show policy isms-report

# 查看cu下发的通用信息参数策略
show policy isms-eu-comm 
# 包含：设备编号，机房ID，站点名称等

# 查看信息安全策略
show policy isms-security 


# 计数
show statistic summary

# 查看快照上报策略
show polic isms-report

```

#### DPI查看策略

```shell
# cp
# 查看信安日志上报策略
show rpt-plcy 

[Plcy          ID]: 1  	# 
[Plcy   Refer  ID]: "0"  # 
[Cndt   Rcv   Cnt]: 0
[Cndt   Cur   Cnt]: 0
[UPLoad      Type]: "xdr"    # 上报类型
[UPLoad Sub  Type]: "xdr_acs" # 上报子类型
[Template      ID]: 2         # 模板ID
[Template   Index]: 0x1       # 
[UPLoad      Freq]: 300(s)    # 上报的周期
[UPLoad      Size]: 31457280(B) # 上报的大小
[UPLoad      Line]: 0 
[UPLoad      Path]: "/"     # 上报路径
[UPLoad  FP Index]: 0x1
[Exec Time  Index]: 0x0
[UPLoad Delimiter]: "|"
[Upload    Field]: "room_name|src_ip_str|dst_ip_str|l4_proto|src_port|dst_port|host|url|ssn_duration|access_time"
[Stats    Object]: ""


# 查看机房详细
 show config-info 
 
[Company]: "IDC"     # 机房名称
[Device Id]: "066"   # 机房ID
[Scanlog Path]: "/"  # 访问日志上报路径
[Snap Path]: "/"     # 快照的上报路径
[Site Name]: "hzl"
[Monitor Priority]: "enable"


# 查看信息安全策略
show ctrl-plcy 




```

#### 统计计数查看

```shell

```

#### 访问日志本地备份留存

```shell
功能开关： access_log backup (enable|disable)
日志数据的备份在/tmp目录下 accessLogBuckupData.backup
日志名称的备份在/tmp下 accessLogBuckupName.backup
# 注意：此功能基于upload-filter-ip先配置的，另外由于比较占用空间，建议使用完毕，将此文件删除
```

#### 信安日志备份

```shell
1.开启管控日志入库功能
在cmp有管控备份功能，将原始数据写入数据库
在
```



```shell
=========daemon===========
=========sysaux===========
** 0000000025242492 	 TASKSTS_SYSAUX_MAINLOOP
=========mp===============
** 0000000000025374 	 TASKSTS_MP_MAINLOOP
=========cp===============
** 0000000000025375 	 TASKSTS_CP_MAINLOOP
** 0000000000000350 	 TASKSTS_CP_DYNAMIC_GET_FTP_ERR
=========cnm===============
** 0000000000000005 	 [event] connect db error times
=========nsm===============
** 0000000000025367 	 TASKSTS_MAINLOOP
** 0000000000507422 	 TASKSTS_PLCY_STORAGE
** 0000000000000008 	 TASKSTS_CONNECT_DB_FAIL
** 0000000001014607 	 TASKSTS_ISMSLOG_STORAGE
** 0000000000050793 	 Scan state file dir times 
** 0000000000050793 	 Not get state file from dir times
** 0000000000497272 	 TASKSTS_CNM_GRADE_MAINLOOP
** 0000000000532916 	 TASKSTS_CNM_GRADE_FILE_MAINLOOP
** 0000000000126813 	 TASKSTS_CNM_GRADE_TABLE_MAINLOOP
** 0000000000000002 	 TASKSTS_CNM_ISMS_BIND_CONNECT_MYSQL_ERR
** 0000000000025364 	 TASKSTS_CNM_STORAGE_CYCLE_MAINLOOP
** 0000000000000001 	 TASKSTS_CNM_STORAGE_CYCLE_CONNECT_MYSQL_ERR
** 0000000000126866 	 TASKSTS_CNM_BUSI_OPERATE_MAINLOOP
** 0000000000126882 	 TASKSTS_CNM_BUSI_ANALYSIS_MAINLOOP
** 0000000000000212 	 TASKSTS_CNM_BUSI_DPI_VERSION_FILE_COUNT
** 0000000000253771 	 TASKSTS_NSM_BUSINESS_FILE_UPDATE_MAINLOOP
** 0000000000507544 	 TASKSTS_NSM_FTP_SERVER_NO_SET
=========pm===============
** 0000000000226584 	 TASKSTS_PM_NEGROUP_SYNC_MAINLOOP
** 0000000000226034 	 TASKSTS_PM_MSG_CHECK_MAINLOOP
** 0000000000253768 	 TASKSTS_PM_FILE_CREATE_MAINLOOP
** 0000000000000726 	 connect local db fail
** 0000000000000001 	 get policy change room id cnt
** 0000000000000001 	 insert default negroup success
** 0000000000000001 	 NEGROUP_INSERT_NEGROUP_ROOM_TBL_SUC
** 0000000000000001 	 create report plcy file success
** 0000000000000001 	 create control plcy file success
** 0000000000000001 	 create ssn filter plcy file success
** 0000000000000001 	 create mirror plcy file success
** 0000000000000001 	 create basic info file success
** 0000000000000001 	 create report template file success
** 0000000000000001 	 create link info file success
** 0000000000000001 	 create iplib file success
** 0000000000000001 	 create usergroup file success
** 0000000000000001 	 create weblib file success
** 0000000000000001 	 create config file success
** 0000000000000001 	 compress file cnt
** 0000000000000001 	 upload file success
** 0000000000000001 	 update plcy sync time success
** 0000000000000001 	 create house ip plcy file success
** 0000000000000001 	 FILE_CREATE_CTROL_ACK_FILE_SUCCESS
=========ismsud===============
** 0000000001015080 	 TASKSTS_ISMSUD_MAINLOOP
** 0000000000025375 	 TASKSTS_ISMSUD_CHECK_MAINLOOP
=========dpiud===============
** 0000000000025375 	 TASKSTS_DPIUD_MAINLOOP
=========uc===============
** 0000000000025374 	 TASKSTS_UC_MAINLOOP
** 0000000000253711 	 TASKSTS_UC_PLCY_STORAGE
** 0000000025242953 	 TASKSTS_UC_PLCY_PARSER
** 0000000000000001 	 recv eu-common-policy msg from CU
** 0000000000000002 	 recv isms-idc-bind msg from CU
** 0000000000000001 	 recv isms-scan-policy msg from CU
** 0000000000000001 	 recv isms-traffic-upload msg from CU
** 0000000000253778 	 CP_STAT_EPOLL_WAIT_ISMS_LOOP
** 0000000000253765 	 CP_STAT_EPOLL_WAIT_DPI_LOOP
** 0000000000000001 	 refresh plcy cnt
** 0000000000000001 	 insert iplib table cnt
** 0000000000000001 	 insert weblib table cnt
** 0000000000000001 	 insert report plcy table cnt
** 0000000000000001 	 insert control plcy table cnt
** 0000000000000001 	 insert mirror plcy table cnt
** 0000000000000001 	 insert report template table success
** 0000000000000001 	 insert report template plcygroup table success
** 0000000000000001 	 insert basic info table success
** 0000000000000001 	 insert plcygruop room table success
** 0000000000000001 	 insert plcygroup table success
** 0000000000000001 	 insert config table success
** 0000000000000001 	 insert dpi ssn filter table success
** 0000000000000001 	 insert dpi ssn filter port table success
** 0000000000253765 	 TASKSTS_UC_STATUS_MAINLOOP
** 0000000000194568 	 TASKSTS_UC_MONITOR_ISMS_RPT_ALARM_MAINLOOP
** 0000000000000555 	 UC_MONITOR_ISMS_RPT_CONNECT_LOCAL_DB_FAIL_TIMES
** 0000000000025374 	 TASKSTS_UC_HOUSE_IP_HANDLE
** 0000000000000001 	 UC_INSERT_HOUSE_INFO_TABLE_SUCCESS
** 0000000000253765 	 TASKSTS_UC_RECV_CMD_SERVER_MAINLOOP
=========ismslog===============
** 0000000001015058 	 TASKSTS_ISMSLOG_MAINLOOP
** 0000000000050798 	 TASTSTS_ISMSLOG_SCAN_MAINLOOP
=========flowstats===============
** 0000000050483881 	 TASKSTS_FLOWSTATS_MAINLOOP
** 0000000025187287 	 TASKSTS_FLOWSTATS_OPN_STATS_ZERO
** 0000000025185863 	 TASKSTS_FLOWSTATS_GEN_STATS_ZERO
** 0000000025188598 	 TASKSTS_FLOWSTATS_WEB_STATS_ZERO
** 0000000025188139 	 TASKSTS_FLOWSTATS_DIREC_STATS_ZERO
=========syslog===============
** 0000000000025375 	 TASKSTS_SYSLOG_MAINLOOP
=========du===============
** 0000000025292283 	 TASKSTS_DU_MAINLOOP
=========du_upload_0===============
** 0000000000050797 	 TASKSTS_DU_UPLOAD_MAINLOOP
=========du_upload_1===============
** 0000000000050797 	 TASKSTS_DU_UPLOAD_MAINLOOP
=========du_upload_2===============
** 0000000000050797 	 TASKSTS_DU_UPLOAD_MAINLOOP
```

