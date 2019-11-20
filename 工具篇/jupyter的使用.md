##### 安装前提

- 安装Jupyter Notebook的前提是需要安装了Python（3.3版本及以上，或2.7版本）

##### 安装

```python
pip3 install jupyter
```

##### 运行jupyter

```shell
jupyter notebook --help  					# 查看文档
jupyter notebook 							# 默认启动
jupyter notebook --port <port_number>		# 指定端口启动
jupyter notebook --no-browser				# 启动服务器但不打开浏览器
```

##### 添加语言

##### **python**

```shell
python -m ipykernel install --user --name=nlp  # 添加jupyter服务
```

##### go

```shell
# linux
$ go get -u github.com/gopherdata/gophernotes
$ mkdir -p ~/.local/share/jupyter/kernels/gophernotes
$ cp $GOPATH/src/github.com/gopherdata/gophernotes/kernel/* ~/.local/share/jupyter/kernels/gophernotes
# 详情参考
地址：https://github.com/gopherdata/gophernotes
```

##### jupyter 制作幻灯片

```shell
pip3 install RISE
jupyter-nbextension install rise --py --sys-prefix
jupyter-nbextension enable rise --py --sys-prefix
```

更改notebook 显示样式

```shell
# 1.下载jupyterthemes
pip install --upgrade jupyterthemes
# 2.查看样式包（命令行）
jt -l
# 3.修改样式
jt -t chesterish -T -N
```

#### 扩展包

```shell
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

##### 推荐以下几个插件：

- `Code prettify`，对代码进行格式化；
- `Collapsible Headings`，可以根据headings折叠区域；
- `Codefolding`，可以对代码块进行折叠；
- `ScrollDown`，当代码输出内容过长，自动下拉滚动条；
- `Table of Contents (2)`，根据markdown的标题栏自动生成目录，有个按钮，可以自动添加数字编号！！！；





