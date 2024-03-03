import sys
import pprint

sys.stdin = open('4615.txt', 'r')

T = int(input())
for t_c in range(1, T + 1):
    N, M = map(int, input().split())
    record = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]
    mid = N // 2
    init_v = [2, 1, 1, 2]
    di = (-1, 0, 1, 0, 1, 1, -1, -1)
    dj = (0, -1, 0, 1, 1, -1, 1, -1)
    for i in range(mid - 1, mid + 1):
        for j in range(mid - 1, mid + 1):
            board[i][j] = init_v[(i - mid - 1) * 2 + j - (mid - 1)]
    for x, y, s in record:
        i, j = y - 1, x - 1
        # 상대 돌 확인 후 놓기
        for k in range(8):
            d = 0
            for p in range(1, N):
                ni, nj = i + di[k] * p, j + dj[k] * p
                if not (0 <= ni < N and 0 <= nj < N): break
                if board[ni][nj] == 0:
                    break
                elif board[ni][nj] == s:
                    d = p
                    break
            if d > 1:
                board[i][j] = s
                for p in range(1, d + 1):
                    nx, ny = i + di[k] * p, j + dj[k] * p
                    board[nx][ny] = s
    blk = wht = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                blk += 1
            elif board[i][j] == 2:
                wht += 1
    print(f'#{t_c} {blk} {wht}')
