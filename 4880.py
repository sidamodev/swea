import sys

sys.stdin = open('4880.txt', 'r')


def solve(start, end):
    winner = 0
    if end == start:
        return start
    mid = (start + end) // 2
    result = 0
    winner1 = solve(start, mid)
    winner2 = solve(mid + 1, end)
    if card_list[winner1] == 1:
        if card_list[winner2] == 3:
            winner = card_list[winner1]
    elif card_list[winner1] < card_list[winner2]:
        winner = card_list[winner2]
    elif card_list[winner1] > card_list[winner2]:
        if card_list[winner2] != 1:
            winner = winner1
    return winner


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input().split()))
    print(solve(0, N))
