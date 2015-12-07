alias vi='/Applications/MacVim.app/Contents/MacOS/Vim'
export EDITOR=/usr/bin/gvim

export TMM_API_SETTINGS=/Users/lhejazi/twitter_config.py

parseTwurl() {
    /usr/local/bin/twurl $* | jq
}
alias twurl=parseTwurl
