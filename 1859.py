T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    val = list(map(int, input().split()))
    i = sum_v = 0
    while i < N:
        max_i = i
        for j in range(i, N):
            if val[j] > val[max_i]:
                max_i = j
        for k in range(i, max_i):
            sum_v += val[max_i] - val[k]
        i = max_i + 1
    print(f'#{test_case} {sum_v}')
