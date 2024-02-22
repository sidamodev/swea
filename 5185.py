# '''
# 3
# 4 47FE
# 5 79E12
# 8 41DA16CD
# '''
#
T = int(input())
for t_c in range(1, T + 1):
    num = input().split()[1]
    total = ''
    for n in num:
        if not n.isnumeric():
            n = ord(n) - 55
        n = int(n)
        res = ''
        while n >= 0 and len(res) < 4:
            if n % 2:
                res += '1'
            else:
                res += '0'
            n //= 2
        total += res[::-1]
    print(f'#{t_c} {total}')
bin_dic = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101',
    'E': '1110', 'F': '1111'
}

T = int(input())

for tc in range(1, T + 1):
    N, arr = input().split()
    N = int(N)
    lst = ''
    # result = solve()
    print(f'#{tc}', end=' ')
    for j in range(N):
        lst += bin_dic[arr[j]]
    print(lst)
