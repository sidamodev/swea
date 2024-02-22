import sys
import pprint

sys.stdin = open('1240.txt', 'r')
T = int(input())
for t_c in range(1, T + 1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    code_book = [
        '0001101',
        '0011001',
        '0010011',
        '0111101',
        '0100011',
        '0110001',
        '0101111',
        '0111011',
        '0110111',
        '0001011'
    ]
    i = j = 0
    for i in range(N):
        if '1' in code[i]:
            break
    for j in range(M - 1, -1, -1):
        if code[i][j] == '1':
            j -= 55
            break
    number = []
    for k in range(j, j + 55, 7):
        number.append(code_book.index(code[i][k:k + 7]))
    odd = even = result = 0
    for l in range(8):
        if l % 2:
            even += number[l]
        else:
            odd += number[l]
    if (odd * 3 + even) % 10:
        result = 0
    else:
        result = odd + even
    print(f'#{t_c} {result}')
