from collections import defaultdict


def main():
    N, M = map(int, input().split())
    node = [[] for _ in range(M)]
    d = defaultdict(list)
    oneRoot = set()
    for i in range(M):
        node[i] = list(map(int, input().split()))
        d[node[i][0]].append(node[i][1])
        if len(d[node[i][0]]) == 1:
            oneRoot.add(node[i][0])
        elif len(d[node[i][1]]) == 1:
            oneRoot.add(node[i][1])
        elif node[i][0] in oneRoot:
            oneRoot.remove(node[i][0])
        elif node[i][1] in oneRoot:
            oneRoot.remove(node[i][1])
    delNode = []
    for i in range(M):
        u = node[i][0]
        v = node[i][1]
        ul = len(d[u])
        vl = len(d[v])
        if len(oneRoot) < 2:
            d[u].remove(v)
            delNode.append(i)
            if ul == 2:
                oneRoot.add(d[u])
            if vl == 2:
                oneRoot.add(d[v])
            continue
        if ul > 1 and vl > 1:
            d[u].remove(v)
            delNode.append(i)
            if ul == 2:
                oneRoot.add(d[u])
            if vl == 2:
                oneRoot.add(d[v])
            continue
    ans = 0
    for d in delNode:
        ans += 2**d % 998244353
    print(ans)


if __name__ == "__main__":
    main()
