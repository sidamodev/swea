import sys

sys.stdin = open('4881.txt', 'r')


def solve(i, k):
    if i == k:
        pass
    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i]
            solve(i + 1, k)
            P[i], P[j] = P[j], P[i]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    solve(0, )
