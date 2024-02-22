import sys

sys.stdin = open('5177.txt', 'r')


def heap_push(n, input_num):
    tree[n] = input_num
    while n // 2 > 0 and tree[n // 2] > tree[n]:
        tree[n // 2], tree[n] = tree[n], tree[n // 2]
        n //= 2

T = int(input())
for t_c in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    tree = [0] * (N + 1)
    heap_cnt = 0
    for elem in data:
        heap_cnt += 1
        heap_push(heap_cnt, elem)
    print(heap_cnt)
    res = 0
    while heap_cnt >= 1:
        heap_cnt //= 2
        res += tree[heap_cnt]
    print(tree)
    print(f'#{t_c} {res}')
