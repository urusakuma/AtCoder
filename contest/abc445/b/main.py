def main():
    N = int(input())
    S = ["" for _ in range(N)]
    maxLen = 0
    for i in range(N):
        S[i] = input()
        maxLen = max(len(S[i]), maxLen)
    for i in range(N):
        l = (maxLen-len(S[i]))//2
        print("."*l+S[i]+"."*l)


if __name__ == "__main__":
    main()
