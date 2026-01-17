def main():
    N, M = map(int, input().split())
    S = str(input())
    T = str(input())
    Q = int(input())
    for _ in range(Q):
        t = str(input())
        takahashi = True
        aoki = True
        for s in t:
            takahashi = s in S and takahashi
            aoki = s in T and aoki
        if takahashi and aoki:
            print("Unknown")
        elif takahashi:
            print("Takahashi")
        else:
            print("Aoki")


if __name__ == "__main__":
    main()
