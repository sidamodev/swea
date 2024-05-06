import sys

sys.stdin = open('2117.txt', 'r')

T = int(input())
for t_c in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0  # 손해 없이 서비스 가능한 최대 가구 수
    home = [(i, j) for i in range(N) for j in range(N) if arr[i][j]]
    # 서비스 중심 : i, j
    for i in range(N):
        for j in range(N):
            for k in range(1, N + 2):  # N+1 까지
                # 서비스 비용
                cost = k * k + (k - 1) * (k - 1)
                # 서비스 영역 내부의 가구 수
                cnt = 0
                for p, q in home:
                    dis = abs(i - p) + abs(j - q)
                    if dis < k and arr[p][q]:
                        cnt += 1
                if cnt * M >= cost and cnt > max_v:
                    max_v = cnt
    print(f'#{t_c} {max_v}')
