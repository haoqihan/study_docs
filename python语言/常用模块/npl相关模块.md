jieba库的使用

介绍

```shell
中文文本需要通过分词获得单个词语的信息
jieba库提供三种分词模式，支持自定义词典
```

```shel
# 三种分词模式
- 精确模式：将文本精确切开，分词无冗余，适合文本分词
- 全模式：把文本中所有可能成词的词语扫描出来，速度快，不能解决歧义
- 搜索引擎模式：在精确模式基础上，对长词再次切分，提高召回率
```

| 函数                            | 描述                                                       |
| ------------------------------- | ---------------------------------------------------------- |
| jieba.cut(s)                    | 精确模式，分词后返回一个迭代器，用for..in 形式便利结果     |
| jieba.lcut(s)                   | 精确模式，分词后返回一个列表                               |
| jieba.cut(s，cut_all=True)      | 全模式，分词返回一个迭代器，用for..in 形式便利结果         |
| jieba.cut(s，cut_all=True)      | 全模式，分词后返回一个列表                                 |
| jieba.cut_for_search("新时代")  | 搜索引擎模式，分词后返回一个迭代器，用for..in 形式便利结果 |
| jieba.lcut_for_search("新时代") | 搜索引擎模式，分词后返回一个列表                           |
| jieba.add_word(w)               | 向分词词典增加新词w                                        |

### wordcloud库的使用

介绍

```shell
wordcloud.WordCloud() 代表一个文本对应的词云
可以根据文本中词语出现的频率等参数绘制词云
绘制词云的形状、尺寸和颜色等可以设定
```

常用用法

```python
w = wordcloud.WordCloud() 
以WordCloud对象为基础
配置参数、加载文本、输出文件
```

方法

| 方法                | 描述                             |
| ------------------- | -------------------------------- |
| w.generate(txt)     | 向WordCloud对象w中加载文本txt    |
| w.to_file(filename) | 将词云输出为图像文件，.png或.jpg |
|                     |                                  |

WordCloud参数

| 参数             | 描述                                                       |
| ---------------- | ---------------------------------------------------------- |
| width            | 指定词云对象生成图片的宽度，默认为400像素                  |
| height           | 指定词云对象生成图片的高度，默认为200像素                  |
| min_font_size    | 指定词云中最小字号，默认为4号                              |
| max_font_size    | 指定词云中字体的最大字号，根据高度自动调节                 |
| font_step        | 指定词云中字体字号的步进间隔，默认为1                      |
| font_path        | 指定字体文件的路径，默认为None  例子：font_path=“msyh.ttc” |
| mask             | 指定词云形状，需要引用 imread() 函数，默认为长方形         |
| background_color | 指定词云的背景颜色                                         |
|                  |                                                            |

例子：

```python
import wordcloud
w = wordcloud.WordCloud()  # 步骤一、配置对象参数
w.generate("one python")   # 步骤二、加载词云文本
w.to_file("zz.png")       # 步骤三、输出词云文件
```

