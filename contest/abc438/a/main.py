def main():
    D, F = map(int, input().split())
    ans = (F-D) % 7
    if ans == 0:
        ans = 7
    print(ans)


def test():
    d, f = 10, 1
    for d in range(10, 30):
        for f in range(1, 8):
            ans = (f-d) % 7
            if ans == 0:
                ans = 7
            print("D:", d, "f:", f, "ans:", ans)


if __name__ == "__main__":
    main()
