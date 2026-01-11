def main():
    N = int(input())
    T = list(zip((map(int, input().split())), range(1, N+1)))
    T.sort()

    print(T[0][1], T[1][1], T[2][1])


if __name__ == "__main__":
    main()
