def main():
    N, M = map(int, input().split())
    drinked = [False for _ in range(M)]
    for i in range(N):
        L = int(input())
        X = list(map(int, input().split()))
        canDrink = False
        for x in X:
            if not drinked[x-1]:
                drinked[x-1] = True
                print(x)
                canDrink = True
                break
        if not canDrink:
            print(0)


if __name__ == "__main__":
    main()
