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
    B = int(input())
    C = int(input())
    X = int(input())

    ans = solve(A, B, C, X)

    answer(ans)


def solve(A: int, B: int, C: int, X: int) -> Any:
    """問題を解く"""
    ans = 0

    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if a*500+b*100+c*50 == X:
                    ans += 1
    return ans


def answer(ans: Any) -> None:
    """回答を出力する"""
    print(ans)


if __name__ == "__main__":
    main()
