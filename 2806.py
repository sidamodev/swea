import sys
import pprint

sys.stdin = open('2806.txt', 'r')


def dfs(i, j):
    pass

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = [0]
    dfs()
    print(f'#{tc} {result[0]}')
