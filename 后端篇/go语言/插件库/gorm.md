## 0.常使用的方法

### 0.1 库安装

```go
    go get -u github.com/jinzhu/gorm
```

### 0.2. 数据库连接

```go
import (
    "github.com/jinzhu/gorm"
    _ "github.com/jinzhu/gorm/dialects/mysql"
）

var db *gorm.DB

func init() {
    var err error
    db, err = gorm.Open("mysql", "<user>:<password>/<database>?charset=utf8&parseTime=True&loc=Local")
    if err != nil {
        panic(err)
    }
}
```

连接比较简单，直接调用 gorm.Open 传入数据库地址即可 github.com/jinzhu/gorm/dialects/mysql 是 golang 的 mysql 驱动，实际上就是 github.com/go-sql-driver/mysql 作者这里为了好记，重新弄了个名字 这里我用的 mysql，实际上支持基本上所有主流的关系数据库，连接方式上略有不同

```go
    db.DB().SetMaxIdleConns(10)
    db.DB().SetMaxOpenConns(100)
```

还可以使用 db.DB() 对象设置连接池信息

### 0.3. 表定义

先来定义一个点赞表，这里面一条记录表示某个用户在某个时刻对某篇文章点了一个赞，用 ip + ua 来标识用户，title 标识文章标题

```go
    type Like struct {
        ID        int    `gorm:"primary_key"`
        Ip        string `gorm:"type:varchar(20);not null;index:ip_idx"`
        Ua        string `gorm:"type:varchar(256);not null;"`
        Title     string `gorm:"type:varchar(128);not null;index:title_idx"`
        Hash      uint64 `gorm:"unique_index:hash_idx;"`
        CreatedAt time.Time
    }
```

gorm 用 tag 的方式来标识 mysql 里面的约束

创建索引只需要直接指定列即可，这里创建了两个索引，ip_idx 和 title_idx；如果需要多列组合索引，直接让索引的名字相同即可；如果需要创建唯一索引，指定为 unique_index 即可

支持时间类型，直接使用 time.Time 即可

### 0.4. 创建表

```go
    if !db.HasTable(&Like{}) {
        if err := db.Set("gorm:table_options", "ENGINE=InnoDB DEFAULT CHARSET=utf8").CreateTable(&Like{}).Error; err != nil {
            panic(err)
        }
    }
```

直接通过 db.CreateTable 就可以创建表了，非常方便，还可以通过 db.Set 设置一些额外的表属性

### 0.5. 插入

```go
    like := &Like{
        Ip:        ip,
        Ua:        ua,
        Title:     title,
        Hash:      murmur3.Sum64([]byte(strings.Join([]string{ip, ua, title}, "-"))) >> 1,
        CreatedAt: time.Now(),
    }

    if err := db.Create(like).Error; err != nil {
        return err
    }
```

先构造已给对象，直接调用 db.Create() 就可以插入一条记录了

### 0.6. 删除

```go
    if err := db.Where(&Like{Hash: hash}).Delete(Like{}).Error; err != nil {
        return err
    }
```

先用 db.Where() 构造查询条件，再调用 db.Delete() 就可以删除

### 0.7. 查询

```go
    var count int
    err := db.Model(&Like{}).Where(&Like{Ip: ip, Ua: ua, Title: title}).Count(&count).Error
    if err != nil {
        return false, err
    }
```

先用 db.Model() 选择一个表，再用 db.Where() 构造查询条件，后面可以使用 db.Count() 计算数量，如果要获取对象，可以使用 db.Find(&Likes) 或者只需要查一条记录 db.First(&Like)

### 0.8. 修改

```go
    db.Model(&user).Update("name", "hello")
    db.Model(&user).Updates(User{Name: "hello", Age: 18})
    db.Model(&user).Updates(User{Name: "", Age: 0, Actived: false}) // nothing update
```

我这个系统里面没有更新需求，这几个例子来自于官网，第一个是更新单条记录；第二个是更新整条记录，注意只有非空字段才会更新；第三个例子是不会更新的，在系统设计的时候要尽量避免这些空值有特殊的含义，如果一定要更新，可以使用第一种方式，设置单个值

### 0.9. 错误处理

其实你已经看到了，这里基本上所有的函数都是链式的，全部都返回 db 对象，任何时候调用 db.Error 就能获取到错误信息，非常方便

### 0.10. 事务

```go
    func CreateAnimals(db *gorm.DB) err {
        tx := db.Begin()
        if err := tx.Create(&Animal{Name: "Giraffe"}).Error; err != nil {
            tx.Rollback()
            return err
        }
        if err := tx.Create(&Animal{Name: "Lion"}).Error; err != nil {
            tx.Rollback()
            return err
        }
        tx.Commit()
        return nil
    }
```

事务的处理也很简单，用 db.Begin() 声明开启事务，结束的时候调用 tx.Commit()，异常的时候调用 tx.Rollback()

### 0.11. 其他

还可以使用如下方式设置日志输出级别以及改变日志输出地方

```
    db.LogMode(true)
    db.SetLogger(gorm.Logger{revel.TRACE})
    db.SetLogger(log.New(os.Stdout, "\r\n", 0))
```

也支持普通的 sql，但是建议尽量不要使用

## 1. Gorm介绍

GORM是使用Go语言开发的友好的ORM库。

### 1.1. 安装

```go
    go get -u github.com/jinzhu/gorm
```

通用数据库接口sql.DB

从`*gorm.DB`连接获取通用数据库接口`*sql.DB`

```go
    // 获取通用数据库对象`*sql.DB`以使用其函数
    db.DB()

    // Ping
    db.DB().Ping()
```

### 1.2. 连接池

```go
    db.DB().SetMaxIdleConns(10)
    db.DB().SetMaxOpenConns(100)
```

### 1.3. 复合主键

将多个字段设置为主键以启用复合主键

```go
    type Product struct {
        ID           string `gorm:"primary_key"`
        LanguageCode string `gorm:"primary_key"`
    }
```

### 1.4. 日志

Gorm有内置的日志记录器支持，默认情况下，它会打印发生的错误

```go
    // 启用Logger，显示详细日志
    db.LogMode(true)

    // 禁用日志记录器，不显示任何日志
    db.LogMode(false)

    // 调试单个操作，显示此操作的详细日志
    db.Debug().Where("name = ?", "jinzhu").First(&User{})
```

### 1.5. 自定义日志

参考GORM的默认记录器如何自定义它https://github.com/jinzhu/gorm/blob/master/logger.go

```go
    db.SetLogger(gorm.Logger{revel.TRACE})
    db.SetLogger(log.New(os.Stdout, "\r\n", 0))
```

### 1.6. 架构

Gorm使用可链接的API，`*gorm.DB`是链的桥梁，对于每个链API，它将创建一个新的关系。

```go
    db, err := gorm.Open("postgres", "user=gorm dbname=gorm sslmode=disable")

    // 创建新关系
    db = db.Where("name = ?", "jinzhu")

    // 过滤更多
    if SomeCondition {
        db = db.Where("age = ?", 20)
    } else {
        db = db.Where("age = ?", 30)
    }
    if YetAnotherCondition {
        db = db.Where("active = ?", 1)
    }
```

当我们开始执行任何操作时，GORM将基于当前的`*gorm.DB`创建一个新的`*gorm.Scope`实例

```go
    // 执行查询操作
    db.First(&user)
```

并且基于当前操作的类型，它将调用注册的creating,updating,querying,deleting或row_querying回调来运行操作。

## 2. Gorm查询

### 2.1. 查询

```go
    // 获取第一条记录，按主键排序
    db.First(&user)
    //// SELECT * FROM users ORDER BY id LIMIT 1;

    // 获取最后一条记录，按主键排序
    db.Last(&user)
    //// SELECT * FROM users ORDER BY id DESC LIMIT 1;

    // 获取所有记录
    db.Find(&users)
    //// SELECT * FROM users;

    // 使用主键获取记录
    db.First(&user, 10)
    //// SELECT * FROM users WHERE id = 10;
```

### 2.2. Where查询条件 (简单SQL)

```go
    // 获取第一个匹配记录
    db.Where("name = ?", "jinzhu").First(&user)
    //// SELECT * FROM users WHERE name = 'jinzhu' limit 1;

    // 获取所有匹配记录
    db.Where("name = ?", "jinzhu").Find(&users)
    //// SELECT * FROM users WHERE name = 'jinzhu';

    db.Where("name <> ?", "jinzhu").Find(&users)

    // IN
    db.Where("name in (?)", []string{"jinzhu", "jinzhu 2"}).Find(&users)

    // LIKE
    db.Where("name LIKE ?", "%jin%").Find(&users)

    // AND
    db.Where("name = ? AND age >= ?", "jinzhu", "22").Find(&users)

    // Time
    db.Where("updated_at > ?", lastWeek).Find(&users)

    db.Where("created_at BETWEEN ? AND ?", lastWeek, today).Find(&users)
```

### 2.3. Where查询条件 (Struct & Map)

注意：当使用struct查询时，GORM将只查询那些具有值的字段

```go
    // Struct
    db.Where(&User{Name: "jinzhu", Age: 20}).First(&user)
    //// SELECT * FROM users WHERE name = "jinzhu" AND age = 20 LIMIT 1;

    // Map
    db.Where(map[string]interface{}{"name": "jinzhu", "age": 20}).Find(&users)
    //// SELECT * FROM users WHERE name = "jinzhu" AND age = 20;

    // 主键的Slice
    db.Where([]int64{20, 21, 22}).Find(&users)
    //// SELECT * FROM users WHERE id IN (20, 21, 22);
```

### 2.4. Not条件查询

```go
    db.Not("name", "jinzhu").First(&user)
    //// SELECT * FROM users WHERE name <> "jinzhu" LIMIT 1;

    // Not In
    db.Not("name", []string{"jinzhu", "jinzhu 2"}).Find(&users)
    //// SELECT * FROM users WHERE name NOT IN ("jinzhu", "jinzhu 2");

    // Not In slice of primary keys
    db.Not([]int64{1,2,3}).First(&user)
    //// SELECT * FROM users WHERE id NOT IN (1,2,3);

    db.Not([]int64{}).First(&user)
    //// SELECT * FROM users;

    // Plain SQL
    db.Not("name = ?", "jinzhu").First(&user)
    //// SELECT * FROM users WHERE NOT(name = "jinzhu");

    // Struct
    db.Not(User{Name: "jinzhu"}).First(&user)
    //// SELECT * FROM users WHERE name <> "jinzhu";
```

### 2.5. 带内联条件的查询

注意：使用主键查询时，应仔细检查所传递的值是否为有效主键，以避免SQL注入

```go
    // 按主键获取
    db.First(&user, 23)
    //// SELECT * FROM users WHERE id = 23 LIMIT 1;

    // 简单SQL
    db.Find(&user, "name = ?", "jinzhu")
    //// SELECT * FROM users WHERE name = "jinzhu";

    db.Find(&users, "name <> ? AND age > ?", "jinzhu", 20)
    //// SELECT * FROM users WHERE name <> "jinzhu" AND age > 20;

    // Struct
    db.Find(&users, User{Age: 20})
    //// SELECT * FROM users WHERE age = 20;

    // Map
    db.Find(&users, map[string]interface{}{"age": 20})
    //// SELECT * FROM users WHERE age = 20;
```

### 2.6. Or条件查询

```go
    db.Where("role = ?", "admin").Or("role = ?", "super_admin").Find(&users)
    //// SELECT * FROM users WHERE role = 'admin' OR role = 'super_admin';

    // Struct
    db.Where("name = 'jinzhu'").Or(User{Name: "jinzhu 2"}).Find(&users)
    //// SELECT * FROM users WHERE name = 'jinzhu' OR name = 'jinzhu 2';

    // Map
    db.Where("name = 'jinzhu'").Or(map[string]interface{}{"name": "jinzhu 2"}).Find(&users)
```

### 2.7. 查询链

Gorm有一个可链接的API，你可以这样使用它

```go
    db.Where("name <> ?","jinzhu").Where("age >= ? and role <> ?",20,"admin").Find(&users)
    //// SELECT * FROM users WHERE name <> 'jinzhu' AND age >= 20 AND role <> 'admin';

    db.Where("role = ?", "admin").Or("role = ?", "super_admin").Not("name = ?", "jinzhu").Find(&users)
```

### 2.8. 扩展查询选项

```go
    // 为Select语句添加扩展SQL选项
    db.Set("gorm:query_option", "FOR UPDATE").First(&user, 10)
    //// SELECT * FROM users WHERE id = 10 FOR UPDATE;
```

### 2.9. FirstOrInit

获取第一个匹配的记录，或者使用给定的条件初始化一个新的记录（仅适用于struct，map条件）

```go
    // Unfound
    db.FirstOrInit(&user, User{Name: "non_existing"})
    //// user -> User{Name: "non_existing"}

    // Found
    db.Where(User{Name: "Jinzhu"}).FirstOrInit(&user)
    //// user -> User{Id: 111, Name: "Jinzhu", Age: 20}
    db.FirstOrInit(&user, map[string]interface{}{"name": "jinzhu"})
    //// user -> User{Id: 111, Name: "Jinzhu", Age: 20}
```

### 2.10. Attrs

如果未找到记录，则使用参数初始化结构

```go
    // Unfound
    db.Where(User{Name: "non_existing"}).Attrs(User{Age: 20}).FirstOrInit(&user)
    //// SELECT * FROM USERS WHERE name = 'non_existing';
    //// user -> User{Name: "non_existing", Age: 20}

    db.Where(User{Name: "non_existing"}).Attrs("age", 20).FirstOrInit(&user)
    //// SELECT * FROM USERS WHERE name = 'non_existing';
    //// user -> User{Name: "non_existing", Age: 20}

    // Found
    db.Where(User{Name: "Jinzhu"}).Attrs(User{Age: 30}).FirstOrInit(&user)
    //// SELECT * FROM USERS WHERE name = jinzhu';
    //// user -> User{Id: 111, Name: "Jinzhu", Age: 20}
```

### 2.11. Assign

将参数分配给结果，不管它是否被找到

```go
    db.Where(User{Name: "non_existing"}).Assign(User{Age: 20}).FirstOrInit(&user)
    //// user -> User{Name: "non_existing", Age: 20}

    // Found
    db.Where(User{Name: "Jinzhu"}).Assign(User{Age: 30}).FirstOrInit(&user)
    //// SELECT * FROM USERS WHERE name = jinzhu';
    //// user -> User{Id: 111, Name: "Jinzhu", Age: 30}
```

### 2.12. FirstOrCreate

获取第一个匹配的记录，或创建一个具有给定条件的新记录（仅适用于struct, map条件）

```go
    // Unfound
    db.FirstOrCreate(&user, User{Name: "non_existing"})
    //// INSERT INTO "users" (name) VALUES ("non_existing");
    //// user -> User{Id: 112, Name: "non_existing"}

    // Found
    db.Where(User{Name: "Jinzhu"}).FirstOrCreate(&user)
    //// user -> User{Id: 111, Name: "Jinzhu"}
```

### 2.13. Attrs

如果未找到记录，则为参数分配结构

```go
    // Unfound
    db.Where(User{Name: "non_existing"}).Attrs(User{Age: 20}).FirstOrCreate(&user)
    //// SELECT * FROM users WHERE name = 'non_existing';
    //// INSERT INTO "users" (name, age) VALUES ("non_existing", 20);
    //// user -> User{Id: 112, Name: "non_existing", Age: 20}

    // Found
    db.Where(User{Name: "jinzhu"}).Attrs(User{Age: 30}).FirstOrCreate(&user)
    //// SELECT * FROM users WHERE name = 'jinzhu';
    //// user -> User{Id: 111, Name: "jinzhu", Age: 20}
```

### 2.14. Assign

将其分配给记录，而不管它是否被找到，并保存回数据库。

```go
    // Unfound
    db.Where(User{Name: "non_existing"}).Assign(User{Age: 20}).FirstOrCreate(&user)
    //// SELECT * FROM users WHERE name = 'non_existing';
    //// INSERT INTO "users" (name, age) VALUES ("non_existing", 20);
    //// user -> User{Id: 112, Name: "non_existing", Age: 20}

    // Found
    db.Where(User{Name: "jinzhu"}).Assign(User{Age: 30}).FirstOrCreate(&user)
    //// SELECT * FROM users WHERE name = 'jinzhu';
    //// UPDATE users SET age=30 WHERE id = 111;
    //// user -> User{Id: 111, Name: "jinzhu", Age: 30}
```

### 2.15. Select

指定要从数据库检索的字段，默认情况下，将选择所有字段;

```go
    db.Select("name, age").Find(&users)
    //// SELECT name, age FROM users;

    db.Select([]string{"name", "age"}).Find(&users)
    //// SELECT name, age FROM users;

    db.Table("users").Select("COALESCE(age,?)", 42).Rows()
    //// SELECT COALESCE(age,'42') FROM users;
```

### 2.16. Order

在从数据库检索记录时指定顺序，将重排序设置为true以覆盖定义的条件

```go
    db.Order("age desc, name").Find(&users)
    //// SELECT * FROM users ORDER BY age desc, name;

    // Multiple orders
    db.Order("age desc").Order("name").Find(&users)
    //// SELECT * FROM users ORDER BY age desc, name;

    // ReOrder
    db.Order("age desc").Find(&users1).Order("age", true).Find(&users2)
    //// SELECT * FROM users ORDER BY age desc; (users1)
    //// SELECT * FROM users ORDER BY age; (users2)
```

### 2.17. Limit

指定要检索的记录数

```go
    db.Limit(3).Find(&users)
    //// SELECT * FROM users LIMIT 3;

    // Cancel limit condition with -1
    db.Limit(10).Find(&users1).Limit(-1).Find(&users2)
    //// SELECT * FROM users LIMIT 10; (users1)
    //// SELECT * FROM users; (users2)
```

### 2.18. Offset

指定在开始返回记录之前要跳过的记录数

```go
    db.Offset(3).Find(&users)
    //// SELECT * FROM users OFFSET 3;

    // Cancel offset condition with -1
    db.Offset(10).Find(&users1).Offset(-1).Find(&users2)
    //// SELECT * FROM users OFFSET 10; (users1)
    //// SELECT * FROM users; (users2)
```

### 2.19 Count

获取模型的记录数

```go
    db.Where("name = ?", "jinzhu").Or("name = ?", "jinzhu 2").Find(&users).Count(&count)
    //// SELECT * from USERS WHERE name = 'jinzhu' OR name = 'jinzhu 2'; (users)
    //// SELECT count(*) FROM users WHERE name = 'jinzhu' OR name = 'jinzhu 2'; (count)

    db.Model(&User{}).Where("name = ?", "jinzhu").Count(&count)
    //// SELECT count(*) FROM users WHERE name = 'jinzhu'; (count)

    db.Table("deleted_users").Count(&count)
    //// SELECT count(*) FROM deleted_users;
```

### 2.20. Group & Having

```go
    rows, err := db.Table("orders").Select("date(created_at) as date, sum(amount) as total").Group("date(created_at)").Rows()
    for rows.Next() {
        ...
    }

    rows, err := db.Table("orders").Select("date(created_at) as date, sum(amount) as total").Group("date(created_at)").Having("sum(amount) > ?", 100).Rows()
    for rows.Next() {
        ...
    }

    type Result struct {
        Date  time.Time
        Total int64
    }
    db.Table("orders").Select("date(created_at) as date, sum(amount) as total").Group("date(created_at)").Having("sum(amount) > ?", 100).Scan(&results)
```

### 2.21. Join

指定连接条件

```go
    rows, err := db.Table("users").Select("users.name, emails.email").Joins("left join emails on emails.user_id = users.id").Rows()
    for rows.Next() {
        ...
    }

    db.Table("users").Select("users.name, emails.email").Joins("left join emails on emails.user_id = users.id").Scan(&results)

    // 多个连接与参数
    db.Joins("JOIN emails ON emails.user_id = users.id AND emails.email = ?", "jinzhu@example.org").Joins("JOIN credit_cards ON credit_cards.user_id = users.id").Where("credit_cards.number = ?", "411111111111").Find(&user)
```

### 2.22. Pluck

将模型中的单个列作为地图查询，如果要查询多个列，可以使用Scan

```go
    var ages []int64
    db.Find(&users).Pluck("age", &ages)

    var names []string
    db.Model(&User{}).Pluck("name", &names)

    db.Table("deleted_users").Pluck("name", &names)

    // 要返回多个列，做这样：
    db.Select("name, age").Find(&users)
```

### 2.23. Scan

将结果扫描到另一个结构中。

```go
    type Result struct {
        Name string
        Age  int
    }

    var result Result
    db.Table("users").Select("name, age").Where("name = ?", 3).Scan(&result)

    // Raw SQL
    db.Raw("SELECT name, age FROM users WHERE name = ?", 3).Scan(&result)
```

### 2.24. Scopes

将当前数据库连接传递到`func(*DB) *DB`，可以用于动态添加条件

```go
    func AmountGreaterThan1000(db *gorm.DB) *gorm.DB {
        return db.Where("amount > ?", 1000)
    }

    func PaidWithCreditCard(db *gorm.DB) *gorm.DB {
        return db.Where("pay_mode_sign = ?", "C")
    }

    func PaidWithCod(db *gorm.DB) *gorm.DB {
        return db.Where("pay_mode_sign = ?", "C")
    }

    func OrderStatus(status []string) func (db *gorm.DB) *gorm.DB {
        return func (db *gorm.DB) *gorm.DB {
            return db.Scopes(AmountGreaterThan1000).Where("status in (?)", status)
        }
    }

    db.Scopes(AmountGreaterThan1000, PaidWithCreditCard).Find(&orders)
    // 查找所有信用卡订单和金额大于1000

    db.Scopes(AmountGreaterThan1000, PaidWithCod).Find(&orders)
    // 查找所有COD订单和金额大于1000

    db.Scopes(OrderStatus([]string{"paid", "shipped"})).Find(&orders)
    // 查找所有付费，发货订单
```

### 2.25. 指定表名

```go
    // 使用User结构定义创建`deleted_users`表
    db.Table("deleted_users").CreateTable(&User{})

    var deleted_users []User
    db.Table("deleted_users").Find(&deleted_users)
    //// SELECT * FROM deleted_users;

    db.Table("deleted_users").Where("name = ?", "jinzhu").Delete()
    //// DELETE FROM deleted_users WHERE name = 'jinzhu';
```

## 3. Gorm更新

### 3.1. 更新全部字段

Save将包括执行更新SQL时的所有字段，即使它没有更改

```go
    db.First(&user)

    user.Name = "jinzhu 2"
    user.Age = 100
    db.Save(&user)

    //// UPDATE users SET name='jinzhu 2', age=100, birthday='2016-01-01', updated_at = '2013-11-17 21:34:10' WHERE id=111;
```

### 3.2. 更新更改字段

如果只想更新更改的字段，可以使用Update,Updates

```go
    // 更新单个属性（如果更改）
    db.Model(&user).Update("name", "hello")
    //// UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE id=111;

    // 使用组合条件更新单个属性
    db.Model(&user).Where("active = ?", true).Update("name", "hello")
    //// UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE id=111 AND active=true;

    // 使用`map`更新多个属性，只会更新这些更改的字段
    db.Model(&user).Updates(map[string]interface{}{"name": "hello", "age": 18, "actived": false})
    //// UPDATE users SET name='hello', age=18, actived=false, updated_at='2013-11-17 21:34:10' WHERE id=111;

    // 使用`struct`更新多个属性，只会更新这些更改的和非空白字段
    db.Model(&user).Updates(User{Name: "hello", Age: 18})
    //// UPDATE users SET name='hello', age=18, updated_at = '2013-11-17 21:34:10' WHERE id = 111;

    // 警告:当使用struct更新时，FORM将仅更新具有非空值的字段
    // 对于下面的更新，什么都不会更新为""，0，false是其类型的空白值
    db.Model(&user).Updates(User{Name: "", Age: 0, Actived: false})
```

### 3.3. 更新选择的字段

如果您只想在更新时更新或忽略某些字段，可以使用Select,Omit

```go
    db.Model(&user).Select("name").Updates(map[string]interface{}{"name": "hello", "age": 18, "actived": false})
    //// UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE id=111;

    db.Model(&user).Omit("name").Updates(map[string]interface{}{"name": "hello", "age": 18, "actived": false})
    //// UPDATE users SET age=18, actived=false, updated_at='2013-11-17 21:34:10' WHERE id=111;
```

### 3.4. 更新更改字段但不进行Callbacks

以上更新操作将执行模型的BeforeUpdate,AfterUpdate方法，更新其UpdatedAt时间戳，在更新时保存它的Associations，如果不想调用它们，可以使用UpdateColumn,UpdateColumns

```go
    // 更新单个属性，类似于`Update`
    db.Model(&user).UpdateColumn("name", "hello")
    //// UPDATE users SET name='hello' WHERE id = 111;

    // 更新多个属性，与“更新”类似
    db.Model(&user).UpdateColumns(User{Name: "hello", Age: 18})
    //// UPDATE users SET name='hello', age=18 WHERE id = 111;
```

### 3.5. Batch Updates 批量更新

Callbacks在批量更新时不会运行

```go
    db.Table("users").Where("id IN (?)", []int{10, 11}).Updates(map[string]interface{}{"name": "hello", "age": 18})
    //// UPDATE users SET name='hello', age=18 WHERE id IN (10, 11);

    // 使用struct更新仅适用于非零值，或使用map[string]interface{}
    db.Model(User{}).Updates(User{Name: "hello", Age: 18})
    //// UPDATE users SET name='hello', age=18;

    // 使用`RowsAffected`获取更新记录计数
    db.Model(User{}).Updates(User{Name: "hello", Age: 18}).RowsAffected
```

### 3.6. 使用SQL表达式更新

```go
    DB.Model(&product).Update("price", gorm.Expr("price * ? + ?", 2, 100))
    //// UPDATE "products" SET "price" = price * '2' + '100', "updated_at" = '2013-11-17 21:34:10' WHERE "id" = '2';

    DB.Model(&product).Updates(map[string]interface{}{"price": gorm.Expr("price * ? + ?", 2, 100)})
    //// UPDATE "products" SET "price" = price * '2' + '100', "updated_at" = '2013-11-17 21:34:10' WHERE "id" = '2';

    DB.Model(&product).UpdateColumn("quantity", gorm.Expr("quantity - ?", 1))
    //// UPDATE "products" SET "quantity" = quantity - 1 WHERE "id" = '2';

    DB.Model(&product).Where("quantity > 1").UpdateColumn("quantity", gorm.Expr("quantity - ?", 1))
    //// UPDATE "products" SET "quantity" = quantity - 1 WHERE "id" = '2' AND quantity > 1;
```

### 3.7. 在Callbacks中更改更新值

如果要使用BeforeUpdate,BeforeSave更改回调中的更新值，可以使用scope.SetColumn，例如

```go
    func (user *User) BeforeSave(scope *gorm.Scope) (err error) {
      if pw, err := bcrypt.GenerateFromPassword(user.Password, 0); err == nil {
        scope.SetColumn("EncryptedPassword", pw)
      }
    }
```

### 3.8. 额外更新选项

```go
    // 为Update语句添加额外的SQL选项
    db.Model(&user).Set("gorm:update_option", "OPTION (OPTIMIZE FOR UNKNOWN)").Update("name, "hello")
    //// UPDATE users SET name='hello', updated_at = '2013-11-17 21:34:10' WHERE id=111 OPTION (OPTIMIZE FOR UNKNOWN);
```

## 4. Gorm删除

### 4.1. 删除/软删除

警告删除记录时，需要确保其主要字段具有值，GORM将使用主键删除记录，如果主要字段为空，GORM将删除模型的所有记录

```go
    // 删除存在的记录
    db.Delete(&email)
    //// DELETE from emails where id=10;

    // 为Delete语句添加额外的SQL选项
    db.Set("gorm:delete_option", "OPTION (OPTIMIZE FOR UNKNOWN)").Delete(&email)
    //// DELETE from emails where id=10 OPTION (OPTIMIZE FOR UNKNOWN);
```

### 4.2. 批量删除

删除所有匹配记录

```go
    db.Where("email LIKE ?", "%jinzhu%").Delete(Email{})
    //// DELETE from emails where email LIKE "%jinhu%";

    db.Delete(Email{}, "email LIKE ?", "%jinzhu%")
    //// DELETE from emails where email LIKE "%jinhu%";
```

### 4.3. 软删除

如果模型有DeletedAt字段，它将自动获得软删除功能！ 那么在调用Delete时不会从数据库中永久删除，而是只将字段DeletedAt的值设置为当前时间。

```go
    db.Delete(&user)
    //// UPDATE users SET deleted_at="2013-10-29 10:23" WHERE id = 111;

    // 批量删除
    db.Where("age = ?", 20).Delete(&User{})
    //// UPDATE users SET deleted_at="2013-10-29 10:23" WHERE age = 20;

    // 软删除的记录将在查询时被忽略
    db.Where("age = 20").Find(&user)
    //// SELECT * FROM users WHERE age = 20 AND deleted_at IS NULL;

    // 使用Unscoped查找软删除的记录
    db.Unscoped().Where("age = 20").Find(&users)
    //// SELECT * FROM users WHERE age = 20;

    // 使用Unscoped永久删除记录
    db.Unscoped().Delete(&order)
    //// DELETE FROM orders WHERE id=10;
```

## 5. Gorm错误处理

### 5.1. 错误处理

执行任何操作后，如果发生任何错误，GORM将其设置为`*DB`的Error字段

```go
    if err := db.Where("name = ?", "jinzhu").First(&user).Error; err != nil {
        // 错误处理...
    }

    // 如果有多个错误发生，用`GetErrors`获取所有的错误，它返回`[]error`
    db.First(&user).Limit(10).Find(&users).GetErrors()

    // 检查是否返回RecordNotFound错误
    db.Where("name = ?", "hello world").First(&user).RecordNotFound()

    if db.Model(&user).Related(&credit_card).RecordNotFound() {
        // 没有信用卡被发现处理...
    }
```

## 6. Gorm事务

### 6.1. 事物

要在事务中执行一组操作，一般流程如下。

```go
    // 开始事务
    tx := db.Begin()

    // 在事务中做一些数据库操作（从这一点使用'tx'，而不是'db'）
    tx.Create(...)

    // ...

    // 发生错误时回滚事务
    tx.Rollback()

    // 或提交事务
    tx.Commit()
```

一个具体的例子

```go
    func CreateAnimals(db *gorm.DB) err {
      tx := db.Begin()
      // 注意，一旦你在一个事务中，使用tx作为数据库句柄

      if err := tx.Create(&Animal{Name: "Giraffe"}).Error; err != nil {
         tx.Rollback()
         return err
      }

      if err := tx.Create(&Animal{Name: "Lion"}).Error; err != nil {
         tx.Rollback()
         return err
      }

      tx.Commit()
      return nil
    }
```

## 7.Sql构建

### 7.1. 执行原生SQL

```go
    db.Exec("DROP TABLE users;")
    db.Exec("UPDATE orders SET shipped_at=? WHERE id IN (?)", time.Now, []int64{11,22,33})

    // Scan
    type Result struct {
        Name string
        Age  int
    }

    var result Result
    db.Raw("SELECT name, age FROM users WHERE name = ?", 3).Scan(&result)
```

### 7.2. sql.Row & sql.Rows

获取查询结果为`*sql.Row`或`*sql.Rows`

```go
    row := db.Table("users").Where("name = ?", "jinzhu").Select("name, age").Row() // (*sql.Row)
    row.Scan(&name, &age)

    rows, err := db.Model(&User{}).Where("name = ?", "jinzhu").Select("name, age, email").Rows() // (*sql.Rows, error)
    defer rows.Close()
    for rows.Next() {
        ...
        rows.Scan(&name, &age, &email)
        ...
    }

    // Raw SQL
    rows, err := db.Raw("select name, age, email from users where name = ?", "jinzhu").Rows() // (*sql.Rows, error)
    defer rows.Close()
    for rows.Next() {
        ...
        rows.Scan(&name, &age, &email)
        ...
    }
```

### 7.3. 迭代中使用sql.Rows的Scan

```go
    rows, err := db.Model(&User{}).Where("name = ?", "jinzhu").Select("name, age, email").Rows() // (*sql.Rows, error)
    defer rows.Close()

    for rows.Next() {
      var user User
      db.ScanRows(rows, &user)
      // do something
    }
```