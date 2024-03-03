import sys

sys.stdin = open('5189.txt', 'r')
T = int(input())


def dfs(i, j, sum_e):
    global min_e
    if sum_e >= min_e:
        return
    if i == N - 1:
        sum_e += e[j][0]
        if sum_e < min_e:
            min_e = sum_e
        return
    for k in range(1, N):
        if not visited[k]:
            visited[k] = 1
            dfs(i + 1, k, sum_e + e[j][k])
            visited[k] = 0


for t_c in range(1, T + 1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_e = 0xffff
    dfs(*([0] * 3))
    print(f'#{t_c} {min_e}')
