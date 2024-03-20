def find(c):
    if c != p[c]:
        return c
    else:
        p[c] = find(p[c])
        return p[c]


def union(x, y):
    x, y = find(x), find(y)
    p[y] = x


for t_c in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    p = [i for i in range(N)]
    for elem in:
