import sys

sys.stdin = open('1251.txt', 'r')


T = int(input())

def find(c):
    if c != p[c]:
        c = find(p[c])
    return p[c]


def union(a, b):
    pa = find(a)
    pb = find(b)
    p[pb] = pa


for t_c in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    MST = sorted([[((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) ** 0.5, i, j] for i in range(N) for j in range(i + 1, N)])
    p = [i for i in range(N)]
    sum_dst = 0
    for dst, start, end in MST:
        if find(start) != find(end):
            union(start, end)
            sum_dst += dst ** 2
    print(f'#{t_c} {int(round(E * sum_dst, 0))}')
