def main():
    H, _, N = map(int, input().split())
    A = [0]*91

    for i in range(H):
        for a in map(int, input().split()):
            A[a] = i+1
    c = [0]*(H+1)
    for i in range(N):
        c[A[int(input())]] += 1
    print(max(c[1:]))


if __name__ == "__main__":
    main()
