T = int(input())

d_ij = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(lev, i, j):
    if lev == 7:
        res.add(''.join(map(str, path)))
        return
    for di, dj in d_ij:
        ni, nj = i + di, j + dj
        if 4 > ni >= 0 <= nj < 4:
            path.append(board[ni][nj])
            dfs(lev + 1, ni, nj)
            path.pop()


for t_c in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    path = []
    res = set()
    for p in range(4):
        for q in range(4):
            dfs(0, p, q)
    print(f'#{t_c} {len(res)}')
