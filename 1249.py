import sys

sys.stdin = open('1249.txt', 'r')

from heapq import heappush, heappop
d_ij = ((1, 0), (-1, 0), (0, -1), (0, 1))

def dijkstra():
    pq = [(0, (0, 0))]
    while pq:
        w, v = heappop(pq)
        if v == (N - 1, N - 1): return w
        if v in chk: continue
        chk.add(v)
        for di, dj in d_ij:
            ni, nj = v[0] + di, v[1] + dj
            if N > ni >= 0 <= nj < N:
                heappush(pq, (w + A[ni][nj], (ni, nj)))

for t_c in range(1, int(input()) + 1):
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    chk = set()
    print(f'#{t_c} {dijkstra()}')
