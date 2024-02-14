import sys

sys.stdin = open('1222.txt', 'r')

for test_case in range(1, 11):
    N = int(input())
    input_str = input()
    result, stk, opr = [], [], []
    for elem in input_str:
        if elem == '+':
            opr.append(elem)
            result.append(stk.pop())
        else:
            result.append(elem)
    print(result)
