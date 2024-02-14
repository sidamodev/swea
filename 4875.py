import sys
import pprint

sys.stdin = open('4875.txt', 'r')


def dfs(x, y):
    stk = [[x, y]]
    i, j =  x, y
    visit = [[0] * N for _ in range(N)]
    while stk:
        for di, dj in d_ij:
            if 0 <= i + di < N and 0 <= j + dj < N and maze[i + di][j + dj] != 1 and visit[i + di][j + dj] == 0:
                stk.append([i + di, j + dj])
                visit[i + di][j + dj] = 1
                break
            elif visit[0][end] == 1:
                return 1
        else:
            i, j = stk.pop()
    return 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    d_ij = ((-1, 0), (1, 0), (0, -1), (0, 1))
    end = [p for p in range(N) if maze[0][p] == 3][0]
    start = [(p, q) for q in range(N) for p in range(N) if maze[p][q] == 2][0]
    print(f'#{test_case} {dfs(start[0], start[1])}')
