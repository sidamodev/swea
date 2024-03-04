import sys

sys.stdin = open('5209.txt', 'r')

T = int(input())


def dfs(i, sum_v):
    global min_cost
    if sum_v >= min_cost:
        return
    if i == N:
        if sum_v < min_cost:
            min_cost = sum_v
        return

    for k in range(N):
        if not chk[k]:
            chk[k] = 1
            dfs(i + 1, sum_v + cost[i][k])
            chk[k] = 0


for t_c in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 0xffff
    chk = [0] * N
    dfs(0, 0)
    print(f'#{t_c} {min_cost}')