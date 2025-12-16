import math
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
    W, B = map(int, input().split())

    ans = solve(W, B)

    answer(ans)


def solve(W: int, B: int) -> Any:
    """問題を解く"""
    w = W*1000
    return math.floor((w) / B)+1


def answer(ans: Any) -> None:
    """回答を出力する"""
    print(ans)


if __name__ == "__main__":
    main()
