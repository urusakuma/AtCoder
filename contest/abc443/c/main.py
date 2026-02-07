def main():
    N, T = map(int, input().split())
    if N == 0:
        print(T)
        return
    A = list(map(int, input().split()))
    ans = A[0]
    openT = A[0]+100
    for i in range(1, N):
        if openT > A[i]:
            continue
        t = A[i]-openT
        openT = A[i]+100
        ans += t
    if T > openT:
        ans += T-openT
    print(ans)


if __name__ == "__main__":
    main()
