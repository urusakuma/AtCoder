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
    T = int(input())
    cases = [[0]*3 for _ in range(T)]
    for i in range(T):
        cases[i][0], cases[i][1], cases[i][2] = map(int, input())

    ans = solve(T, cases)

    answer(ans)


# 問題を解く


def solve(T: int, cases: List[List[int]]) -> Any:

    return

# 回答を出力する


def answer(ans: Any) -> None:
    print(ans)


if __name__ == "__main__":
    main()
