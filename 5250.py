import sys

sys.stdin = open('5250.txt', 'r')

from collections import deque

d_ij = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    queue = deque([(0, 0, A[0][0])])
    v[0][0] = 1
    while queue:
        i, j, h = queue.popleft()
        for di, dj in d_ij:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                n_h = A[ni][nj]
                if n_h > h:
                    n_cost = v[i][j] + 1 + n_h - h
                else:
                    n_cost = v[i][j] + 1
                if not v[ni][nj] or n_cost < v[ni][nj]:
                    v[ni][nj] = n_cost
                    queue.append((ni, nj, n_h))


for t_c in range(1, int(input()) + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    bfs()
    print(f'#{t_c} {v[N - 1][N - 1]-1}')
