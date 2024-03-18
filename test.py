# quick sort by indexing

arr = [7, 5, 4, 1, 2, 10, 3, 6, 9, 8]


def partition(l, r):
    # 가장 좌측 요소를 pivot으로 설정
    pivot = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= pivot: i += 1
        while i <= j and arr[j] >= pivot: j -= 1
        if i < j: arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def qck_sort(l, r):
    if l < r:
        p = partition(l, r)
        qck_sort(l, p - 1)
        qck_sort(p + 1, r)


qck_sort(0, len(arr) - 1)
print(arr)
