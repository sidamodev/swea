import sys

sys.stdin = open('5250.txt', 'r')

from heapq import heappush, heappop

d_ij = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dijkstra():
    dist = []
    visited = [[0]*N for _ in range(N)]

    heappush(dist, (0, (0, 0)))  # (w, (i, j))

    while True:
        w, v = heappop(dist)
        if visited[v[0]][v[1]]: continue

        visited[v[0]][v[1]] = 1

        if v == (N - 1, N - 1): return w
        for di, dj in d_ij:
            ni, nj = v[0] + di, v[1] + dj
            if 0 <= ni < N and 0 <= nj < N:
                diff = A[ni][nj] - A[v[0]][v[1]]
                cost = w + 1 + diff if diff > 0 else w + 1
                heappush(dist, (cost, (ni, nj)))


for t_c in range(1, int(input()) + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t_c} {dijkstra()}')
# 데이크서터라