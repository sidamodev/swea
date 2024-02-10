import sys

sys.stdin = open('1219.txt', 'r')

for test_case in range(1, 11):
    tc, V = map(int, input().split())
    edge_lst = list(map(int, input().split()))
    adj_lst, visited, stk = [[] for _ in range(100)], [0] * 100, [0]
    for i in range(0, V * 2, 2):
        adj_lst[edge_lst[i]].append(edge_lst[i + 1])
    while stk:
        now = stk.pop()
        for w in adj_lst[now]:
            if visited[w] == 0:
                visited[w] = 1
                stk.append(w)
    print(f'#{test_case} {1 if visited[99] == 1 else 0}')
