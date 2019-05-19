---
title: vim的使用
date: 2019-01-16 13:24:54
tags: [vim]
categories: [linux]
---

### 常用指令

#### 底行模式常用指令

- ：w    写
- ：q    退出
- ：！    强制
- ：ls    列出打开的所有文件
- ：n    切换到后一个文件
- ：N    切换到上一个文件
- ：15    跳到15行
- /xxx    向后搜索
- ？xxx    向前搜索

#### 命令模式常用指令

- h    光标左移
- j    光标下移
- k    光标上移
- l    光标右移
- ctrl + f    向下翻页（front）
- ctrl + b    向上翻页（back）
- ctrl + d   向下翻半页（down）
- ctrl + u   向上翻半页（up）
- dd    删除光标所在行
- o    在光标所在行的下方插入一行并切换到输入模式
- yy    复制光标所在的行
- p    在光标所在行的下方粘贴
- P    在光标所在行的上方粘贴

### 打造自己的vim

```shell
# 常用设置
# 设置行号
set number
# 设置主题
colorscheme hybrid

# 按f2进入粘贴模式
set pastetoggle=<F2>

# 高亮搜索
set hlsearch

# 设置折叠方式
set foldmethod=indent

# 常用映射
# 使用jj进入normal 模式
inoremap jj <Esc>`^

# 插件设置
call plug#begin()
```

设置分4部分

- 常用设置
- 常用映射
- 插件的安装和配置
- 自定义函数（vimscript）