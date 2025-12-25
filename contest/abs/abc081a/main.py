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
    a = int(input())
    x1 = a % 10
    x2 = (a//10) % 10
    x3 = a//100

    answer(x1+x2+x3)


def solve(N: int, M: int) -> Any:
    """問題を解く"""
    return


def answer(ans: Any) -> None:
    """回答を出力する"""
    print(ans)


if __name__ == "__main__":
    main()
