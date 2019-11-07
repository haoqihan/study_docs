### strings包

```go
// 转换

func ToUpper(s string) string
func ToLower(s string) string
func ToTitle(s string) string

func ToUpperSpecial(_case unicode.SpecialCase, s string) string
func ToLowerSpecial(_case unicode.SpecialCase, s string) string
func ToTitleSpecial(_case unicode.SpecialCase, s string) string

func Title(s string) string
```

```go
// 比较

func Compare(a, b string) int

func EqualFold(s, t string) bool
```

```go

// 清理

func Trim(s string, cutset string) string
func TrimLeft(s string, cutset string) string
func TrimRight(s string, cutset string) string

func TrimFunc(s string, f func(rune) bool) string
func TrimLeftFunc(s string, f func(rune) bool) string
func TrimRightFunc(s string, f func(rune) bool) string

func TrimSpace(s string) string

func TrimPrefix(s, prefix string) string
func TrimSuffix(s, suffix string) string
```

```go
// 拆合

func Split(s, sep string) []string
func SplitN(s, sep string, n int) []string

func SplitAfter(s, sep string) []string
func SplitAfterN(s, sep string, n int) []string

func Fields(s string) []string
func FieldsFunc(s string, f func(rune) bool) []string

func Join(a []string, sep string) string

func Repeat(s string, count int) string
```

```go

// 子串

func HasPrefix(s, prefix string) bool
func HasSuffix(s, suffix string) bool

func Contains(s, substr string) bool
func ContainsRune(s string, r rune) bool
func ContainsAny(s, chars string) bool

func Index(s, sep string) int
func IndexByte(s string, c byte) int
func IndexRune(s string, r rune) int
func IndexAny(s, chars string) int
func IndexFunc(s string, f func(rune) bool) int

func LastIndex(s, sep string) int
func LastIndexByte(s string, c byte) int
func LastIndexAny(s, chars string) int
func LastIndexFunc(s string, f func(rune) bool) int

func Count(s, sep string) int
```

```go
// 替换

func Replace(s, old, new string, n int) string

func Map(mapping func(rune) rune, s string) string
```

```go
// 其他
type Reader struct { ... }

func NewReader(s string) *Reader

func (r *Reader) Read(b []byte) (n int, err error)
func (r *Reader) ReadAt(b []byte, off int64) (n int, err error)
func (r *Reader) WriteTo(w io.Writer) (n int64, err error)
func (r *Reader) Seek(offset int64, whence int) (int64, error)

func (r *Reader) ReadByte() (byte, error)
func (r *Reader) UnreadByte() error

func (r *Reader) ReadRune() (ch rune, size int, err error)
func (r *Reader) UnreadRune() error

func (r *Reader) Len() int
func (r *Reader) Size() int64
func (r *Reader) Reset(s string)
```



##### 常用方法

```go
var str string = "字符串"
len(str)  									// 统计字符串长度，按字节计算，len(string)
strings.Contains(str,"字符")					// 判断字符是否存在，返回布尔值
fmt.Println(strings.ContainsAny("failure", "ez")) // 判断 ez 只要有一个在failure 中就返回true
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

fmt.Println("ba" + strings.Repeat("na", 2))
// 输出 banana


```

#### 字符串与基本类型之间的转换

##### 字符串转为整数

```go
func ParseInt(s string, base int, bitSize int) (i int64, err error)
func ParseUint(s string, base int, bitSize int) (n uint64, err error)
func Atoi(s string) (i int, err error)

// 常使用Atoi
```

#####  整型转为字符串

```go
func FormatUint(i uint64, base int) string    // 无符号整型转字符串
func FormatInt(i int64, base int) string    // 有符号整型转字符串
func Itoa(i int) string

// 常使用 Itoa
```

##### 字符串和布尔值之间的转换

```go
// 接受 1, t, T, TRUE, true, True, 0, f, F, FALSE, false, False 等字符串；
// 其他形式的字符串会返回错误
func ParseBool(str string) (value bool, err error)

// 直接返回 "true" 或 "false"
func FormatBool(b bool) string

// 将 "true" 或 "false" append 到 dst 中
// 这里用了一个 append 函数对于字符串的特殊形式：append(dst, "true"...)
func AppendBool(dst []byte, b bool)
```

##### 字符串和浮点数之间的转换

```go
func ParseFloat(s string, bitSize int) (f float64, err error)
func FormatFloat(f float64, fmt byte, prec, bitSize int) string
func AppendFloat(dst []byte, f float64, fmt byte, prec int, bitSize int)

例子：
strconv.ParseFloat("2.222",64)
// 结果 2.222  float64  字符串转float

// float64 转字符串
strconv.FormatFloat(2.22222,'f',3,64)
// 结果：2.222


fmt.Println("This is", strconv.Quote("studygolang.com"), "website")
// This is "studygolang.com" website
```





