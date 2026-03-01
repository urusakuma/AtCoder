cd /atcoder_python/contest

# 例: contest ディレクトリ名が abc075, abc076, arc001 など
for contest in *; do
  [ -d "$contest" ] || continue
  echo "=== contest: $contest ==="

  cd "$contest"

  # 例: a, b, c, d ディレクトリがある前提
  for task in *; do
    [ -d "$task" ] || continue
    echo "  task: $task"

    mkdir -p "$task/tests"
    (
      cd "$task"
      oj d "https://atcoder.jp/contests/${contest}/tasks/${contest}_${task}" -d tests
    )
  done

  cd ..
done
