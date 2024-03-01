import sys

sys.stdin = open('1244.txt', 'r')
T = int(input())

def solve(lev):
    global max_v
    value = int(''.join(board))
    if value not in visited[lev]:
        visited[lev].add(value)
    else:
        return
    if lev == change:
        if value > max_v:
            max_v = value
        return
    for i in range(N - 1):
        for j in range(i + 1, N):
            board[i], board[j] = board[j], board[i]
            solve(lev + 1)
            board[i], board[j] = board[j], board[i]


for t_c in range(1, T + 1):
    board, change = map(int, input().split())
    visited = [set() for _ in range(change + 1)]
    board = list(str(board))
    max_v = 0
    N = len(board)
    solve(0)
    print(f'#{t_c} {max_v}')

# 1 321
# 2 7732
# 3 857147
# 4 87664
# 5 88832
# 6 777770
# 7 966354
# 8 954311
# 9 332211
# 10 987645
