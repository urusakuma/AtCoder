def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    balls = [(A[i], i+1)for i in range(N)]
    balls.sort()
    topBalls = balls[:6]

    for _ in range(Q):
        K = int(input())
        B = set(map(int, input().split()))
        for a, i in topBalls:
            if i not in B:
                print(a)
                break


if __name__ == "__main__":
    main()
