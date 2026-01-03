def main():
    N = int(input())
    a = N
    s = set()
    while a not in s:
        s.add(a)
        b = 0
        while a > 0:
            b += (a % 10)**2
            a //= 10
        a = b
    if a == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
