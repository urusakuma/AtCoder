def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        R = list(map(int, input().split()))
        s = sum(R)

        for i in range(1, N):
            R[i] = min(R[i], R[i-1]+1)
        for i in range(N-2, -1, -1):
            R[i] = min(R[i], R[i+1]+1)
        s -= sum(R)
        print(s)


if __name__ == "__main__":
    main()
