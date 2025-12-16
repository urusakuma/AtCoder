import math  # type: ignore
import sys
from typing import List, Tuple, Any  # type: ignore


def input() -> str:
    """高速入力"""
    return sys.stdin.readline().strip()


def map_int() -> List[int]:
    """ 配列入力"""
    return list(map(int, input().split()))


"""二次配列"""
_ = [[0]*10 for _ in range(10)]


def main():
    N, M = map(int, input().split())

    ans = solve(N, M)

    answer(ans)


def solve(N: int, M: int) -> Any:
    """問題を解く"""
    return


def answer(ans: Any) -> None:
    """回答を出力する"""
    print(ans)


if __name__ == "__main__":
    main()
