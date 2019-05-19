### bs4的基本使用方法 

### 实例

```python
from bs4 import BeautifulSoup
html = "<html><title class='xxx'>111111</title> "
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())  #自动补全代码
print(soup.title.string)#获取title标签的代码
```

### 标签选择器

- **获取名称:**print(soup.title.name)
- **获取属性:** print(soup.p.attrs['name']) 和 print(soup.p['name'])
- **获取内容:** print(soup.p.string)
- **嵌套选择:**print(soup.head.title.string)
- **子节点和子孙节点**
	- print(soup.body.contents):返回一个列表
	- print(soup.body.children):放回一个迭代器
	- soup.body.descendants :所有的子孙节点,也是一个迭代器
- **父节点和祖先节点**
	- print(soup.a.parent) :父节点,只有一个
	- soup.a.parents :祖先节点
- **兄弟节点**
	- print(list(soup.p.next_siblings))
	- print(list(soup.p.previous_siblings))

### 标准选择器

- **根据标签**:print(soup.find_all('ul'))
- **根据属性:**
	- print(soup.find_all(attrs={'id':'list_1'}))
	- print(soup.find_all(id='list_1'))
	- print(soup.find_all(class_='p1'))
- **根据文本**:print(soup.find_all(text=[777,666,888]))
- **返回单个元素:find**()
	- print(soup.find_parent('title')) :返回父节点
	- print(soup.find_parents('title')):返回祖先节点
	- print(soup.find_next_siblings('p')) :返回兄弟节点
	- print(soup.find_next_sibling('p'))返回兄弟节点
- **css选择器**
	- print(soup.select('.p1 .a1'))
	- print(soup.select('#list_1 .a1'))
- **获取属性**:

**获取内容**

```python
for i in soup.select('#list_1 .a1'):
	print(i.get_text())
	print(i.text)
```

