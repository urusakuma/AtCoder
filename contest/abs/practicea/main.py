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
    A = int(input())
    B, C = map(int, input().split())
    S = input()

    print(A+B+C, S)


if __name__ == "__main__":
    main()
