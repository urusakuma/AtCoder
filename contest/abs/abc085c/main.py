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
    N, Y = map(int, input().split())

    ans = solve(N, Y)

    answer(ans)


def solve(N: int, Y: int) -> Any:
    """問題を解く"""
    for a in range(N+1):
        if Y < a*10000:
            break
        for b in range(N+1):
            c = N-(a+b)
            if c < 0:
                continue
            y = a*10000+b*5000+c*1000
            if y == Y:
                return [a, b, c]
    return [-1, -1, -1]


def answer(ans: Any) -> None:
    """回答を出力する"""
    print('{} {} {}'.format(*ans))


if __name__ == "__main__":
    main()
