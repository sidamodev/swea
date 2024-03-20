from collections import deque


def bfs(x, y):
    queue = deque([(0, x)])
    memo = set()
    while queue:
        cnt, num = queue.popleft()
        if 0 >= num or num > 1000000 or num in memo:
            continue
        if num == y:
            return cnt
        memo.add(num)
        queue.append((cnt + 1, num * 2))
        queue.append((cnt + 1, num + 1))
        queue.append((cnt + 1, num - 1))
        queue.append((cnt + 1, num - 10))


for t_c in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    print(f'#{t_c} {bfs(N, M)}')
