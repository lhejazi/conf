execute pathogen#infect()

filetype off
call pathogen#incubate()
call pathogen#helptags()

filetype on		" try to detect filetypes
syntax on		" syntax highlighting
syntax enable
filetype plugin indent on		" enabled loading indent file
					" for filetype

"let g:pyflakes_use_quickfix = 0
map <leader>td <Plug>TaskList

let g:pep8_map='<leader>8'		"pep8 makes sure your code is consistent accross projects	

map <leader>g :GundoToggle<CR>

map <D-C> <S-'><S-8>y

set foldmethod=indent   " for code folding (hiding inside funcionts)
set foldlevel=99        " to open/close fold type 'za'

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

set backspace=indent,eol,start  " make that backspace key work the way it should

set expandtab		"insert space characters whenever the tab key is pressed
set tabstop=4		"whenever the tab key is pressed, four spaces will be used
set shiftwidth=4	"change the number of space characters inserted for indentations

set guifont=Menlo:h14


"""""" Go Settings

" Syntax highliting for functions, methods, and structs
let g:go_highlight_functions = 1
let g:go_highlight_methods = 1
let g:go_highlight_structs = 1

" Move cursor to definition location if in the same file.
let g:godef_same_file_in_same_window=1

"" Syntastic recommended Settings
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0  " check on disk write

filetype on             " detect type of file
filetype indent on      " load indent file for specific file type
filetype plugin on 

set t_Co=256
set spell		" set the spell check on

autocmd FileType javascript setlocal shiftwidth=2 tabstop=2
autocmd FileType jade setlocal shiftwidth=2 tabstop=2
autocmd FileType coffee setlocal shiftwidth=2 tabstop=2
autocmd FileType coffeescript setlocal shiftwidth=2 tabstop=2


" Add the virtualenv's site-packages to vim path

py << EOF
import os.path
import sys
import vim
if 'VIRTUAL_ENV' in os.environ:
    project_base_dir = os.environ['VIRTUAL_ENV']
    sys.path.insert(0, project_base_dir)
    activate_this = os.path.join(project_base_dir,
    'bin/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
EOF
