def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    cum = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        cum[i] = cum[i-1]+A[i-1]
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            swap = cum[q[1]+1]-cum[q[1]]
            cum[q[1]] = swap+cum[q[1]-1]
        if q[0] == 2:
            print(cum[q[2]]-cum[q[1]-1])


if __name__ == "__main__":
    main()
