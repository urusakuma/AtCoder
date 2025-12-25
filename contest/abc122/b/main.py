def main():
    S = input()
    l = 0
    c = 0
    for s in S:
        if not (s == "A" or s == "C" or s == "G" or s == "T"):
            l = max(l, c)
            c = 0
        else:
            c += 1
    l = max(l, c)
    print(l)


if __name__ == "__main__":
    main()
