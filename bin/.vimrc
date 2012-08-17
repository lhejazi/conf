set nocompatible        " use vim defaults
set scrolloff=3         " keep 3 lines when scrolling
set ai                  " set auto-indenting on for programming
set showcmd             " display incomplete commands

set nobackup            " do not keep a backup file
set number              " show line numbers
set ruler               " show the current row and column

set hlsearch            " highlight searches
set incsearch           " do incremental searching
set showmatch           " jump to matches when entering regexp
set ignorecase          " ignore case when searching
set smartcase           " no ignorecase if Uppercase char present

set visualbell t_vb=    " turn off error beep/flash
set novisualbell        " turn off visual bell
set vb			" turn off beep while in terminal
set backspace=indent,eol,start  " make that backspace key work the way it should

set textwidth=79	" setting the maximum line length to 80 chars

syntax on              " turn syntax highlighting on by default
filetype on             " detect type of file
filetype indent on      " load indent file for specific file type

set spell		" set the spell check on

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Moving around, tabs, windows and buffers
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
imap <C-j> <Down>
imap <C-h> <Left>
imap <C-k> <Up>
imap <C-l> <Right>
map <c-s> :w<cr>

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Colors and Fonts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set t_Co=256		" allowing 256 colors while working in the terminal

let g:solarized_termcolors=256
colorscheme solarized	
set background=light  " dark backgrounds

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Editing Files
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
map <S-Enter> o<Esc>	" while in command mode, insert a newline above current line

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Plugin Related Variables
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:checksyntax_auto = 1

au BufWritePost *.py CheckSyntax
