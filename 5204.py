T = int(input())
from collections import deque


def merge_sort(arr):
    len_arr = len(arr)
    if len_arr == 1:
        return arr
    left, right = deque(), deque()
    middle = len_arr // 2
    for i in range(len_arr):
        if i < middle:
            left.append(arr[i])
        else:
            right.append(arr[i])
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(l, r):
    global cnt
    result = deque()
    if l[len(l) - 1] > r[len(r) - 1]:
        cnt += 1
    while len(l) > 0 or len(r) > 0:
        if len(l) > 0 and len(r) > 0:
            if l[0] <= r[0]:
                result.append(l.popleft())
            else:
                result.append(r.popleft())
        elif len(l) > 0:
            result.append(l.popleft())
        elif len(r) > 0:
            result.append(r.popleft())
    return result


for t_c in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(A)[N // 2]
    print(f'#{t_c} {result} {cnt}')
