
def main():
    H, W = map(int, input().split())
    S = ["."*(W+2) for _ in range(H+2)]
    for i in range(H):
        S[i+1] = "."+input()+"."

    ans = ["" for _ in range(H)]
    for i in range(1, H+1):
        for j in range(1, W+1):
            if S[i][j] != ".":
                continue
            bom = 0
            for k in range(3):
                for l in range(3):
                    bom += fn(S[i+k-1][j+l-1])
            S[i] = S[i][:j]+str(bom)+S[i][j+1:]
        ans[i-1] = S[i][1:-1]
    for a in ans:
        print(a)


def fn(c: str):
    if c == "#":
        return 1
    return 0


if __name__ == "__main__":
    main()
