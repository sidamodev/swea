import sys

sys.stdin = open('4408.txt', 'r')

T = int(input())
for t_c in range(1, T + 1):
    N = int(input())
    s, e = map(int, input().split())
    cnt = 0
    visited = [0] * 400
    max_v = 0
