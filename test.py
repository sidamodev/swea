# MST using prim & priority queue
from heapq import heappush, heappop

"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""


def prim(start):
    mst = {start}
    weight_heap = []  # 확정되지 않은 가중치
    weight = [0] * V  # 확정된 가중치
    for i in range(V):
        if adj[start][i]:
            # (가중치, 노드 번호)
            heappush(weight_heap, (adj[start][i], i))
            print(weight_heap)

    # 모든 노드를 고를 때까지 반복
    while len(mst) < V:
        # 가중치가 가장 작은 노드(루트노드) 추출
        w, v = heappop(weight_heap)
        if v in mst and weight[v]: continue
        mst.add(v)
        weight[v] = w
        for i in range(V):
            if adj[v][i] and i not in mst or weight:
                heappush(weight_heap, (adj[v][i], i))
                print(weight_heap)

    print(mst, sum(weight))


V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s][e] = w
    adj[e][s] = w
prim(0)
