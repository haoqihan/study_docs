#### 如何编写vim配置

- linux、Unix下新建一个隐藏文件vim  ~/.vimrc
- windows系统vim $MYCIMRC ,通过环境变量编辑配置文件
- 常用设置：set number 设置行号，colorscheme default 设置主题
- 常用的vim映射设置，noremap <leader> w : w <cr> 保存文件
- 自定义的vimscript函数和插件的配置

#### 常用设置

- 我们可以把常用的设置写到.vimrc里避免每次打开vim重新设置
- 比如设置行号：set number
- 也可以参照其他人的设置

#### vim中的映射

- 设置一下leader键 let mapleader = “,” 常用逗号或空格
- 比如用inoremap <leader>w <Esc>:w<cr> 在插入模式下保存
- vim中的映射比较复杂，但是十分强大

#### vim的插件

- 通过插件可以让你无限扩充vimm的功能
- 想要使用插件需要具备一定的vim配置知识

#### vim脚本

- vim脚本对于vim高级玩家来说可以实现强大的vim插件
- vim是一个简单的脚本语言

### 模式映射

#### vim常用模式normal、visual、insert都可以定义映射

- 用nmap、vmap、imap定义映射只在normal、visual、insert分别有效
- :vmap \ U把在visual模式下选中的文件大小（u、U转换大小写）

### 非递归映射

- 使用*map 对应nnoremap、vnoremap、inoremap
- 何时使用递归映射（*map）？何时使用非递归映射（\*nnoremap）
- 任何时候你都应使用非递归映射，拯救自己和插件作者



