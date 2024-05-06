import pprint

T = int(input())
d_ij = ((-1, 0), (0, 1), (1, 0), (0, -1))

for t_c in range(1, T + 1):
    board = [[0] * 10 for _ in range(10)]
    M, A = map(int, input().split())
    a_move = list(map(int, input().split()))
    b_move = list(map(int, input().split()))
    bc = []
    for _ in range(A):
        bc.append(list(map(int, input().split())))
    
