import sys

sys.stdin = open('1865.txt', 'r')

T = int(input())


def dfs(i, prob):
    global max_v
    if prob <= max_v:
        return
    if i == N:
        if prob > max_v:
            max_v = prob
        return
    for k in range(N):
        if chk[k]:
            continue
        chk[k] = task[i][k]
        dfs(i + 1, prob * task[i][k] * 0.01)
        chk[k] = 0


for t_c in range(1, T + 1):
    N = int(input())
    task = [list(map(int, input().split())) for _ in range(N)]
    chk = [0] * N
    max_v = 0
    dfs(0, 1)
    print(f'#{t_c} {format(max_v * 100, ".6f")}')
