import math


def main():
    T = int(input())
    for _ in range(T):
        N, W = map(int, input().split())
        C = list(map(int, input().split()))
        l_len = math.ceil(2*W)
        l = [0 for _ in range(l_len)]
        ans = 2*10**9
        for i in range(N):
            j = i % (2*W)
            l[j] += C[i]
        l += l
        s = sum(l[:W])
        ans = s
        for i in range(1, 2*W):
            s += l[i+W-1]
            s -= l[i-1]
            if s < ans:
                ans = s

        print(ans)


if __name__ == "__main__":
    main()
