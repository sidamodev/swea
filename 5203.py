import sys

sys.stdin = open('5203.txt', 'r')

T = int(input())


def solve(p_deck, player):
    global winner
    path = [0] * 12
    cnt = 0
    for elem in p_deck:
        path[elem] += 1
    if 3 in path:
        winner = player
        return
    for i in range(len(path)):
        if path[i] >= 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            winner = player
            return


for t_c in range(1, T + 1):
    deck = list(map(int, input().split()))
    winner = 0
    p_1, p_2 = [], []
    for i in range(12):
        if i % 2:
            p_2.append(deck[i])
            if i >= 5:
                solve(p_2, 2)
                if winner != 0: break
        else:
            p_1.append(deck[i])
            if i >= 4:
                solve(p_1, 1)
                if winner != 0: break
    print(f'#{t_c} {winner}')
