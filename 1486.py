import sys

sys.stdin = open('1486.txt', 'r')
T = int(input())


def dfs(i, j):
    global min_v
    tmp_sum = sum(path)
    if tmp_sum >= min_v:
        return
    if tmp_sum >= B:
        if tmp_sum < min_v:
            min_v = tmp_sum
        return
    if i == N:
        return
    for k in range(j, N):
        path.append(S[k])
        dfs(i + 1, k + 1)
        path.pop()


for t_c in range(1, T + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    min_v = 0xfffff
    path = []
    dfs(0, 0)
    print(f'#{t_c} {min_v-B}')
