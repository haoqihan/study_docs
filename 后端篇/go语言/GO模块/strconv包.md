```go
// 将布尔值转换为字符串 true 或 false
func FormatBool(b bool) string

// 将字符串转换为布尔值
// 它接受真值：1, t, T, TRUE, true, True
// 它接受假值：0, f, F, FALSE, false, False
// 其它任何值都返回一个错误。
func ParseBool(str string) (bool, error)
```


```go

// ErrRange 表示值超出范围
var ErrRange = errors.New("value out of range")

// ErrSyntax 表示语法不正确
var ErrSyntax = errors.New("invalid syntax")

// 将整数转换为字符串形式。base 表示转换进制，取值在 2 到 36 之间。
// 结果中大于 10 的数字用小写字母 a - z 表示。
func FormatInt(i int64, base int) string
func FormatUint(i uint64, base int) string

// 将字符串解析为整数，ParseInt 支持正负号，ParseUint 不支持正负号。
// base 表示进位制（2 到 36），如果 base 为 0，则根据字符串前缀判断，
// 前缀 0x 表示 16 进制，前缀 0 表示 8 进制，否则是 10 进制。
// bitSize 表示结果的位宽（包括符号位），0 表示最大位宽。
func ParseInt(s string, base int, bitSize int) (i int64, err error)
func ParseUint(s string, base int, bitSize int) (uint64, error)

// 将整数转换为十进制字符串形式（即：FormatInt(i, 10) 的简写）
func Itoa(i int) string

// 将字符串转换为十进制整数，即：ParseInt(s, 10, 0) 的简写）
func Atoi(s string) (int, error)
```

```go
// 示例
func main() {
	fmt.Println(strconv.ParseInt("FF", 16, 0))
	// 255
	fmt.Println(strconv.ParseInt("0xFF", 16, 0))
	// 0 strconv.ParseInt: parsing "0xFF": invalid syntax
	fmt.Println(strconv.ParseInt("0xFF", 0, 0))
	// 255
	fmt.Println(strconv.ParseInt("9", 10, 4))
	// 7 strconv.ParseInt: parsing "9": value out of range
}
```


```go
// FormatFloat 将浮点数 f 转换为字符串形式
// f：要转换的浮点数
// fmt：格式标记（b、e、E、f、g、G）
// prec：精度（数字部分的长度，不包括指数部分）
// bitSize：指定浮点类型（32:float32、64:float64），结果会据此进行舍入。
//
// 格式标记：
// 'b' (-ddddp±ddd，二进制指数)
// 'e' (-d.dddde±dd，十进制指数)
// 'E' (-d.ddddE±dd，十进制指数)
// 'f' (-ddd.dddd，没有指数)
// 'g' ('e':大指数，'f':其它情况)
// 'G' ('E':大指数，'f':其它情况)
//
// 如果格式标记为 'e'，'E'和'f'，则 prec 表示小数点后的数字位数
// 如果格式标记为 'g'，'G'，则 prec 表示总的数字位数（整数部分+小数部分）
// 参考格式化输入输出中的旗标和精度说明
func FormatFloat(f float64, fmt byte, prec, bitSize int) string

// 将字符串解析为浮点数，使用 IEEE754 规范进行舍入。
// bigSize 取值有 32 和 64 两种，表示转换结果的精度。 
// 如果有语法错误，则 err.Error = ErrSyntax
// 如果结果超出范围，则返回 ±Inf，err.Error = ErrRange
func ParseFloat(s string, bitSize int) (float64, error)
```

```go
// 示例
func main() {
	s := "0.12345678901234567890"

	f, err := strconv.ParseFloat(s, 32)
	fmt.Println(f, err)                // 0.12345679104328156
	fmt.Println(float32(f), err)       // 0.12345679

	f, err = strconv.ParseFloat(s, 64)
	fmt.Println(f, err)                // 0.12345678901234568
}
```

```go
// 将 s 转换为双引号字符串
func Quote(s string) string

// 功能同上，非 ASCII 字符和不可打印字符会被转义
func QuoteToASCII(s string) string

// 功能同上，非图形字符会被转义
func QuoteToGraphic(s string) string

------------------------------

// 示例
func main() {
	s := "Hello\t世界！\n"
	fmt.Println(s)                         // Hello	世界！（换行）
	fmt.Println(strconv.Quote(s))          // "Hello\t世界！\n"
	fmt.Println(strconv.QuoteToASCII(s))   // "Hello\t\u4e16\u754c\uff01\n"
	fmt.Println(strconv.QuoteToGraphic(s)) // "Hello\t世界！\n"
}

```

```go
// 将 r 转换为单引号字符
func QuoteRune(r rune) string

// 功能同上，非 ASCII 字符和不可打印字符会被转义
func QuoteRuneToASCII(r rune) string

// 功能同上，非图形字符会被转义
func QuoteRuneToGraphic(r rune) string

------------------------------

// Unquote 将“带引号的字符串” s 转换为常规的字符串（不带引号和转义字符）
// s 可以是“单引号”、“双引号”或“反引号”引起来的字符串（包括引号本身）
// 如果 s 是单引号引起来的字符串，则返回该该字符串代表的字符
func Unquote(s string) (string, error)

// UnquoteChar 将带引号字符串（不包含首尾的引号）中的第一个字符“取消转义”并解码
//
// s    ：带引号字符串（不包含首尾的引号）
// quote：字符串使用的“引号符”（用于对字符串中的引号符“取消转义”）
//
// value    ：解码后的字符
// multibyte：value 是否为多字节字符
// tail     ：字符串 s 解码后的剩余部分
// error    ：返回 s 中是否存在语法错误
//
// 参数 quote 为“引号符”
// 如果设置为单引号，则 s 中允许出现 \'、" 字符，不允许出现单独的 ' 字符
// 如果设置为双引号，则 s 中允许出现 \"、' 字符，不允许出现单独的 " 字符
// 如果设置为 0，则不允许出现 \' 或 \" 字符，但可以出现单独的 ' 或 " 字符
func UnquoteChar(s string, quote byte) (value rune, multibyte bool, tail string, err error)

------------------------------

// 示例
func main() {
	s1 := "`Hello	世界！`"                 // 解析反引号字符串
	s2 := `"Hello\t\u4e16\u754c\uff01"` // 解析双引号字符串
	fmt.Println(strconv.Unquote(s1))    // Hello	世界！ <nil>
	fmt.Println(strconv.Unquote(s2))    // Hello	世界！ <nil>

	fmt.Println()
	fmt.Println(strconv.UnquoteChar(`\u4e16\u754c\uff01`, 0))
	// 19990 true \u754c\uff01 <nil>
	fmt.Println(strconv.UnquoteChar(`\"abc\"`, '"'))
	// 34 false abc\" <nil>
}

```

```go

// 将各种类型转换为字符串后追加到 dst 尾部。
func AppendInt(dst []byte, i int64, base int) []byte
func AppendUint(dst []byte, i uint64, base int) []byte
func AppendFloat(dst []byte, f float64, fmt byte, prec, bitSize int) []byte
func AppendBool(dst []byte, b bool) []byte

// 将各种类型转换为带引号字符串后追加到 dst 尾部。
func AppendQuote(dst []byte, s string) []byte
func AppendQuoteToASCII(dst []byte, s string) []byte
func AppendQuoteToGraphic(dst []byte, s string) []byte
func AppendQuoteRune(dst []byte, r rune) []byte
func AppendQuoteRuneToASCII(dst []byte, r rune) []byte
func AppendQuoteRuneToGraphic(dst []byte, r rune) []byte
```

