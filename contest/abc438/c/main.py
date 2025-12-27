
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B: list[int] = []
    for k in range(N):
        B.append(A[k])
        if len(B) >= 4 and B[-1] == B[-2] == B[-3] == B[-4]:
            for _ in range(4):
                B.pop()
    print(len(B))


if __name__ == "__main__":
    main()
