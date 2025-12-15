n = int(input())
a = list(map(int, input().split()))
r = 0


def fn_sum(i: int, j: int):
    r = 0
    for k in range(i, j+1):
        r += a[k]
    return r


def judge(i: int, j: int):
    m = fn_sum(i, j)
    for k in range(i, j+1):
        if m % a[k] == 0:
            return 0
    return 1


for i in range(n-1):
    for j in range(i+1, n):
        r += judge(i, j)
print(r)
