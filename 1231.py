import sys

sys.stdin = open('1231.txt', 'r')


def in_trav(n):
    if n > N:
        return
    in_trav(n * 2)
    result.append(g[(n - 1)][1])
    in_trav(n * 2 + 1)

for t_case in range(1, 11):
    N = int(input())
    g = [input().split() for _ in range(N)]
    result = []
    in_trav(1)
    print(f"#{t_case} {''.join(result)}")
