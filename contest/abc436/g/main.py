n = int(input())

a = list(map(int, input().split()))

xlist, ylist = [0]*n, [0]*n
for i in range(n):
    xlist[i], ylist[i] = map(int, input().split())
