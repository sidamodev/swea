def merge_sort(arr, N):
    len_arr = len(arr)
    # 인덱스만 조작해서 실행시간 단축하기
    if len_arr == 1:
        return arr
    m = len_arr // 2
    return merge(merge_sort(left), merge_sort(right))


def merge(l, r):
    global cnt
    len_l, len_r = len(l), len(r)
    result = []
    if l[len_l - 1] > r[len_r - 1]:
        cnt += 1
    i = j = 0
    while len_l > i or len_r > j:
        if len_l > i and len_r > j:
            if l[i] <= r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        elif len_l > i:
            result.append(l[i])
            i += 1
        elif len_r > j:
            result.append(r[j])
            j += 1
    return result


for t_c in range(1, int(input()) + 1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    print(f'#{t_c} {merge_sort(A)[N // 2]} {cnt}')
