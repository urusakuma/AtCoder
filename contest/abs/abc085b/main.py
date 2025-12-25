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
    D = set[int]()
    for _ in range(N):
        D.add(int(input()))
    solve(N, D)
    answer(len(D))


def solve(N: int, D: Set[int]) -> Any:
    """問題を解く"""
    return len(D)


def answer(ans: Any) -> None:
    """回答を出力する"""
    print(ans)


if __name__ == "__main__":
    main()
