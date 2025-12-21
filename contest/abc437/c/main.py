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
    for _ in range(T):
        N = int(input())
        wp: List[list[int]] = [[0]*2]*N
        p = 0
        for i in range(N):
            wp[i] = list(map(int, input().split()))
            p += wp[i][1]
        wp.sort(key=lambda x: x[0]+x[1])
        ans = solve(N, wp, p)
        answer(ans)

# 問題を解く


def solve(N: int, wp: List[List[int]], P: int) -> Any:
    ans = 0
    for i in range(N):
        ans += wp[i][0]+wp[i][1]
        if P < ans:
            return i
    return

# 回答を出力する


def answer(ans: Any) -> None:
    print(ans)


if __name__ == "__main__":
    main()
