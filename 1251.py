import sys

sys.stdin = open('1251.txt', 'r')

from heapq import heappush, heappop

def prim():
    pq = [(0, 0)]
    mst = set()
    sum_dist = 0

    while len(mst) < N:
        w, v = heappop(pq)
        if v in mst: continue
        mst.add(v)
        sum_dist += w
        for i in range(N):
            if adj[v][i] and i not in mst:
                heappush(pq, (adj[v][i], i))
    return round(E * sum_dist)


for t_c in range(1, int(input()) + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    adj = [[0] * N for _ in range(N)]
    for s in range(N - 1):
        for e in range(s + 1, N):
            w = (X[s] - X[e]) ** 2 + (Y[s] - Y[e]) ** 2
            adj[s][e] = w
            adj[e][s] = w
    print(f'#{t_c} {prim()}')