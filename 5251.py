import sys

sys.stdin = open('5251.txt', 'r')

from heapq import heappush, heappop
INF = int(1e9)

def dijkstra(start):
    pq = [(0, start)]
    while pq:
        w, v = heappop(pq)
        if v == N: return w
        if v in chk: continue
        chk.add(v)
        for i in range(N + 1):
            heappush(pq, (w + A[v][i], i))

for t_c in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    A = [[INF] * (N + 1) for _ in range(N + 1)]
    chk = set()
    for i in range(E):
        s, e, w = map(int, input().split())
        A[s][e] = w
    print(f'#{t_c} {dijkstra(0)}')
