# 解答提出のためのマージ
alias m='python /atcoder_python/merge.py'

# コンテストフォルダへ移動
alias c='cd /atcoder_python/contest/'

# main.pyを開く
alias o='code main.py'

# 出力確認用
alias d='python main.py'

test() {
    if [ $# -eq 0 ]; then
        oj t -c "pypy3 main.py" -d ./tests/
    else
        pypy3 main.py < tests/sample-$1.in
    fi
}
n(){
    if [ -z "$1" ]; then
        echo "Usage: n <contest-id>"
        return 1
    fi
    cd /atcoder_python/contest/ 
    acc new $1 || return
    cd /atcoder_python/contest/$1
}