import sys
import pprint

sys.stdin = open('2806.txt', 'r')


def dfs(i):
    global cnt
    if i == N:
        cnt += 1
        return
    for k in range(N):
        if chk[k] == -1:
            for j in range(N):
                if chk[j] != -1 and abs(chk[j] - i) == abs(k - j):
                    break
            else:
                chk[k] = i
                dfs(i + 1)
                chk[k] = -1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    chk = [-1] * N
    dfs(0)
    print(f'#{tc} {cnt}')
