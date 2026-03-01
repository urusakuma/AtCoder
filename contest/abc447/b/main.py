from collections import defaultdict


def main():
    S = input()
    d: dict[str, int] = defaultdict(int)
    m = 0
    for s in S:
        d[s] += 1
        m = max(m, d[s])
    ans = S
    for i in d:
        if d[i] == m:
            ans = ans.replace(i, "")
    print(ans)


if __name__ == "__main__":
    main()
