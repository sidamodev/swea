import sys
import pprint

sys.stdin = open('2806.txt', 'r')


def dfs(i):
    for j in range(N):
        if i < N - 1 and i != j and visit[i] == 0:
            visit[i] = j
            dfs(i + 1)
            visit[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visit = [0] * N
    dfs(0)
    print(f'#{tc} {visit}')
