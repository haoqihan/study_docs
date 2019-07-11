### strings包

##### 常用方法

```go
var str string = "字符串"
len(str)  									// 统计字符串长度，按字节计算，len(string)
strings.Contains(str,"字符")					// 判断字符是否存在，返回布尔值
strings.Count(str,"字")						// 字符串统计，返回个数
strings.EqualFold("abc","ABC") 	 			 // 不区分大小写进行字符串的比较
strings.Index(str,"符")						// 返回在字符串第一次出现的位置
strings.LastIndex(str,"符")					// 返回在字符串最后出现的位置
new_str := strings.Replace(str,"字"，"22",-1)	// 	字符串替换strings.Replace(s, old, new, n)，n表示替换次数，-1代表替所有。
strings.Split(str,",")						// 字符串拆分为数组，返回一个数组
strings.Fields(str)							// 字符串拆分为数组，返回一个数组，分割的内容为1：n 个空格
strings.ToUpper(str)						// 字符全部转换为大写
strings.ToLower(str)						// 字符全部转换为小写

strings.TrimSpace(str)						// 去除两边空格及特殊字符
strings.Trim(str,cutset)					// cutest代表去除的两边字符
strings.TrimLeft(s,cutset)					// 将左边的指定字符去除
strings.TrimRight(s,cutset)					// 将右边的指定字符去除

strings.HasPrefix(s, prefix)				// 判断以什么字符开头
strings.HasSuffix(s, suffix)				// 判断以什么字符结尾
```

