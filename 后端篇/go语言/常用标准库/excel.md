### 操作excel

#### 下载

```go
go get github.com/360EntSecGroup-Skylar/excelize/v2
```

#### 设置样式

```go
// 设置边框，背景颜色，对其方式，
style, _ := f.NewStyle(`{"border":[{"type":"left","color":"000000","style":1},
								{"type":"top","color":"000000","style":1},
								{"type":"bottom","color":"000000","style":1},
								{"type":"right","color":"000000","style":1}],
								"fill":{"type":"pattern","color":["#ffeb00"],"pattern":1},
							"alignment":	{"horizontal":"left","ident":1,"vertical":"center","wrap_text":true}，
"font":{"bold":true,"italic":true,"family":"Berlin Sans FB Demi","size":36,"color":"#777777"}}`)

```



