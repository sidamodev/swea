T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    customer_lst = list(map(int, input().split()))
    result = n_acc = 0
    count_time = [0] * 11112
    for elem in customer_lst:
        count_time[elem] += 1
    for i, n in enumerate(count_time):
        if n:
            n_acc += n
            sum_bread = i // M * K - n_acc
            if sum_bread < 0:
                break
    else:
        result = 1
    print(f"#{test_case} {'Possible' if result else 'Impossible'}")
