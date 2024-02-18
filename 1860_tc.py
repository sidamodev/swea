import sys

sys.stdin = open('1860_tc_out.txt', 'r')
impossible = 0
possible = 0
for i in range(1000):
    input_str = input().split()
    if input_str[1] == 'Impossible':
        impossible += 1
    else:
        possible += 1
print(possible, impossible)
