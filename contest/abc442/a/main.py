def main():
    S = input()
    ans = 0
    for s in S:
        if s == "i" or s == "j":
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
