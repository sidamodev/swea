import sys

sys.stdin = open('2115.txt', 'r')
T = int(input())


def calc_profit(lev, v, s, bultong, len_arr):
    global tmp_max
    if lev == len_arr:
        if v > tmp_max and s <= C:
            tmp_max = v
        return
    if s + bultong[lev] <= C:
        calc_profit(lev + 1, v + bultong[lev] ** 2, s + bultong[lev], bultong, len_arr)
    calc_profit(lev + 1, v, s, bultong, len_arr)


for t_c in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N - M + 1):
            tmp_max = 0
            arr1 = arr[i][j:j + M]  # 위 벌통
            len_arr1 = len(arr1)
            calc_profit(0, 0, 0, arr1, len_arr1)
            profit1 = tmp_max
            for p in range(i, N):  # 아래 벌통
                for q in range(N - M + 1):
                    if i == p and q <= j + M: continue
                    tmp_max = 0
                    arr2 = arr[p][q:q + M]
                    len_arr2 = len(arr2)
                    calc_profit(0, 0, 0, arr2, len_arr2)
                    profit2 = tmp_max
                    if profit1 + profit2 > max_v:
                        max_v = profit1 + profit2
    print(f'#{t_c} {max_v}')
