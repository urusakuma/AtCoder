def main():
    N, K = map(int, input().split())
    ans = 0
    n = N
    s = n
    while s < K:
        n += 1
        s += n
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
