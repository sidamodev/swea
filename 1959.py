import sys

sys.stdin = open('1959.txt', 'r')
for t_c in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_v = 0
    if N < M: N, M, A, B = M, N, B, A
    for i in range(N - M + 1):
        tmp_sum = 0
        for j in range(M): tmp_sum += A[j + i] * B[j]
        if tmp_sum > max_v: max_v = tmp_sum
    print(f'#{t_c} {max_v}')
