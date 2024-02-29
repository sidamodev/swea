T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    result = i = 0
    while i < N:
        j = i
        for k in range(i, N):
            if price[k] >= cur_max:
                cur_max = price[k]
                j = k
        sum_acc = cnt = 0
        for p in range(i, j):
            sum_acc += price[p]
            cnt += 1
        result += cur_max * cnt - sum_acc
        i = j + 1

    print(result)
