import sys
import pprint

sys.stdin = open("2806.txt", "r")


# 1 1
# 2 0
# 3 0
# 4 2
# 5 10
# 6 4
# 7 40
# 8 92
# 9 352
# 10 724

def zero_fill():
    for i in range(N):
        for j in range(N):
            board[i][j] = 0

def solve(x, y):
    global counter
    if counter == N:
        zero_fill()

    i, j = x, y
    counter += 1
    for p in range(N):
        for q in range(N):
            if p == i or q == j or p - i == q - j or p - i == j - q:
                board[p][q] = 1
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                solve(r, c)


    #             print('aaa')
    # print('\n'.join([' '.join([str(cell) for cell in row]) for row in board]))
    # print(counter)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    counter = 0
    result = [0]

    solve(0, 0)
    print(f'#{tc} {result[0]}')
