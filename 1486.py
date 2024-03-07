import sys

sys.stdin = open('1486.txt', 'r')
T = int(input())


def dfs(i, sum_v):
    global min_v
    if min_v <= B:
        return
    if sum_v >= min_v:
        return
    if sum_v >= B:
        min_v = sum_v
        return


    for k in range(i, N):
        if not v[k]:
            v[k] = 1
            dfs(k + 1, sum_v + S[k])
            v[k] = 0


for t_c in range(1, T + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    v = [0] * N
    min_v = 0xfffff
    dfs(0, 0)
    print(f'#{t_c} {min_v - B}')
