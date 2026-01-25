def main():
    Q = int(input())
    vol = 0
    playing = False
    for i in range(Q):
        A = int(input())
        if A == 1:
            vol += 1
        elif A == 2 and vol >= 1:
            vol -= 1
        elif A == 3:
            playing = not playing
        if vol >= 3 and playing:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
