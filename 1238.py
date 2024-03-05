import sys

sys.stdin = open('1238.txt', 'r')

from collections import deque
# 그래프 -> bfs탐색
def bfs():
    q = deque([S])
    visit = [0] * 101
    visit[S] = 1
    while q:
        i = q.popleft()
        for node in graph[i]:
            if not visit[node]:
                visit[node] = visit[i] + 1
                q.append(node)
    max_k = 0
    for k in range(101):
        if visit[k] >= visit[max_k]:
            max_k = k
    return max_k


for t_c in range(1, 11):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        graph[lst[i]].append(lst[i + 1])
    print(f'#{t_c} {bfs()}')
