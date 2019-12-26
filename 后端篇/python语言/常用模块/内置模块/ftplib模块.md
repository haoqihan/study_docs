### ftplib模块的使用

#### ftplib.FTP的参数

| 参数           | 方法                                         |
| -------------- | -------------------------------------------- |
| host           | 调用connect(host)方法                        |
| user           | 调用login(user, passwd, acct)方法            |
| timeout        | 超时参数，若不指定则应用全局超时参数         |
| source_address | 二元组(host, port)，连接前绑定的socket源地址 |

#### ftplib.FTP的方法

| 方法                                                         | 参数                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| FTP.**set_debuglevel**(*level*)                              | `0`：默认，无调试输出；`1`：中等调试输出；`2`：最大量 调试输出 | 该方法用来控制调试输出的量                                   |
| FTP.**connect**(*host='', port=0, timeout=None, source_address=None*) | `host`：主机地址；`port`:根据FTP协议默认端口为`21`；`timeout`：若不指定则使用`全局超时参数` | 用于链接FTP服务器，链接成功后无需再调用                      |
| FTP.**login**(*user='anonymous', passwd='', acct=''*)        | 参数指定用户名和密码，若未指定则匿名访问。`user：'anonymous'，passwd：'anonymous@'` | 只有在链接FTP服务器时用以验证使用                            |
| FTP.**abort**()                                              | 无参数                                                       | 中断文件传输操作，不一定管用，尝试而已                       |
| FTP.**getwelcome**()                                         | 无参数                                                       | 链接成功返回“welcome”信息                                    |
| FTP.**sendcmd**(*cmd*)                                       |                                                              | 发送简单命令给服务器，并返回相应字符串                       |
| FTP.**voidcmd**(*cmd*)                                       |                                                              | 发送简单命令，并处理响应，若响应时成功码，啥也不返回，否则raise `error_replly` |
| FTP.**retrbinary**(*cmd, callback, blocksize=8192, rest=None*) | `cmd`：RETR命令，`callback`：获取的数据块将要调用的函数，`blocksize`：数据块的最大尺寸，`rest`： | 以`BINARY模式`获取文件，                                     |
| FTP.**retrlines**(*cmd, callback=None*)                      | `cmd`：`RETR`命令                                            | 以`ASCII`模式获取文件或者文件夹列表                          |
| FTP.**set_pasv**(*val*)                                      | `true`：允许被动模式，`false`：禁用被动模式。默认允许        | 允许或者禁用被动模式                                         |
| FTP.**storbinary**(*cmd, fp, blocksize=8192, callback=None, rest=None*) | `cmd`：合适的`STOR`命令。`fp`：文件对象，以`read（）`方法读取文件直到EOF，以供存储。`blocksize`：数据块大小。`callback`：对数据块进行处理的方法。`rest`： | 以`BINARY`模式存储文件                                       |
| FTP.**storlines**(*cmd, fp, callback=None*)                  | `cmd`：合适的`STOR`命令。`fp`：文件对象，以`readline（）`方法读取文件直到EOF，以供存储。`blocksize`：数据块大小。`callback`：对数据块进行处理的方法。`rest`： | 以`ASCII`模式存储文件                                        |
| FTP.**transfercmd**(*cmd, rest=None*)                        | cmd：传输命令，rest：REST命令                                | 开启数据连接，`主动模式`下发送`EPRT`或者`PORT`命令，并通过cmd发送传输命令，接受连接，`被动模式`下发送`EPSV`或者`PASV`命令，连接服务器并通过cmd发送传输命令。两种模式下都要返回`socket套接字` |
| FTP.**ntransfercmd**(*cmd, rest=None*)                       |                                                              | 返回一个包含数据连接和期望数据大小的元组                     |
| FTP.**mlsd**(*path="", facts=[]*)                            | `path`：文件夹路径，`facts`：期望信息字段列表                | 用`MSLD`命令获取文件下的文件信息列表，返回包含文件名称和对应信息的元组，其中部分期望信息可能未获得服务器允许 |
| FTP.**nlst**(*argument[, ...]*)                              | `argument`：文件夹路径                                       | 使用`NLST`命令获取文件夹下的文件名称列表                     |
| FTP.**dir**(*argument[, ...]*)                               | `argument`：文件夹路径                                       | 使用`LIST`命令获取某路径下的文件夹列表，默认为当前目录       |
| FTP.**rename**(*fromname, toname*)                           | `fromname`：旧名称；`toname`：新名称                         | 修改文件名称                                                 |
| FTP.**delete**(*filename)*                                   | `filename`：文件名                                           | 移除服务器中的某文件，若成功返回`响应文本`，否则返回`error_perm`（许可错误） 或 `error_reply`（其他错误） |
| FTP.**cwd**(*pathname*)                                      | `pathname`：文件夹路径                                       | 设置当前文件夹                                               |
| FTP.**mkd**(*pathname*)                                      | `pathname`：文件夹路径                                       | 服务器中新建文件夹                                           |
| FTP.**pwd**()                                                |                                                              | 返回当前文件夹的路径                                         |
| FTP.**rmd**(*dirname*)                                       | `dirname`：文件夹名称                                        | 移除某个文件夹                                               |
| FTP.**size**(*filename*)                                     | `filename`：文件名                                           | 请求文件大小，若请求成功则返回整数，否则返回None；该命令非标准命令，但很多服务器支持 |
| FTP.**quit**()                                               | 无参数                                                       | 向服务器发送`QUIT`命令后，关闭连接，若服务器无法识别该命令，会响应错误 |
| FTP.**close**()                                              | 无参数                                                       | 单方面关闭连接，无法重复关闭连接                             |

#### class ftplib.FTP_TLS(host='', user='', passwd='', acct='', keyfile=None, certfile=None, context=None, timeout=None, source_address=None)

该类是FTP类的子类，自3.2版本后增加了tls安全传输层协议，一下是该类的方法说明

| 方法                  | 说明                                                    |
| --------------------- | ------------------------------------------------------- |
| FTP_TLS.ssl_version() | 使用的SSL的版本                                         |
| FTP_TLS.auth()        | 使用TLS或者SSL建立安全控制链接，取决于ssl_version()方法 |
| FTP_TLS.ccc()         |                                                         |
| FTP_TLS.prot_p()      | 建立安全的数据连接                                      |
| FTP_TLS.prot_c()      | 建立明文数据连接                                        |
|                       |                                                         |

#### FTP有两种传输模式：ASCII传输模式和BINARY传输模式。

ASCII传输模式：
该方式可以根据服务器系统对文件进行自动调整，将原始文件的回车换行转换为系统对应的回车字符，比如Unix下是\n,Windows下是\r\n，Mac下是\r。CGI脚本和普通HTML文件（或其他文本文件）用ASCII模式上传，而其他的一些文件则使用二进制传输模式。
BINARY传输模式：
在二进制传输中，保存文件的位序，以便原始和拷贝的是逐位一一对应的。即使目的地机器上包含位序列的文件是没意义的。例如，macintosh以二进制方式传送可执行文件到Windows系统，在对方系统上，此文件不能执行。如果你在ASCII方式下传输二进制文件，即使不需要也仍会转译。这会使传输稍微变慢 ，也会损坏数据，使文件变得不能用。（在大多数计算机上，ASCII方式一般假设每一字符的第一有效位无意义，因为ASCII字符组合不使用它。如果你传输二进制文件，所有的位都是重要的。）如果你知道这两台机器具有相同的系统，则二进制方式对文本文件和数据文件都是有效的。
列举：
ASCII传输模式：用HTML和文本编写的文件必须用ASCII模式上传
二进制传输模式：BINARY模式用来传送可执行文件，压缩文件，和图片文件
FTP支持两种模式：一种方式叫做Standard (也就是 PORT方式，主动方式)， Standard模式下 FTP的客户端发送 PORT 命令到FTP服务器。另一种是 Passive (也就是PASV，被动方式) ，Passive模式下FTP的客户端发送 PASV命令到 FTP Server。

Standard模式：
Port模式FTP 客户端首先和FTP服务器的TCP 21端口建立连接，通过这个通道发送命令，客户端需要接收数据的时候在这个通道上发送PORT命令。 PORT命令包含了客户端用什么端口接收数据。在传送数据的时候，服务器端通过自己的TCP 20端口连接至客户端的指定端口发送数据。 FTP server必须和客户端建立一个新的连接用来传送数据。（可以看到在这种方式下是客户端和服务器建立控制连接，服务器向客户端建立数据连接，其中，客户端的控制连接和数据连接的端口号是大于1024的两个端口号（临时端口），而FTP服务器的数据端口为20，控制端口为21）
Passive模式：
Passive模式在建立控制通道的时候和Standard模式类似，但建立连接后发送的不是Port命令，而是Pasv命令。FTP服务器收到Pasv命令后，随机打开一个临时端口（也叫自由端口，端口号大于1023小于65535）并且通知客户端在这个端口上传送数据的请求，客户端连接FTP服务器此端口，然后FTP服务器将通过这个端口进行数据的传送，这个时候FTP server不再需要建立一个新的和客户端之间的连接。（可以看到这种情况下的连接都是由客户端向服务器发起的，与下面所说的“为了解决服务器发起到客户的连接的问题，人们开发了一种不同的FTP连接方式。这就是所谓的被动方式”相对应，而服务器端的数据端口是临时端口，而不是常规的20）

###### 注意：很多防火墙在设置的时候都是不允许接受外部发起的连接的，所以许多位于防火墙后或内网的FTP服务器不支持PASV模式，因为客户端无法穿过防火墙打开FTP服务器的高端端口；而许多内网的客户端不能用PORT模式登陆FTP服务器，因为从服务器的TCP 20无法和内部网络的客户端建立一个新的连接，造成无法工作。


