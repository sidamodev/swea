import sys

sys.stdin = open('4880.txt', 'r')
def solve(start, end):
    mid = (start + end) // 2

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input().split()))
