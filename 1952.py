import sys

sys.stdin = open('1952.txt', 'r')

T = int(input())


def dp(i):
    if i == 0:
        return 0
    if memo[i]:
        return memo[i]
    else:
        memo[i] = min(dp(i - 1) + (plan[i] * price[0]), dp(i - 1) + price[1])
        if i >= 3:
            memo[i] = min(memo[i], dp(i - 3) + price[2])
        return memo[i]

for t_c in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    memo = [0] * 13
    dp(12)
    print(f'#{t_c} {min(memo[12], price[3])}')
