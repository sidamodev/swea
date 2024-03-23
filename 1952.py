import sys

sys.stdin = open('1952.txt', 'r')

T = int(input())


def dfs(i, cost):
    global result
    if cost >= result:
        return
    if i >= 12:
        if cost < result:
            result = cost
        return
    day_cost = price[0] * plan[i]
    if day_cost < price[1]:
        dfs(i + 1, cost + day_cost)
    else:
        dfs(i + 1, cost + price[1])
    dfs(i + 3, cost + price[2])


for t_c in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    result = 9999
    dfs(0, 0)
    print(f'#{t_c} {min(result, price[3])}')
