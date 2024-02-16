import sys

sys.stdin = open('5102.txt', 'r')

from collections import deque
def search():
    q = deque()
    visit = [0] * (V + 1)
    q.append(S)
    visit[S] = 1
    while q:
        now = q.popleft()
        for node in node_lst[now]:
            if not visit[node]:
                visit[node] = visit[now] + 1
                q.append(node)
    if visit[G]:
        return visit[G] - 1
    else:
        return 0

T = int(input())
for t_c in range(1, T + 1):
    V, E = map(int, input().split())
    node_lst = [[] for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        node_lst[n1].append(n2)
        node_lst[n2].append(n1)
    S, G = map(int, input().split())
    print(f'#{t_c} {search()}')
