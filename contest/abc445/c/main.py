def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in range(N-1, -1, -1):
        a = A[i]
        A[i] = max(A[i], A[a-1])

    print(*A)


if __name__ == "__main__":
    main()
