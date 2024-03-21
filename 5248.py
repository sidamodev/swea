def find(c):
    if c == p[c]: return c
    p[c] = find(p[c])
    return p[c]


def union(x, y):
    x, y = find(x), find(y)
    if x == y: return
    p[y] = x


for t_c in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    p = [i for i in range(N + 1)]
    arr = [sorted(A[i * 2:i * 2 + 2]) for i in range(M)]
    for a, b in arr: union(a, b)
    print(p)
    print(f'#{t_c} {len(set(find(elem) for elem in p)) - 1}')
