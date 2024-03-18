import sys

sys.stdin = open('5207.txt', 'r')

T = int(input())


# 가운데 -> 1 / 오른쪽 -> 2 / 왼쪽 -> 3 / 실패 -> 0
def bin_search(l, r, t, d):
    m = (l + r) // 2
    if l > r:
        return -1
    if A[m] == t:
        return m
    elif A[m] > t and d != 1:
        return bin_search(l, m - 1, t, 1)
    elif A[m] < t and d != 2:
        return bin_search(m + 1, r, t, 2)
    else:
        return -1


for t_c in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    A.sort()
    for n in B:
        if bin_search(0, N - 1, n, 0) != -1:
            cnt += 1
    print(f'#{t_c} {cnt}')
