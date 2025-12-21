
import sys
from typing import List, Set, Tuple, Any  # type: ignore

# 高速入力


def input() -> str:
    return sys.stdin.readline().strip()

# 配列入力


def map_int() -> List[int]:
    return list(map(int, input().split()))


# 二次配列
_ = [[0]*10 for _ in range(10)]


def main():
    H, W, N = map(int, input().split())
    A = [set[int]() for _ in range(H)]

    for i in range(H):
        a = map_int()
        for j in a:
            A[i].add(j)
    B = [0]*N
    for i in range(N):
        B[i] = int(input())
    ans = solve(H, W, N, A, B)

    answer(ans)

# 問題を解く


def solve(H: int, W: int, N: int, A: List[Set[int]], B: List[int]) -> int:
    c = [0]*H
    for i in range(N):
        for h in range(H):
            if B[i] in A[h]:
                c[h] += 1
                break
    return max(c)


# 回答を出力する


def answer(ans: Any) -> None:
    print(ans)


if __name__ == "__main__":
    main()
