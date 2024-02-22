import sys

sys.stdin = open('5178.txt', 'r')
T = int(input())

for t_c in range(1, T + 1):
    N, M, L = map(int, input().split())
    leaf = [list(map(int, input().split())) for _ in range(M)]
    tree = [0] * (N + 1)
    for elem in leaf:
        tree[elem[0]] = elem[1]
    heap_cnt = N
    while heap_cnt // 2 > 0:
        tree[heap_cnt // 2] += tree[heap_cnt]
        heap_cnt -= 1
    print(f'#{t_c} {tree[L]}')
