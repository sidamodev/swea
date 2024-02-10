import sys

sys.stdin = open('4871.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj_lst, visited, stk = [[] for _ in range(V + 1)], [0] * (V + 1), []
    for i in range(E):
        n1, n2 = map(int, input().split())
        adj_lst[n1].append(n2)
    S, G = map(int, input().split())
    stk.append(S)
    while stk:
        now = stk.pop()
        for w in adj_lst[now]:
            if visited[w] == 0:
                visited[w] = 1
                stk.append(w)
    print(f'#{test_case} {1 if visited[G] == 1 else 0}')
