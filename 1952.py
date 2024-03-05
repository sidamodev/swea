import sys

sys.stdin = open('1952.txt', 'r')

T = int(input())

# 그리디인가 dfs인가 dp인가..

for t_c in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    dp = [0] * len(plan)

