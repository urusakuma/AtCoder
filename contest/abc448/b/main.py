def main():
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    S = [0]*M
    for _ in range(N):
        A, B = map(int, input().split())
        S[A-1] += B

    ans = 0
    for i in range(M):
        ans += min(C[i], S[i])
    print(ans)


if __name__ == "__main__":
    main()
