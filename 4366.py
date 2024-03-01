import sys

sys.stdin = open('4366.txt', 'r')

T = int(input())
for t_c in range(1, T + 1):
    memo_bin = input()
    memo_trn = input()
    bin_set, trn_set = set(), set()
    for i in range(len(memo_bin)):
        bin_set.add(int(memo_bin, 2) ^ 1 << i)
    for j in range(len(memo_trn)):
        trn_num = list(memo_trn)
        if memo_trn[j] == '1':
            trn_num[j] = '0'
            trn_set.add(int(''.join(trn_num), 3))
            trn_num[j] = '2'
            trn_set.add(int(''.join(trn_num), 3))
        elif memo_trn[j] == '2':
            trn_num[j] = '0'
            trn_set.add(int(''.join(trn_num), 3))
            trn_num[j] = '1'
            trn_set.add(int(''.join(trn_num), 3))
        else:
            trn_num[j] = '1'
            trn_set.add(int(''.join(trn_num), 3))
            trn_num[j] = '2'
            trn_set.add(int(''.join(trn_num), 3))

    print(f'#{t_c} {(bin_set & trn_set).pop()}')
