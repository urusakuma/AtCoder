def main():
    A, B, C, X, Y = map(int, input().split())
    # A,Bを素直に買う
    p1 = A * X + B * Y
    # すべてCで買う
    p2 = 2 * C * max(X, Y)
    # 片方をすべてCで買い、残りを素直に買う
    m = min(X, Y)
    p3 = 2 * C * m + A * (X - m) + B * (Y - m)
    print(min(p1, p2, p3))


if __name__ == "__main__":
    main()
