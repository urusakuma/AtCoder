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
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    ans = solve(N, M, A, B)
    answer(ans)


def solve(N: int, M: int, A: List[int], B: List[int]) -> Any:
    """問題を解く"""
    k = [[0] for _ in range(M)]
    for i in range(N):
        k[A[i]-1].append(B[i])

    ans = [0.0]*M
    for i in range(M):
        sum = 0
        for j in range(len(k[i])):
            sum += k[i][j]
        ans[i] = sum/(len(k[i])-1)
    return ans


def answer(ans: List[int]) -> None:
    """回答を出力する"""
    for i in range(len(ans)):
        print(ans[i])


if __name__ == "__main__":
    main()
