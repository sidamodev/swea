d_ij = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(i, j, path):
    if len(path) == 7:
        result.add(path)
        return
    for di, dj in d_ij:
        ni, nj = i + di, j + dj
        if 4 > ni >= 0 <= nj < 4:
            if (i, j, path) not in chk:
                chk.add((i, j, path))
                dfs(ni, nj, path + A[ni][nj])


for t_c in range(1, int(input()) + 1):
    A = [input().split() for _ in range(4)]
    result = set()
    chk = set()
    for p in range(4):
        for q in range(4):
            dfs(p, q, A[p][q])
    print(f'#{t_c} {len(result)}')

