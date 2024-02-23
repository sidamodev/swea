import sys
import pprint

sys.stdin = open('1242.txt', 'r')
T = int(input())


def find_start(start):
    for i in range(start, N):
        for char in code[i]:
            if char != '0' and char in hex_dict.keys():
                return i


hex_dict = {
    '0': "0000",
    '1': "0001",
    '2': "0010",
    '3': "0011",
    '4': "0100",
    '5': "0101",
    '6': "0110",
    '7': "0111",
    '8': "1000",
    '9': "1001",
    'A': "1010",
    'B': "1011",
    'C': "1100",
    'D': "1101",
    'E': "1110",
    'F': "1111"
}

code_dict = {
    '3211': 0,
    '2221': 1,
    '2122': 2,
    '1411': 3,
    '1132': 4,
    '1231': 5,
    '1114': 6,
    '1312': 7,
    '1213': 8,
    '3112': 9
}

for t_c in range(1, T + 1):
    N, M = map(int, input().split())
    code = [input().strip() for _ in range(N)]
    tmp_str = ''
    result = 0
    for elem in code[find_start(0)]:
        tmp_str += hex_dict[elem]
    K = M * 4 - 1
    for i in range(K, -1, -1):
        if tmp_str[i] == '1':
            break
    mul, flag = 1, False
    # print(i, start_j)
    # print(tmp_str)
    # print(tmp_str[start_j:start_j + 7])
    start_j = i - 55
    cnt_n = ''
    while True:
        cnt_idx = 0
        cnt_lst = [0, 0, 0, 0]
        pre_v = '0'
        for k in range(mul * 7):
            if tmp_str[start_j + k] == pre_v:
                cnt_lst[cnt_idx] += 1
            else:
                cnt_idx += 1
                if cnt_idx > 3: break
                cnt_lst[cnt_idx] += 1
            pre_v = tmp_str[start_j + k]
        if min(cnt_lst):
            for idx_cnt in range(4):
                cnt_lst[idx_cnt] //= min(cnt_lst)
        cnt_str = ''.join(map(str, cnt_lst))
        if cnt_str in code_dict.keys():
            break
        if start_j - 55 * mul > 0:
            start_j -= 55 * mul
        else:
            break
        mul += 1
    if 0 in cnt_lst:
        result = 0
    else:
        result = 1
    print(cnt_str)
    # print(start_j)
# pprint.pprint(code)
