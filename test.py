def dfs(lev, j):
    if lev == 4:
        print(path)
        return
    for k in range(j, 4):
        path.append(k)
        dfs(lev + 1, k)
        path.pop()


path = []
dfs(0, 1)
