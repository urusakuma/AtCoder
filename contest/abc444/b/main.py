def main():
    N, K = map(int, input().split())
    ans = 0
    for n in range(1, N+1):
        s = n % 10
        for i in range(1, 6):
            s += (n//(10**i)) % 10
        if s == K:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
