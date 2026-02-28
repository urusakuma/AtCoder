from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i in range(N):
        d[A[i]] = max(d[A[i]], d[A[i] - 1] + 1)
    print(max(d.values()))


if __name__ == "__main__":
    main()
