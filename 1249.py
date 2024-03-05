import sys
import pprint


sys.stdin = open('1249.txt', 'r')
from collections import deque
T = int(input())

def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 0
    while q:
        i, j, = q.popleft()
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if N > ni >= 0 <= nj < N:
                tmp = board[ni][nj] + visited[i][j]
                if tmp < visited[ni][nj]:
                    visited[ni][nj] = tmp
                    q.append((ni, nj))

for t_c in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    d_ij = ((1, 0), (-1, 0), (0, -1), (0, 1))
    visited = [[999] * N for _ in range(N)]
    bfs()
    print(f'#{t_c} {visited[N-1][N-1]}')
