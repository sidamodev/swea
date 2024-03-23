import sys

sys.stdin = open('1238.txt', 'r')

from collections import deque


def bfs():
    max_d = longest_node = 0
    q = deque([(S, 0)])
    visit = [0] * 101
    visit[S] = 1
    while q:
        v, d = q.popleft()
        if d > max_d or (d == max_d and v > longest_node):
            max_d = d
            longest_node = v
        for node in graph[v]:
            if not visit[node]:
                visit[node] = 1
                q.append((node, d + 1))
    return longest_node


for t_c in range(1, 11):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        graph[lst[i]].append(lst[i + 1])
    print(f'#{t_c} {bfs()}')
