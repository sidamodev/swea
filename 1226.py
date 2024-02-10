import sys
sys.stdin = open("1226.txt", "r")

def dfs(i, j):
    maze[i][j] = 1
    for di, dj in d_ij:
        if maze[i + di][j + dj] != 1:
            dfs(i + di, j + dj)

for test_case in range(1, 11):
    tc = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    d_ij = ((-1, 0), (1, 0), (0, -1), (0, 1))
    dfs(1, 1)
    print(f'#{tc} {1 if maze[arr[0]][arr[1]] == 1 else 0}')
    # pprint.pprint(maze)
