def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    if len(A) < K or len(A) < N-K:
        print(-1)
        return
    A.sort(reverse=True)
    A = A[N-K:]
    drink = 0
    ans = N-K
    for a in A:
        ans += 1
        drink += a
        if drink >= X:
            print(ans)
            return
    print(-1)


if __name__ == "__main__":
    main()
