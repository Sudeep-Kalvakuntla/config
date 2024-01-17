"Enable mouse support"
set mouse=a

"Enable syntax"
syntax on

"Enable line numbers"
set number

"Enable relative line numbers"
set relativenumber

"Enable highlight search pattern"
set hlsearch

"Enable smartcase search sensitivity"
set ignorecase
set smartcase

"Indentation"
set tabstop =4
set softtabstop =4
set shiftwidth =4
set expandtab
set autoindent
filetype indent on

"Show the matching part of the pairs (), [], {}"
set showmatch

"Enable true colours support"
set termguicolors

"Set colorscheme"
colorscheme catppuccin_macchiato
"colorscheme slate"

"Automatically close brackets"
inoremap ( ()<Left>
inoremap [ []<Left>
inoremap { {}<Left>
inoremap " ""<Left>

"Highlights current line"
set cursorline

