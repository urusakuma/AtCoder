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
    A = map_int()
    ans = solve(N, A)

    answer(ans)


def solve(N: int, A: List[int]) -> Any:
    """問題を解く"""
    A.sort()
    alice = 0
    bob = 0
    for i in range(N):
        if i % 2 == 0:
            alice += A.pop()
        else:
            bob += A.pop()
    return alice - bob


def answer(ans: Any) -> None:
    """回答を出力する"""
    print(ans)


if __name__ == "__main__":
    main()
