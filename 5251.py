import sys

sys.stdin = open('5251.txt', 'r')

for t_c in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    A = [[0] * N + 1 for _ in range(N + 1)]
    INF = int(1e9)
    for i in range(E):
        s, e, w = map(int, input().split())

