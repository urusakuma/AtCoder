from collections import deque


def main():
    T = int(input())
    for t in range(T):
        N, D = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        cp = 0
        for i in range(N):
            A[cp] -= B[i]
            while A[cp] < 0:
                cp += 1
                A[cp] += A[cp-1]  # A[cp-1]<0
                A[cp-1] = 0
            cp = max(cp, (i+1)-D)
        cp = max(cp, N-D)
        ans = 0
        for i in range(cp, N):
            ans += A[i]
        print(ans)


if __name__ == "__main__":
    main()
