import math  # type: ignore
import sys
from typing import List, Set, Tuple, Any  # type: ignore


def input() -> str:
    """高速入力"""
    return sys.stdin.readline().strip()


def map_int() -> List[int]:
    """ 配列入力"""
    return list(map(int, input().split()))


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)

    answer(ans)


def solve(N: int, A: List[int]) -> Any:
    """問題を解く"""
    ans: int = 0
    while True:
        for i in range(N):
            if A[i] % 2 == 1:
                return ans
            A[i] = A[i]//2
        ans += 1


def answer(ans: Any) -> None:
    """回答を出力する"""
    print(ans)


if __name__ == "__main__":
    main()
