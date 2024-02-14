import sys

sys.stdin = open('4881.txt', 'r')


def solve(i, sum_n):
    global min_v
    if i == N:
        min_v = sum_n
        return
    else:
        for j in range(N):
            if visit[j] == 0 and sum_n + arr[i][j] < min_v:
                print(i,j)
                print(visit)
                visit[j] = 1
                solve(i + 1, sum_n + arr[i][j])  # 부모 노드로 이동
                visit[j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 100
    visit = [0] * N
    solve(0, 0)
    print(min_v)
