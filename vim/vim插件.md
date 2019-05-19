### 什么是插件

#### 和现在流行编辑器一样vim同样支持强大的插件扩展

- vim插件是使用vimscript或其他语言编写的vim功能扩展
- 编辑器自带的功能有限，有了插件之后几乎可以无限制的扩充功能
- 网络上比如github等都有很多vim插件可以使用

### 如何安装插件

#### 原始的方式直接clone插件代码，如何有很多插件管理器

- 目前vim有很多插件管理器可供选择，你可以选择一个顺手的
- 常见的有vim-plug，Vundle，Pathogen，Dein.vim，volt等
- 综合性能，易用性，文档等方面，推荐使用vim-plug

#### 如何寻找自己需要的插件

[地址](<https://vimawesome.com/>)

#### vim美化插件

- 修改启动界面：[地址](<https://github.com/mhinz/vim-startify>)
- 状态栏美化：[地址](https://github.com/vim-airline/vim-airline)
- 状态栏因为字体原因会乱码，[解决地址](https://powerline.readthedocs.io/en/latest/installation/linux.html)
- 增加代码缩进线条：[地址](https://github.com/Yggdroot/indentLine)

#### vim配色方案

- vim-hybird配色：[地址](https://github.com/w0ng/vim-hybrid)
- solarized配色：[地址](https://github.com/altercation/vim-colors-solarized)
- gruxbox配色：[地址](https://github.com/morhetz/gruvbox)

#### 文件管理器nerdtree

##### 使用nerdtree插件进行文件目录树管理

- [地址](https://github.com/scrooloose/nerdtree)
- autocmd vimenter * NERDTree 可以在启动vim的时候打开
- nnoremap <leader>v :NERDTreeFind<cr> 查找文件位置

### 模糊搜索器

#### 如果想快速查找并且打开一个文件可以使用ctrlp插件

- [地址](https://github.com/kien/ctrlp.vim)
- let g:ctrlp_map '<c-p>'
- 使用ctrl+p然后开始输入少量字符就可以搜索了

#### vim移动命令

- 比如w、e基于单词移动，gg、G文件首尾，0、$行首位，f（char）查询字符
- ctrl + f  和ctrl + u 前后翻屏

#### 如何移动到任意位置

##### 可以使用vim的搜索/加上n跳转，但是使用easymotion

- [地址](https://github.com/easymotion/vim-easymotion)
- 官方文档太长
-  nmap ss <Plug>(easymotion-s2)

#### 快速替换插件

##### 如果快速让你更换一对单引号为双引号，你会如何做

- 一个个的查找和更改，是不是很低效
- [地址](https://github.com/tpope/vim-surround)

#### vim-surround的使用

##### normal模式下增加，删除，修改成对内容

- ds  " 删除
- cs  (   [  更改
- ys iw   “  添加

#### 模糊搜索

#### fzf 与fzf.vim

##### fzf 是一个强大的命令行模糊搜索工具，fzf.vim集成到vim里

- [地址](https://github.com/junegunn/fzf.vim)
- 使用 Ag [PATTERN] 模糊搜索字符串 还需下载：apt-get install silversearcher-ag
- 使用Files [PATH] 模糊搜索目录



#### 搜索和替换插件far.vim

#### 如果想要批量搜索替换，可以试试far.vim

- [地址](https://github.com/brooth/far.vim)
- 重构代码比较常用
- :Far foo bar **/*.py
- :Fardo

#### vim-go

#### 功能强大的golang插件vim-go

- [地址](https://github.com/fatih/vim-go)
- 代码重构，补全，跳转，自动格式化，自动导入功能
- 基本满足golang日常开发
- 基本满足常用的基本使用

#### python-mode

- 













































终端下载字体
--------------------- 

```python
# Linux：
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20Sans%20Mono%20Nerd%20Font%20Complete.otf
# macOS (OS X)
cd ~/Library/Fonts && curl -fLo "Droid Sans Mono for Powerline Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/DroidSansMono/complete/Droid%20Sans%20Mono%20Nerd%20Font%20Complete.otf
参考地址：https://www.jianshu.com/p/61e14ee7bd6e
```



