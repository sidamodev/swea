import sys

sys.stdin = open('5208.txt', 'r')

T = int(input())




for t_c in range(1, T + 1):
    bat = list(map(int, input().split()))
    min_change = max(bat)
    chk = [0] * len(bat)
    print(min_change)
