if [ -f ~/.bashrc ]; then . ~/.bashrc; fi

export GOROOT=/usr/local/go/
export GOPATH=$HOME/work/go
export PATH=$PATH:~/bin:$GOROOT/bin:$GOPATH/bin

#parse_git_branch() {
#	git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
#}
#export PS1="\u@\h \W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "


# git pretty
function parse_git_dirty {
  [[ $(git status 2> /dev/null | tail -n1) != "nothing to commit (working directory clean)" ]] && echo "*"
  }
  function parse_git_branch {
    git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e "s/* \(.*\)/[\1$(parse_git_dirty)]/"
}
export PS1='CAB: \[\033[1;33m\]\w\[\033[0m\]$(parse_git_branch)$'


[[ -s ~/.docker_profile ]] && source ~/.docker_profile
export PATH=/usr/local/sbin:$PATH

#ruby stuff
if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi
