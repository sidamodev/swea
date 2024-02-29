import sys
import pprint

sys.stdin = open('11315.txt', 'r')


def solve(i, j):
    cnt = 1
    for di, dj in d_ij:
        for k in range(1, 5):
            ni, nj = i + di * k, j + dj * k
            if not (0 <= ni < N and 0 <= nj < N): break
            if b[ni][nj] == 'o':
                cnt += 1
            if cnt == 5:
                return True
    return False


T = int(input())
for t_c in range(1, T + 1):
    N = int(input())
    b = [list(input()) for _ in range(N)]
    pprint.pprint(b)
    d_ij = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1))  # 상하좌우 좌상 좌하 우상 우하
    result = 0
    for r in range(N):
        for c in range(N):
            if b[r][c] == 'o':
                result = solve(r, c)
    print(result)
