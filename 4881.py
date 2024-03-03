import sys

sys.stdin = open('4881.txt', 'r')

T = int(input())


def dfs(lev, sum_v):
    global min_v
    if lev == N:
        min_v = sum_v
        return
    for k in range(N):
        if not v[k] and sum_v + arr[lev][k] < min_v:
            v[k] = 1
            dfs(lev + 1, sum_v + arr[lev][k])
            v[k] = 0


for t_c in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    min_v = 0xffff
    dfs(0, 0)
    print(f'#{t_c} {min_v}')
