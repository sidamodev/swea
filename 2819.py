T = int(input())
d_ij = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(i, j, path):
    if len(path) == 7:
        res.add(path)
        return
    for di, dj in d_ij:
        ni, nj = i + di, j + dj
        if 4 > ni >= 0 <= nj < 4:
            dfs(ni, nj, path + board[ni][nj])


for t_c in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]
    res = set()
    for p in range(4):
        for q in range(4):
            dfs(p, q, '')
    print(f'#{t_c} {len(res)}')
