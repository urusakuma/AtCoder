import sys


input = sys.stdin.readline
N, M, L, S, T = map(int, input().split())
cost = dict[tuple[int, int], list[int]]()
root = dict[int, list[int]]()
for i in range(M):
    u, v, c = map(int, input().split())
    if u not in root:
        root[u] = []
    root[u].append(v)
    if (u, v) not in cost:
        cost[(u, v)] = []
    cost[(u, v)].append(c)


def main():
    ans = set()
    fn(0, 1, 0, ans)
    l = list(ans)
    l.sort()
    print(*l)


def fn(l: int, u: int, c: int, ans: set):
    if c > T:
        return
    elif l == L:
        if c >= S:
            ans.add(u)
        return
    if u not in root:
        return
    for v in root[u]:
        for cs in cost[(u, v)]:
            fn(l+1, v, c+cs, ans)


if __name__ == "__main__":
    main()
