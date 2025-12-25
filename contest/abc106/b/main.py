
def main():
    N = int(input())
    ans = 0
    for i in range(N+1):
        c = 0
        for j in range(1, (i//2)+1, 2):
            if i % j == 0:
                c += 1
        c += 1
        if c == 8:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
