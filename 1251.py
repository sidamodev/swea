import sys

sys.stdin = open('1251.txt', 'r')

T = int(input())


def find(c):
    if p[c] < 0:
        return c
    else:
        p[c] = find(p[c])
    return p[c]


def union(a, b):
    pa = find(a)
    pb = find(b)
    if (pa == pb):
        return
    if p[pa] < p[pb]:
        p[pa] += p[pb]
        p[pb] = pa
    else:
        p[pb] += p[pa]
        p[pa] = pb


for t_c in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    MST = [[((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2), i, j] for i in range(N - 1) for j in range(i + 1, N)]
    MST.sort(key=lambda x: x[0])
    p = [-1 for i in range(N)]
    sum_dst = 0
    for dst, start, end in MST:
        if find(start) != find(end):
            union(start, end)
            sum_dst += dst
    print(f'#{t_c} {round(E * sum_dst)}')
