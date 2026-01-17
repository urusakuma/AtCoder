N, M, L, S, T = map(int, input().split())
graph: list[list[tuple[int, int]]] = [[]for _ in range(N+1)]
for i in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))


def main():
    ok = [False for _ in range(N+1)]
    fn(0, 1, 0, ok)
    ans = [i for i in range(N+1) if ok[i]]
    print(*ans)


def fn(l: int, u: int, c: int, ans: list):
    if c > T:
        return
    elif l == L:
        if c >= S:
            ans[u] = True
        return
    for v in graph[u]:
        fn(l+1, v[0], c+v[1], ans)


if __name__ == "__main__":
    main()
