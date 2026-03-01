def main():
    N, M = map(int, input().split())
    if N+1 >= M*2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
