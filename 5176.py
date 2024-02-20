import sys

sys.stdin = open('5176.txt', 'r')

def in_trav(v, num):
    global i
    if v <= N:
        l = in_trav(v * 2, num * 2)
        i += 1
        tree[v][0] = l
        tree[v][2] = i
        if l:
            tree[v][1] = in_trav(v * 2 + 1, l + 1)
        return num

T = int(input())
for t_c in range(1, T + 1):
    N = int(input())
    tree = [[0] * 3 for _ in range(N + 1)]
    i = 0
    in_trav(1, 1)
    print(f'#{t_c} {tree[1][2]} {tree[N // 2][2]}')
    print(tree)