n = int(input())
a = list(map(int, input().split()))

f = a[0]
c = 1
for i in range(1, n):
    f -= 1
    if (f == 0):
        break
    if f < a[i]:
        f = a[i]
    c += 1

print(c)
