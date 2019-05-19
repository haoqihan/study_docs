### pyquery库的基本使用

#### 基本使用

```python
from pyquery import PyQuery as py
doc = py(html)
print(doc('p'))# 也可以:.p1或#p1
```

#### url初始化

```python
doc = py(url='http://www.baidu.com')
print(doc('head'))
```

#### 文件初始化

```python
doc = py(filename='demo.html')
print(doc('head'))
```

#### 基本css选择器

```python
doc = py(html)
print(doc('#list_1 .a1 ' ))
```

#### 查找元素

##### 子元素

- 所有的

	- ```python
		doc = py(html)
		item = doc('#list_1')
		print(item.find('a'))
		```

- 直接的

	- ```python
		doc = py(html)
		item = doc('#list_1')
		print(item.children())
		```

- 子元素筛选

	- ```python
		item = doc('#list_1')
		print(item.children('.a1'))
		```

父元素

```python
item = doc('#list_1')
print(item.parent())
```

祖先节点

```python
item = doc('#list_1')
print(item.parents())
```

对父节点在进一次筛选

```python
item = doc('#list_1')
print(item.parent('.r1'))
```

兄弟节点

```python
item = doc('#list_1')
print(item.siblings())
```

对兄弟元素进行筛选

```python
item = doc('#list_1')
print(item.siblings('.a1'))
```

### 遍历

单个元素

```python
item = doc('#list_1')
print(item)
```

返回迭代器

```python
item = doc('#list_1').items()
print(item)
```

### 获取信息

获取属性

```python
item = doc('#list_1 a')
print(item.attr('href'))
print(item.attr.href)
```

获取文本

```python
item = doc('#list_1 a') print(item.text())
```

获取html内容

```python
item = doc('#list_1') print(item.html())
```

### DOM操作

addClass和removeClass

```python 
item = doc('#list_1')
print(item.remove_class('p1')) :删除p1
print(item.add_class('p1')):添加p1
```

attr和css

```python
item = doc('#list_1')
print(item.attr('name','link'))
print(item.css('font_size','14px'))
```

remove:把中间a标签全部删除

```python
item = doc('#list_1')
print(item.text())
print(item.find('a').remove())
print(item.text())
```

### 伪类选择器

```python
doc = py(html) print(doc('p:first-child')) # 获取第一个
print(doc('p:last-child'))# 获取最后一个
print(doc('p:nth-child(2)'))# 获取第二个
print(doc('p:gt(1)')) # 获取比1大的所有元素
print(doc('p:nth-child(2n)')) # 获取偶数的
print(doc('p:contains(xxx)')) #查看包含xxx文本的所有内容
```

