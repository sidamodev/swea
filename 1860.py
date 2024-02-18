import sys
p=q=0
sys.stdin = open('1860.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    result = 0
    customer_lst = list(map(int, input().split()))
    min_time = min(customer_lst)
    if min_time < M:
        q += 1

        pass
    else:
        count_time = [0] * 11112
        n_acc = 0
        for elem in customer_lst:
            count_time[elem] += 1
        for i, n in enumerate(count_time):
            if n:
                n_acc += n
                sum_acc = i // M * K - n_acc
                if sum_acc < 0:
                    q+=1
                    break
        else:
            p += 1

            result = 1
    print(f"#{test_case} {'Possible' if result else 'Impossible'}")
print(p,q)