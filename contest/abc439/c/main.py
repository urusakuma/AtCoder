def main():
    N = int(input())
    memo = [0 for _ in range(N+1)]
    fn(N, memo)
    l = []
    i = 0
    for c in memo:
        if c == 1:
            l.append(i)
        i += 1
    k = len(l)
    print(k)
    if k == 0:
        print()
    else:
        print(*l)


def fn(n, memo: list):
    for x in range(1, int(n**0.5)+1):
        for y in range(x+1, int(n**0.5)+1):
            z = x**2+y**2
            if z <= n:
                memo[z] += 1
            else:
                break


def fn1(n, memo: dict):
    c = 0
    for x in range(1, int(n**0.5)+1):
        y = int((n-x**2)**0.5)
        z = x**2+y**2
        if z == n and x < y:
            c += 1
            if c > 1:
                return False
    return c == 1


def fn2(n, memo: dict):
    c = 0
    if memo.get(n) is not None and memo.get(n) != (0, 0):
        del memo[n]
        return True
    elif memo.get(n) == (0, 0):
        del memo[n]
        return False
    for i in range(max(int(n**0.5)-1, 1), n):
        if i**2 > n:
            break
        if 2*i**2 < n:
            continue
        for j in range(i-1, 0, -1):
            z = i**2+j**2
            print(i, j, z, n)
            if memo.get(z) is None:
                memo[z] = (i, j)
            elif memo.get(z) != (i, j):
                memo[z] = (0, 0)
            if z < n:
                break
            if z != n:
                continue
            c += 1
            if c > 1:
                return False
    return c == 1


if __name__ == "__main__":
    main()
