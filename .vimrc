let mapleader = ","

set termguicolors

filetype on
syntax enable
filetype plugin on
filetype indent on

set number relativenumber
set ruler
set shiftwidth=4
set tabstop=4
set wildmenu
set autoread
set so=3

set hidden
set nohlsearch

set lazyredraw
set noerrorbells
set novisualbell
set t_vb=
set tm=500
set regexpengine=0
set nobackup
set background=dark
set encoding=utf-8
set termguicolors
set nowb
set noswapfile

" let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
" let &t_8b = "\<Esc>[48:2;%lu;%lu;%lum"

set smarttab
set ai
set si
set wrap
set backspace=eol,start,indent
set whichwrap+=<,>,h,l
set laststatus=2
set ignorecase

" map <leader>r :CocCommand workspace.renameCurrentFile<CR>
map <leader>vj :split<CR><C-W>j
map <leader>vk :split<CR>
map <leader>vl :vsplit<CR><C-W>l
map <leader>vh :vsplit<CR>
map <leader>l :bnext<CR>
map <leader>h :bprevious<CR>
map <leader>dd :bdelete<CR>
map <leader>s :FZF --reverse --info=inline /home/caracole<CR>
map <leader>S :FZF --reverse --info=inline /<CR>
map <leader>f :Files<CR>
map <leader>b :Buffers<CR>
map <leader>c :Colors<CR>
map! ;; <Esc>

nmap oo o<Esc>k
nmap OO O<Esc>j

let g:fzf_action = {
	\ 'ctrl-n': 'tab split',
	\ 'ctrl-k': 'split',
	\ 'ctrl-h': 'vsplit' }

call plug#begin('~/.vim/plugged')
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'ghifarit53/tokyonight-vim'
Plug 'jiangmiao/auto-pairs'
call plug#end()

let g:airline_powerline_fonts=1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#fnamemod = ':p:.:gs?/? > ?'

au BufReadPost * if line("'\"") > 1 && line("'\"") < line("$") | exe "normal! g'\"" | endif

inoremap <expr> <cr> coc#pum#visible() ? coc#pum#confirm() : "\<CR>"
inoremap <silent><expr> <cr> coc#pum#visible() ? coc#_select_confirm() :  "\<C-g>u\<CR>"

let g:tokyonight_style = 'night'
let g:tokyonight_enable_italic = 1
let g:airline_theme = "tokyonight"

colorscheme tokyonight

let g:flake8_show_in_gutter=1
