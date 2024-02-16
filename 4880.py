import sys

sys.stdin = open('4880.txt', 'r')


def solve(start, end):
    mid = (start + end) // 2
    if end == start:
        return start
    winner1 = solve(start, mid)
    winner2 = solve(mid + 1, end)
    result = winner1
    if card_list[winner1] > card_list[winner2]:
        if card_list[winner1] == 3 and card_list[winner2] == 1:
            result = winner2
        else:
            result = winner1
    elif card_list[winner1] < card_list[winner2]:
        if card_list[winner1] == 1 and card_list[winner2] == 3:
            result = winner1
        else:
            result = winner2
    elif card_list[winner1] == card_list[winner2]:
        result = winner1 if winner1 < winner2 else winner2
    return result

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input().split()))
    print(f'#{test_case} {solve(0, N - 1) + 1}')
