import sys

sys.stdin = open('5105.txt', 'r')
import pprint
from collections import deque

def search():
    q = deque([start])
    visit = [[0] * N for _ in range(N)]
    d_ij = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visit[start[0]][start[1]] = 1
    while q:
        if visit[end[0]][end[1]]:
            return visit[end[0]][end[1]] - 2
        pos = q.popleft()
        for di, dj in d_ij:
            i, j = (pos[0] + di, pos[1] + dj)
            if N > j >= 0 <= i < N and maze[i][j] != 1:
                if not visit[i][j]:
                    visit[i][j] = visit[pos[0]][pos[1]] + 1
                    q.append((i, j))
    return 0

T = int(input())
for t_c in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start = [(i, j) for j in range(N) for i in range(N) if maze[i][j] == 2][0]
    end = [(i, j) for j in range(N) for i in range(N) if maze[i][j] == 3][0]
    print(f'#{t_c} {search()}')
