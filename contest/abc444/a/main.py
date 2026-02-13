def main():
    N = int(input())
    i = 1
    ans = True
    v = N//(100)
    n = N//10 % 10
    ans = v == n and ans
    n = N % 10
    ans = v == n and ans
    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
