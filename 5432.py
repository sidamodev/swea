import sys

sys.stdin = open('5432.txt', 'r')
T = int(input())
for t_c in range(1, T + 1):
    input_lst = list(input())
    stk = ['(']
    l_stk = []
    cnt = laser = 0
    i = 1

    print(cnt)
