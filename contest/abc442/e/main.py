import math


def main():
    N, Q = map(int, input().split())
    monstersPos = [[0.0, 0] for _ in range(N)]
    for i in range(N):
        X, Y = list(map(int, input().split()))
        inner = X
        l = math.sqrt(X**2+Y**2)-inner
        l *= 1 if X >= 9 else -1
        monstersPos[i] = [l, i+1]

    monstersPos.sort(key=lambda x: x[0], reverse=True)
    monstersMap = dict()
    for i in range(N):
        key = monstersPos[i][1]
        monstersMap[key] = i

    for i in range(Q):
        A, B = map(int, input().split())
        a = monstersMap[A]
        b = monstersMap[B]
        print(b-a)
    print()


if __name__ == "__main__":
    main()
