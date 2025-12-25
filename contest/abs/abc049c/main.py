

def main():
    s: str = input()
    text = ["dream", "dreamer", "erase", "eraser"]
    while len(s) != 0:
        s7 = s[-7:]
        if s7 == text[1]:
            s = s[:-7]
            continue
        s6 = s[-6:]
        if s6 == text[3]:
            s = s[:-6]
            continue
        s5 = s[-5:]
        if s5 == text[0] or s5 == text[2]:
            s = s[:-5]
            continue
        print("NO")
        return
    print("YES")


if __name__ == "__main__":
    main()
