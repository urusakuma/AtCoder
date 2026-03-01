def main():
    S = input()
    ac = 0
    bc = 0
    ans = 0
    for s in S:
        if s == 'A':
            ac += 1
        elif s == 'B':
            if ac > bc:
                bc += 1
        elif s == 'C':
            if ac >= bc > 0:
                ac -= 1
                bc -= 1
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
