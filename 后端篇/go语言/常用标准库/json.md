基础结构

```go
type User struct {
    Email    string `json:"email"`
    Password string `json:"password"`
}
```

#### 1.临时忽略struct的某个字段

如果想临时忽略掉空`Password`字段,可以用`omitempty`:

```go
user := User{Email: "xxx", Password: "xxx"}
k, v := json.Marshal(struct {
    *User
    Password bool `json:"password,omitempty"`
}{
    User: &user,
})
fmt.Println(string(k), v)
```

#### 2.临时添加额外的字段

临时忽略掉空`Password`字段，并且添加`token`字段

```go
user := User{Email: "xxx", Password: "xxx"}
k, v := json.Marshal(struct {
    *User
    Token    string `json:"token"`
    Password bool   `json:"password,omitempty"`
}{
    User:  &user,
    Token: "token",
})
fmt.Println(string(k), v)
```

#### 3.临时粘合两个struct

基础结构

```go
type BlogPost struct {
	URL   string `json:"url"`
	Title string `json:"title"`
}
type Analytics struct {
	Visitors  int `json:"visitors"`
	PageViews int `json:"page_views"`
}
```

使用

```go
post := BlogPost{URL: "URL", Title: "Title"}
analytics := Analytics{Visitors: 1, PageViews: 2}
k, v := json.Marshal(struct {
    *BlogPost
    *Analytics
}{&post, &analytics})
fmt.Println(string(k), v)
```

#### 4.一个json切分成两个struct

```go
post := BlogPost{}
analytics := Analytics{}
err := json.Unmarshal([]byte(`{
		  "url": "attila@attilaolah.eu",
		  "title": "Attila's Blog",
		  "visitors": 6,
		  "page_views": 14
		}`), &struct {
    *BlogPost
    *Analytics
}{&post, &analytics})
if err != nil {
    fmt.Println(err)
}
fmt.Printf("%+v\n", post)
fmt.Printf("%+v", analytics)
```

#### 5.临时改名struct的字段

先用两个字段把要修改的名字占用，然后在修改字段名称

```go
type CacheItem struct {
	Key    string `json:"key"`
	MaxAge int    `json:"cacheAge"`
	Value  string `json:"cacheValue"`
}

item := CacheItem{Key: "key", MaxAge: 11, Value: "value"}

k, v := json.Marshal(struct {
    *CacheItem
    OmitMaxAge string `json:"cacheAge,omitempty"`
    OmitValue  string `json:"cacheValue,omitempty"`
    MaxAge     int    `json:"max_age"`
    Value      string `json:"value"`
}{
    CacheItem: &item,
    // Set the int by value:
    MaxAge: item.MaxAge,
    // Set the nested struct by reference, avoid making a copy:
    Value: item.Value,
})
fmt.Println(string(k), v)
```



