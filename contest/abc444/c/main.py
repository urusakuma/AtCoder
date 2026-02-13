def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans: list = []
    if N % 2 == 0 and fn(A):
        ans.append(A[0]+A[N-1])

    i = 0
    while i < N and A[i] == A[0]:
        i += 1
    if (N-i) % 2 == 0 and fn(A[i:]):
        ans.append(A[0])

    ans.sort()
    print(*ans)


def fn(A):
    N = len(A)
    l = -1
    isMatch = True
    for j in range(N//2):
        l2 = A[j]+A[N-j-1]
        if l == -1:
            l = l2
        isMatch = l == l2
        if not isMatch:
            break
    return isMatch


if __name__ == "__main__":
    main()
