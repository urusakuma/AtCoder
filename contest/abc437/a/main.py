import sys
from typing import List, Tuple, Any  # type: ignore

# 高速入力


def input() -> str:
    return sys.stdin.readline().strip()

# 配列入力


def map_int() -> List[int]:
    return list(map(int, input().split()))


# 二次配列
_ = [[0]*10 for _ in range(10)]


def main():
    N, M = map(int, input().split())

    ans = solve(N, M)

    answer(ans)

# 問題を解く


def solve(N: int, M: int) -> Any:
    a = N*12

    return a+M

# 回答を出力する


def answer(ans: Any) -> None:
    print(ans)


if __name__ == "__main__":
    main()
