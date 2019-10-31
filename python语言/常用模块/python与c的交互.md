### C语言概述

#### c语言概述

```shell
C语言：与操作系统直接交互的便车会给你语言
- 1973年，由Dennis Ritchie设计，用于重写Unix操作系统
- 通用语言、过程式编程语言，重点关注程序执行效率
- C语言也提供函数API，但严格受控

c89:ANSI标准化的C语言版本，也被称为标准c或ANSI 、ISO版本
c99：1999年改进版本，inline、变长数组等新语法，需要额外声明
c11:2011年版本，匿名结构，Unicode支持，边界检查函数等
c18:2018年6月版本，无新语法增加

python解释器采用c语言编写：被称为Cpython
Python从未试图替换C语言，而是通过扩展与C语言并存，各展所长
C和Python都将是不可超越的经典

C语言的精髓
C语言精髓在于灵活语法下内存有效管理
无论何种语法形态，最终体现为数据在内存中栈和堆的存储和操作
C语言可以直接精细到操作每个比特和字节，充分发挥计算机效率
```

#### c语言语法

```c
C语言的注释
- 多行注释： /*......*/
- 单行注释： //
- 注释完全被编译器忽略，但很多工具可以提取注释形成文档

C语言的所属关系
- 大括号表达所属关系：{....}
- 函数，分支，循环等定义中使用
- 表达式用分号；隔离，表示结束

C语言的声明Declaration
- 变量及函数需要声明再使用，声明要指定类型
- 声明需要使用保留或内置数据类型（char int）等
- 相关保留字：struct、union、enum

C语言的程序控制结构
- 分支 if,if-else,switch-case,default,goto
- 循环：do-while,while,for,break,continue
- 分支和循环都可以嵌套定义和使用

C语言的字符集
- 字母和数字：a-z A-Z 0-9
- 特殊字符 ! " # % & ' () * +、- . /:;< = > ? [\]^_ {|} ~
- 隐式字符：空格、制表符TAB、换行等


c语言的操作符
- 数学操作符： +、-、*、/、%
- 赋值操作符： =
- 增强赋值操作符号：+=、-=、*= /= %= &= |= ^= <<= >>=
- 位逻辑操作符：～，&，|，^
- 位移位操作符：<<,>>
- 布尔运算操作符：！，&& , ||
- 条件评估操作符：?:
- 比较操作符：<,>,<=,>=,==,!=
- 自操作符：++,--
- 成员选择操作符：. , ->
- 指针引用操作符：&，*,[]
- 分组操作符：()

```

| auto     | do       | goto       | `signed` | `unsigned` |
| -------- | -------- | ---------- | -------- | ---------- |
| break    | `double` | if         | sizeof   | void       |
| case     | else     | `int`      | static   | `volatile` |
| char     | enum     | `long`     | struct   | while      |
| const    | extern   | `register` | switch   | inline     |
| continue | `float`  | return     | typedef  | restrict   |
| default  | for      | `short`    | union    |            |

#### c开发环境配置

#### c语言实例

#### 编译和解释

```shell
C语言是一种约定数据类型的语言
- 类型声明无处不在：变量，函数
- 数据类型的本质：计算机内存空间的外在表现
- 类型声明体现了编译语言的特点，即：编译阶段能够评估内存使用

编译和解释的一般区别
- 编译语言：C语言，编译器一次性生成目标代码，优化更充分
	- 需要编程语言能够确定的元素尽量确定，如数据类型，引用关系
- 脚本语言：python语言，执行程序时需要源代码，维护更灵活
	- 不需要在编程阶段确定更多信息，如数据类型、引用关系等，靠执行先后决定

python语言 VS C语言
- 脚本语言 VS 编译语言（静态语言）
- 根据执行情况确定语句含义 vs 编译阶段需要确定语句含义
- 重在程序员的隐形约定 VS 重在程序中的显式声明
```

### python与C的交互方法

#### python与c的交互概念

```shell
Python与C、C++交互的三种方式
- Python的扩展：在python程序中调用c、C++编写的库
- Python的嵌入：在c、C++程序中调用python程序
- Python调用：python和c间以程序级别的互相调用

python与C、C++交互的价值
- 整合python高产与C、C++高效的优势
- 利用C或Python已有功能服务彼此的程序
- python作为粘性脚本整合或被整合到个类独立程序

python扩展：在python程序中调用c、C++编写的库
- 目的：提升关键代码性能，引入C语言成熟功能库
- 方式：Cython、SWIG、ctypes，CFFI
- 形式：python为主程序，c通过.dll/.so形式使用

Python的嵌入：在c、C++程序中调用python程序
- 目的：利用python高产，引入python成熟的功能库
- 方式python、c API
- 形式c、C++ 为主程序，python通过源文件形式使用

Python调用：python和c间以程序级别的互相调用
- 目的：模块功能互用，以功能使用为目标
- 方式：子进程或线程方式，即subprocess
- 形式c、c++和python都是独立程序
```

#### python的扩展方法

```shell
Cython：实现python扩展的一种语言，第三方库
- 思路：通过一种简单的语言来实现python和c的接口
- 方式：采用Pyrex语法形式
- 结果：采用c数据类型的python编程，实现混合编程

SWIG：一个将c、c++与脚本语言相整合的编译器，独立工具
- 思路：通过一个编译器来实现python与c的接口
- 方式：纯c、C++编程，通过编写接口变成python模块
- 结果：独立c和python编程，重点在于编写接口（描述）

ctypes：调用dll或共享库的python功能函数库，标准库API
- 思路：通过一个python标准库实现python扩展
- 方式：c语言功能编为.dll或.so 库，加载库及调用函数，API
- 结果：c语言独立编程，python使用库调用接口函数

CFFI：在python中直接使用c函数方式，第三方库
- 思路：类似ctypes，使用api扩展c程序，也可以直接混合编程
- 方式：关注c函数的访问接口，而不是库函数，构建API
- 结果：c语言独立编程，python用CFFI扩展，最小学习代价
```

#### python的嵌入方法

```shell
python、c API：python嵌入的主要接口
- 嵌入python语句：嵌入一个或多个python语句
- 嵌入python脚本：嵌入一个或多个python文件
- python、c API需要加载python解释器及加载python语句和脚本

- python/c API是一组能够在c语言下执行类定义和函数
- 头文件：Python.h
- 函数：加载python解释器、嵌入Python语句及脚本、数据类型转换等
```

加载Python解释器

| 函数                                          | 描述                                                       |
| --------------------------------------------- | ---------------------------------------------------------- |
| Py_Initialize()                               | 初始化python解释器，加载builtins，`__main__`、sys等        |
| Py_Finalize()                                 | 终结化python解释器，释放解释器占用的内存                   |
| PyRun_simpleString(const char * cmd)          | 在`__main__`模块中执行一条语句，如果`__main__`不存在则创建 |
| PyRun_SimpleFile(FILE *fp,const char * fname) | 在c中调用Python文件                                        |

#### python的调用方法

```shell
在python中调用c语言程序
- 使用python的subprocess模块

python与c间以程序级别互相调用
- Python调用c：subprocess模块
- C调用Python：system()函数
```

### python扩展的CFFI方法

CFFI的概述

```shell
CFFI： C Foreign Function Interface for Python
思路：类似ctypes，使用API扩展c程序，也可以直接混合编程
方式：关注c函数的访问接口，而不是库函数，构建API
结果：c语言独立编程，Python用CFFI扩展，最小学习代价

- 库扩展：对已经编译好的c语言.dll 或.so 库调用并使用
- 标准库：c语言标准库的调用及使用
- 数据类型：c语言与python数据类型的转换

- 安装： pip install cffi

```

#### CFFI的功能接口

| 函数                     | 描述                                                     |
| ------------------------ | -------------------------------------------------------- |
| ffi.NULL                 | 相当于常量值NULL                                         |
| ffi.new(cdecl)           | 数组或指针生成，new('x *') 或new('x[n]')                 |
| ffi.cast(ctype,value)    | c数据类型声明，ctype是类型名，value是变量，cast('int',x) |
| ffi.string(cdata)        | 从cdata类型返回一个python字符串                          |
| ffi.unpack(cdata,lenght) | 从cdata数组中获取特定长度，返回一个python字符串或列表    |
| ffi.typeof(ctype)        | 返回ctype的长度                                          |
| ffi.sizeof(object)       | 返回object对象长度                                       |
| ffi.alignof(ctype)       | 返回ctype或对象的长度                                    |
| ffi.dlopen(libpath)      | 打开动态链接库并建立一个链接                             |
| ffi.diclose(lib)         | 关闭动态链接并释放句柄                                   |
| ffi.cdef(str)            | str指明python中需要使用的c类型，函数等声明               |
| ffi.memmove(dst,src,n)   | 从src向dst拷贝n直接内容，注意src和dst都是python变量      |
|                          |                                                          |
|                          |                                                          |

