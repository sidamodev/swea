# import sys
#
# sys.stdin = open('1861.txt', 'r')

T = int(input())

for t_c in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    d_ij = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt_lst = [1] * (N ** 2 + 1)
    for i in range(N):
        for j in range(N):
            p, q = i, j
            while True:
                for di, dj in d_ij:
                    ni, nj = p + di, q + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == arr[p][q] + 1:
                            cnt_lst[arr[i][j]] += 1
                            p, q = ni, nj
                            break
                else:
                    break

    print(f'#{t_c} {cnt_lst.index(max(cnt_lst))} {max(cnt_lst)}')
