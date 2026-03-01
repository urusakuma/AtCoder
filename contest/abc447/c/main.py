def main():
    S = input()
    T = input()
    sLen = len(S)
    tLen = len(T)
    sc = 0
    ans = 0
    for i in range(tLen):
        if sLen > sc and T[i] == S[sc]:
            sc += 1
            continue
        if T[i] == 'A':
            ans += 1
            continue
        while sLen > sc and S[sc] == 'A' and T[i] != S[sc]:
            ans += 1
            sc += 1
        if sLen <= sc:
            print(-1)
            return
        if T[i] == S[sc]:
            sc += 1
            continue
        print(-1)
        return
    for i in range(sc, sLen):
        if S[i] == 'A':
            ans += 1
            continue
        print(-1)
        return

    print(ans)


if __name__ == "__main__":
    main()
