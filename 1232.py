import sys

sys.stdin = open('1232.txt', 'r')


def in_trav(n):
    if g[n - 1][1] in '+-*/':
        l = in_trav(int(g[n - 1][2]))
        r = in_trav(int(g[n - 1][3]))
        if g[n - 1][1] == '+':
            return l + r
        elif g[n - 1][1] == '-':
            return l - r
        elif g[n - 1][1] == '*':
            return l * r
        elif g[n - 1][1] == '/':
            return l / r
    else:
        return int(g[n - 1][1])


for t_c in range(1, 11):
    N = int(input())
    g = [input().split() for _ in range(N)]
    print(f'#{t_c} {int(in_trav(1))}')
