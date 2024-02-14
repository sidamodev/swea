import sys

sys.stdin = open('4874.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    input_str = input().split()
    stk_num = []

    for char in input_str:
        if char == '.':
            if len(stk_num) > 1:
                result = 'error'
            else:
                result = stk_num.pop()
            break
        elif char in '*/+-':
            if len(stk_num) <= 1:
                result = 'error'
                break
            result = 0
            n2 = stk_num.pop()
            n1 = stk_num.pop()
            if char == '+':
                result += n1 + n2
            elif char == '-':
                result += n1 - n2
            elif char == '*':
                result += n1 * n2
            elif char == '/':
                result += n1 // n2
            stk_num.append(result)
        else:
            stk_num.append(int(char))
    print(f'#{test_case} {result}')
