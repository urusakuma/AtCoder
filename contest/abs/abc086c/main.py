def main():
    N = int(input())
    pos_x, pos_y = 0, 0
    pre_t = 0
    for _ in range(N):
        t, x, y = map(int, input().split())
        dt = t-pre_t
        move = abs(pos_x - x) + abs(pos_y - y)

        if move > dt:
            # 最大移動距離を超える
            print("No")
            return

        if move % 2 != dt % 2:
            # 偶奇性により到着できない
            print("No")
            return
        # 移動できるのでposを更新
        pre_t = t
        pos_x = x
        pos_y = y

    print("Yes")


if __name__ == "__main__":
    main()
