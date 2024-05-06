for t_c in range(1, int(input()) + 1):
    N = int(input())
    A = list(map(int, input().split()))
    result = set()
    for i in range(1 << N):
        sum_v = 0
        for k in range(N):
            if i & (1 << k):
                sum_v += A[k]
        result.add(sum_v)
    print(f'#{t_c} {len(result)}')
