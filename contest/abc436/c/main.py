n, m = (map(int, input().split()))

r, c = [0]*m, [0]*m
for i in range(m):
    r[i], c[i] = map(int, input().split())

puted = [-1]*m
pos = set[tuple[int, int]]()


def can_put(x: int, y: int):
    for i in range(3):
        for j in range(3):
            if (x+i-1, y+j-1) in pos:
                return False
    return True


counter = 0
for i in range(m):
    if can_put(r[i], c[i]):
        pos.add((r[i], c[i]))
        counter += 1

print(counter)
