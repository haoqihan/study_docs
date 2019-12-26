[参考地址](https://www.cnblogs.com/OnOwnRoad/p/4899660.html)

什么时候用到再整理吧

#### crt的表头

```shell
# $language = "Python" 
# $interface = "1.0"
```

```shell
顶级对象crt的子属性和方法
 Dialog：定义了一个Dialog(对话框),通过这个对象，可以通过调用该对象的子属性和方法实现对话框的相关功能
    相关方法
        FileOpenDialog
            解释：
                定义了一个Dialog(对话框),通过这个对象，可以通过调用该对象的子属性和方法实现对话框的相关功能
            语法：
                crt.Dialog.Method([arglist])
            参数：
                （1）title:弹窗最上面的标题文字，见运行结果中窗口最上面的"请选择一个文件"。 
                （2）buttonLabel:见下图中的"Open"按钮，即打开文件用的，至于名称可以使用"Open"或者"打开"均可。
                （3）defaultFilename:默认文件名，如下，在弹窗的"文件名"中默认有"a.log"。注意：当有默认文件名时即使当前文件夹中没有该文件，在点击"打开"按钮后，结果依然会返回该文件的当前目录的绝对路径。
                （4）filter:用于过滤文件类型,见脚本举例中的格式，"Log Files (*.log)|*.log，| 的前半部分是一串提示符，会显示在运行结果中的"文件类型"中，后半部分是正则表达式，用于过滤以.log结尾的所有文件。
            示例：
                crt.Dialog.FileOpenDialog("请选择一个文件", "Open", "a.log", "Log Files (*.log)|*.log")
        MessageBox
            解释：
                弹出一个消息框，可以定义按钮，使用按钮和文本消息来实现和用户的简单对话。
            语法：
                crt.Dialog.MessageBox(message [, title [icon|buttons]])
            参数：
                （1）message:消息文字,必选参数，见运行结果中的消息正文。 
                （2）title:弹窗的标题描述，见运行结果中的标题处。 
                （3）icon:警示图标，见结果中的图1到图4。icon的取值有：16(叉号，表示错误)，32(问号，表示确认)，48(叹号，表示警告)，64(提示，表示信息提示) 
                （4）buttons:按钮类型，定义不同的类型，可以有不同的选项，同时鼠标点击不同的选项时也有不同的返回值。button取值范围为0到6, 
                    --0：见图5，点击后返回值为1； 
                    --1：见图6，点击'确定'时，返回1，点击'取消'时返回2； 
                    --2：见图7，点击'终止'时，返回3，点击'重试'时返回4，点击'忽略'时返回5； 
                    --3：见图8，点击'是'时，返回6，点击'否'时，返回7，点击'取消'时返回2； 
                    --4：见图9，点击'是'时，返回6，点击'否'时，返回7； 
                    --5：见图10，点击'重试'时，返回4，点击'取消'时返回2； 
                    --6：见图11，点击'取消'时，返回2，点击'重试'时，返回10，点击'继续'，返回11； 
            示例：
                 crt.Dialog.MessageBox("这里是消息框正文","这里是标题",16|0) 
        Prompt
            解释：
                弹出一个输入框，用户可以填写文字，比如填写文件名，填写路径，填写IP地址等。
            语法：
                crt.Dialog.Prompt(message [, title [, default [, isPassword ]]])
            参数：
                （1）message:消息文字,必选参数，见运行结果中的消息正文。 
                （2）title:弹窗的标题描述，见运行结果中的标题处。 
                （3）default:输入框中的默认值，如果为""，则没有默认值。 
                （4）isPassword:是否要隐藏输入的文字，类似于日常输入密码时显示**** 
                 (5) 运行结果如下图1，如果点击'ok'，返回输入的字符串，否则返回"" 
            示例：
                crt.Dialog.Prompt("这里是正文","这里是弹窗标题","这是默认值",true) 
```

```shell
Screen属性和方法
    属性：
        CurrentColumn
            解释：
                返回当前光标处的列坐标
            语法：
                crt.Screen.CurrentColumn
            示例：
                curCol = crt.Screen.CurrentColumn  # 获取坐标
                crt.Dialog.MessageBox(curCol)       # 打印结果
        CurrentRow
            解释：
                返回当前光标处的行坐标
            语法：
                crt.Screen.CurrentRow
            示例：
                curRow = crt.Screen.CurrentRow
                crt.Dialog.MessageBox(curRow)
        Columns
            解释：
                返回当前屏幕的最大列宽
            语法：
                crt.Screen.Columns
            示例：
                cols = crt.Screen.Columns
                crt.Dialog.MessageBox(cols)
        Rows
            解释：
                返回当前屏幕的行宽
            语法：
                crt.Screen.Rows
            示例：
                rows = crt.Screen.Rows
                crt.Dialog.MessageBox(rows)
        IgnoreEscape
            解释：
                定义当使用WaitForString、WaitForStrings 和 ReadString这三个方法时是否获取Escape字符(也就是特殊控制字符，如"\n")，默认是会获取的
            语法：
                crt.Screen.IgnoreEscape [ = True | False ]
            参数：
                true|false：当设置为true时不会获取特殊字符，为false时会获取，默认为false。
            示例：
                // 设置false，获取ctrl+c
                crt.Screen.IgnoreEscape = false;
                crt.Dialog.MessageBox(crt.Screen.ReadString("\03"))

                // 设置true，不获取ctrl+c
                crt.Screen.IgnoreEscape = true;
                crt.Dialog.MessageBox(crt.Screen.ReadString("\03"))
        
        MatchIndex
            解释：
                当使用WaitForStrings 和 ReadString这两个方法获取字符串时，会根据参数的位置获取返回值，而MatchIndex就是这个位置，从1开始计算，如果没有一个匹配到则返回0，
            语法：
                crt.Screen.MatchIndex
        Synchronous
            解释：
                设置屏幕的同步属性，关于该属性需要谨慎对待，若设置为false，
                则在脚本中使用WaitForString、WaitForStrings或ReadString函数时可能存在丢失一部分数据的现象，
                而设置为true时不会，但是设置为true后可能会存在屏幕卡顿的情况，
                出现这两种现象的原因应该是和这几个函数以及打印字符到Screen的机制有关系，
                具体内部原因不明，就具体使用而言，如果是跑脚本的话最好还是不要设置为true，
                大量的卡顿看着就会蛋疼了，还可能会造成CRT卡死
            语法：
                crt.Screen.Synchronous [ = True | False ]
            参数：
                true|false ：默认为false
    方法：
        Clear()
            解释：
                清屏功能
            语法：
                crt.Screen.Clear()
            示例：
                crt.Screen.Send("\r\n")
                crt.Screen.Clear()
        get()
            解释：
                按照坐标取出一个矩形框内的屏幕上的字符(即从某行某列开始到其它行其它列)，
                不包含字符串中的回车换行符，所以这个多用于获取无格式的光标处字符串或某小段特定区域字符串
            语法：
                crt.Screen.Get(row1, col1, row2, col2)
            示例：
                getScr = crt.Screen.Get(31,50,31,56)
                crt.Dialog.MessageBox(getScr)
        get2()
            解释：
                按照坐标取出一个矩形框内的屏幕上的字符(即从某行某列开始到其它行其它列)，
                包含字符串中的回车换行符，所以这个多用于获取大段带格式的字符串
            语法：
                crt.Screen.Get2(row1, col1, row2, col2)
            示例：
                getScr = crt.Screen.Get2(29,1,35,20);
                crt.Dialog.MessageBox(getScr)
        IgnoreCase()
            解释：
                使用全局参数设置控制在使用WaitForString、WaitForStrings和ReadString这三个函数时是否对大小写敏感，
                默认为false指大小写敏感即大小写字符串都会检查，设置为true时则不会检测大小写。
            语法：
                crt.Screen.IgnoreCase
            示例：
                crt.Screen.IgnoreCase = true;
                crt.Screen.Send("show memory\r\n");
                crt.Screen.WaitForString("more");
                crt.Screen.Send("\r\n");
                crt.Screen.WaitForStrings("more","#");
                crt.Screen.Send("\r\n");
                crt.Screen.ReadString("more","#");
        send()
            解释：
                向远端设备或者向屏幕(向屏幕发送的功能是CRT7.2以后版本才提供的)发送字符串。
                如语法中所表示的，string是待发送的字符串，这个字符串可以包含转码字符比如"\r","\n","\03"(ctrl+c)，
                当向屏幕上发送字符串时需要指定第二个参数为true。有了向屏幕发送字符串的功能，
                我们就可以很方便的和用户进行交互了。可以打印出一些我们需要的报错信息之类的
            语法：
                crt.Screen.Send(string, [, bSendToScreenOnly])
            示例：
                // 向远程设备发送英文命令"show memory"
                crt.Screen.Send("show memory\r\n");

                // 向屏幕上发送字符串
                crt.Screen.Send("hello,world!\r\n",true);
        SendKeys()
            解释：
                向当前窗口发送按键，包含组合按键，比如可以发送类似"CTRL+ALT+C"等这样的组合键，这样写即可：
                这个功能需要语言本身支持，目前只有VBS和JS脚本可以使用，Python和Perl都不可以
            语法：
                crt.Screen.SendKeys(string)
            示例：
                crt.Screen.Clear();
                crt.screen.sendkeys("mc~");
                crt.Sleep(2000);
                crt.screen.sendkeys("{f1}");
                crt.Sleep(2000);
                crt.screen.sendkeys("{esc}0");
                crt.Sleep(2000);
                crt.screen.sendkeys("{esc}0");
                crt.Sleep(2000);
                crt.screen.sendkeys("y");
            参考信息
                https://www.cnblogs.com/OnOwnRoad/p/4963969.html
        WaitForCursor()
            解释：
                 等待光标移动，当移动时返回值为true，当有超时时间参数且超时时返回false，否则会一直等待光标移动。利用这个功能可以用来判断一个命令的输出是否结束，
                 只不过超时时间是以秒为单位的，对于脚本当中，这个时间还是略显久了。
            语法：
                crt.Screen.WaitForCursor([timeout])
            示例：
                while (1) {
                    if ( crt.Screen.WaitForCursor(5) ) {
                        crt.Screen.Send("show version\r\n");
                    }
                }
        WaitForKey()
            解释：
                检测有键盘按键时返回true，当有超时时间参数且超时时返回false，否则会一直等待按键。
                只可惜这个函数不知道输入的键是什么，否则就可以针对性的判断了，它只能检测到有输入而已。
            语法：
                crt.Screen.WaitForKey([timeout])
            示例：
                // 每5秒内有输入时发送一个命令
                while (1) {
                    if ( crt.Screen.WaitForKey(5) ) {
                        crt.Screen.Send("show version\r\n");
                    }
                }
        WaitForString()
            解释：
                一般用于发送命令后等待某字符串，这个字符串只要是屏幕上出现的即可，
                哪怕是粘贴上去的命令也会同样被检测到，也可以用于等待屏幕的输出打印，
                不需要先发送命令。不过一般我们使用它来检测的都是发送命令后出现的标识符。
            语法：
                crt.Screen.WaitForString(string,[timeout],[bCaseInsensitive])
            参数：
                1、string，必选参数，等待的字符串，可以是特殊字符比如:\r\n；
                2、timeout，可选参数，超时时间，当检测不到对应字符串时会返回false，没有此参数时会一直等待；
                3、bCaseInsensitive，可选参数，大小写不敏感，默认值是false，表示将检测字符串的大小写，当为true时不检测大小写
            示例：
                // 发送命令，并在5秒内获取到对应的字符串后发送一条命令
                crt.Screen.Send("\r\n");
                if ( crt.Screen.WaitForString("#",5) ) {
                    crt.Screen.Send("show version\r\n");
                }
        WaitForStrings()
            解释：
                和WaitForString是同样的功能，只不过可以等待多个字符串，如果有匹配到某个字符串，
                则返回值该字符串在这些字符串中的位置，位置值从1开始。若在超时时间内没有匹配到则返回false，
                没有超时时间时会一直等待。
            语法：
                crt.Screen.WaitForStrings([string1,string2..],[timeout],[bCaseInsensitive])
            参数：
                1、string，必选参数，等待的字符串，最少有一个，可以是特殊字符比如:\r\n；
                2、timeout，可选参数，超时时间，当检测不到对应字符串时会返回false，没有此参数时会一直等待；
                3、bCaseInsensitive，可选参数，大小写不敏感，默认值是false，表示将检测字符串的大小写，当为true时不检测大小写
            示例：（js）
                var outPut = crt.Screen.WaitForStrings("error", "warning", "#", 10);
                var waitIndex = crt.Screen.MatchIndex
                switch (waitIndex) {
                    case 0:
                        crt.Dialog.MessageBox("Timed out!")
                        break;
                    case 1:
                        crt.Dialog.MessageBox("Found 'error'")
                        break;
                    case 2:
                        crt.Dialog.MessageBox("Found 'warning'")
                        break;
                    case 3:
                        crt.Dialog.MessageBox("Found '#'")
                        break;    
                }
        ReadString()
            解释：
                这个功能和上面的WaitForStrings函数有些类似，都是等待某几个字符串出现，
                不过不同的是，ReadString函数还会读取字符串之前的所有出现的字符，
                这个功能可以很方便的用于发送一个命令后获取这个命令的输出结果，
                不过这个函数也不是特别稳定，因为很可能存在命令的输出结果很快，
                而屏幕又没有捕捉到时，要么会由于超时而返回false，要么会一直等待，
                最终返回的都是空值，因此完全依靠该函数获取命令的输出的话并不是很把稳
                (如果程序对于稳定性要求很高的话，那么最好还是不要依赖这个函数。
            语法：
                crt.Screen.ReadString([string1,string2..],[timeout],[bCaseInsensitive])
            参数
                1、string，必选参数，等待的字符串，最少有一个，可以是特殊字符比如:\r\n；
                2、timeout，可选参数，超时时间，当检测不到对应字符串时会返回false，没有此参数时会一直等待；
                3、bCaseInsensitive，可选参数，大小写不敏感，默认值是false，表示将检测字符串的大小写，当为true时不检测大小写。 
            示例：（js）
                // 发送命令并根据提示符获取命令的输出。
                crt.Screen.Send("show version\r\n");
                crt.Screen.WaitForString("show version",2);
                var outPut = crt.Screen.ReadString("error", "warning", "#", 10);
                var waitIndex = crt.Screen.MatchIndex
                switch (waitIndex) {
                    case 0:
                        crt.Dialog.MessageBox("Timed out!")
                        break;
                    case 1:
                        crt.Dialog.MessageBox("Found 'error'")
                        break;
                    case 2:
                        crt.Dialog.MessageBox("Found 'warning'")
                        break;
                    case 3:
                        crt.Dialog.MessageBox("命令的输出时:"+outPut);
                        break;    
                }
```



