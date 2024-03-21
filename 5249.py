import sys


sys.stdin = open('5249.txt', 'r')


def find(c):
    if c != p[c]:
        p[c] = find(p[c])
        return p[c]
    else:
        return c


def union(a, b):
    a, b = find(a), find(b)
    if a == b: return
    if a < b:
        p[b] = a
        return True
    elif a > b:
        p[a] = b
        return True


for t_c in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    g = sorted([list(map(int, input().split())) for _ in range(E)], key=lambda x: x[2])
    p = [i for i in range(V + 1)]
    res = 0
    for s, e, w in g:
        if union(s, e):
            res += w
    print(p)
    print(f'#{t_c} {res}')