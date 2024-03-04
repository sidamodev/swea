import sys
from collections import deque

sys.stdin = open('1249.txt', 'r')

T = int(input())


def bfs():
    global min_v
    q = deque([(0, 0, 0)])
    result = 0
    while q:
        i, j, val = q.popleft()
        if val < min_v:
            result += val
        if (i, j) == (N-1, N-1):
            return result
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if N > ni >= 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj, board[ni][nj]))
                if board[ni][nj] < min_v:
                    min_v = board[ni][nj]


for t_c in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    d_ij = ((1, 0), (-1, 0), (0, -1), (0, 1))
    visited = [[0]*N for _ in range(N)]
    min_v = 0xffff
    print(f'#{t_c} {bfs()}')
