import sys

sys.stdin = open('5432.txt', 'r')
T = int(input())
for t_c in range(1, T + 1):
    input_lst = list(input())
    result = pipe = 0
    for i in range(1, len(input_lst)):
        if input_lst[i] == '(':
            if input_lst[i - 1] == '(':
                pipe += 1
        else:
            if input_lst[i - 1] == '(':
                result += pipe
            else:
                result += 1
                pipe -= 1
    print(result)
