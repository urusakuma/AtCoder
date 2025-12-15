n = int(input())

l = [[0]*n for _ in range(n)]
x = 0
y = int((n-1)/2)
for i in range(n**2):
    if l[x][y] == 0:
        l[x][y] = i+1
    r = (x-1) % n
    c = (y+1) % n
    if l[r][c] == 0:
        x = r
        y = c
    else:
        x = (x+1) % n
        y = y
for i in range(len(l)):
    s = " ".join(map(str, l[i]))
    print(s)
