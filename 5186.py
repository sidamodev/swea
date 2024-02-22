T = int(input())
for t_c in range(1, T + 1):
    N = float(input())
    result = ''
    for i in range(1, 13):
        if N > 0:
            sub = 1 / (1 << i)
            if N >= sub:
                N -= sub
                result += '1'
            elif N <= sub:
                result += '0'
        else:
            break
    else:
        if N > 0:
            result = 'overflow'
    print(f'#{t_c} {result}')
