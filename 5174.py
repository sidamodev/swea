import sys

sys.stdin = open('5174.txt', 'r')

T = int(input())
def search_subtree(n):
    global cnt
    if not n:
        return
    else:
        cnt += 1
    search_subtree(tree[n][0])
    search_subtree(tree[n][1])
    return cnt

for t_c in range(1, T + 1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(E + 2)]
    for i in range(0, E * 2, 2):
        if not tree[data[i]][0]:
            tree[data[i]][0] = data[i + 1]
        else:
            tree[data[i]][1] = data[i + 1]
    cnt = 0
    print(f'#{t_c} {search_subtree(N)}')
