import math


def main():
    N, M = map(int, input().split())
    relationship = dict[int, set[int]]()

    for _ in range(M):
        A, B = map(int, input().split())
        if A not in relationship:
            relationship[A] = set()
        if B not in relationship:
            relationship[B] = set()
        relationship[A].add(B)
        relationship[B].add(A)
    ans = [0 for _ in range(N)]
    for i in range(1, N+1):
        if i not in relationship:
            n = N - 1
        else:
            n = N - len(relationship[i])-1
        s = math.comb(n, 3)
        ans[i-1] = s
    print(*ans)


if __name__ == "__main__":
    main()
