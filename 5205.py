T = int(input())


def qck_sort(l, r):
    if l < r:
        i, j = l, r
        p = A[l]
        while i <= j:
            while i <= j and A[i] <= p: i += 1
            while i <= j and A[j] >= p: j -= 1
            if i < j: A[i], A[j] = A[j], A[i]
        A[l], A[j] = A[j], A[l]
        qck_sort(l, j - 1)
        qck_sort(j + 1, r)


for t_c in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    qck_sort(0, N - 1)
    print(f'#{t_c} {A[N // 2]}')
