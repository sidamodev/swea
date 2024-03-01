T = int(input())
import pprint


def dfs(i, score):

    global max_v
    if i == N:
        if score > max_v:
            max_v = score
    for j in range(N):
        if not visited[j] and board[i][j] >= 0:
            visited[j] = True
            dfs(i + 1, score + board[i][j])


for t_c in range(1, T + 1):
    N = int(input())
    visited = [False] * N
    max_v = 0
    board = [list(map(int, input().split())) for _ in range(N)]
    for p in range(N):
        dfs(p, 0)
    print(max_v)
    print()
