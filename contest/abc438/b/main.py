def main():
    N, M = map(int, input().split())
    S = input()
    T = input()
    ans = 99999
    for i in range(N-M+1):
        # i番目を入れ替える
        s = S[i:i+M]
        c = 0
        for j in range(M):
            sn = int(s[j])
            tn = int(T[j])
            if sn == tn:
                continue
            if tn > sn:
                sn += 10
            c += sn-tn
        ans = min(ans, c)

    print(ans)


if __name__ == "__main__":
    main()
