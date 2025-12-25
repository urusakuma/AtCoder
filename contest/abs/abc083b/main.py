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
    N, A, B = map(int, input().split())

    ans = solve(N, A, B)

    answer(ans)


def solve(N: int, A: int, B: int) -> Any:
    """問題を解く"""
    c = [0 for _ in range(N+1)]
    for i in range(N+1):
        n = i
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        if s >= A and s <= B:
            c[i] = i
    return sum(c)


def answer(ans: Any) -> None:
    """回答を出力する"""
    print(ans)


if __name__ == "__main__":
    main()
