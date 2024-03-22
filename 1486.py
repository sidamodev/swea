import sys

sys.stdin = open('1486.txt', 'r')
T = int(input())


def dfs(i, h):
    global min_v
    if min_v <= B: return
    if h >= min_v: return
    if h >= B:
        min_v = h
        return
    if i == N: return
    dfs(i + 1, h)
    dfs(i + 1, h + arr[i])


for t_c in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_v = int(1e9)
    dfs(0, 0)
    print(f'#{t_c} {min_v - B}')
