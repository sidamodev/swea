import sys
import pprint

sys.stdin = open("2806.txt", "r")
#1 1
#2 0
#3 0
#4 2
#5 10
#6 4
#7 40
#8 92
#9 352
#10 724

def solve():
    for x in range(N):
        for y in range(N):
            board = [[0] * N for _ in range(N)]
            stk = [(x, y)]
            counter = 0
            while stk:
                i, j = stk.pop()
                if board[i][j] == 1:
                    break
                counter += 1
                for p in range(N):
                    for q in range(N):
                        if p == i or q == j or p - i == q - j or p - i == j - q:
                            board[p][q] = 1
                for p in range(N):
                    for q in range(N):
                        if board[p][q] == 0:
                            stk.append((p, q))
            if counter == N:
                result[0] += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = [0]
    solve()
    print(f'#{tc} {result[0]}')
