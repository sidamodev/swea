import sys
import pprint

sys.stdin = open('1227.txt', 'r')
from collections import deque
def bfs():
    d_ij = ((-1, 0), (1, 0), (0, -1), (0, 1))
    que = deque([(1, 1)])
    while que:
        i, j = que.popleft()
        for di, dj in d_ij:
            x, y = i + di, j + dj
            if maze[x][y] == '0':
                maze[x][y] = '1'
                que.append((x, y))
            elif maze[x][y] == '3':
                return '1'
    return '0'

for _ in range(1, 11):
    t_c = int(input())
    N = 100
    maze = [list(input()) for _ in range(N)]
    esc = [(i, j) for j in range(N) for i in range(N) if maze[i][j] == '3'][0]
    print(f'#{t_c} {bfs()}')
