import sys

sys.stdin = open('5209.txt', 'r')

i = input


def dfs(l, sum_v):
    global min_v
    if sum_v >= min_v:
        return
    if l == N:
        if sum_v < min_v:
            min_v = sum_v
        return sum_v

    for k in range(N):
        if A[k] in v:
            continue



for t_c in range(1, i() + 1):
    N = int(i())
    A, v = [list(map(int, i().split())) for _ in range(N)], []
    min_v = 0xfffff
    dfs()
