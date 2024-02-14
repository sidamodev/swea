def sub_set(i, k, t, s):
    cnt[0] += 1
    if s == t:  # 모든 원소에 대해 결정이 끝남
        for j in range(k):
            if bit[j]:
                print(A[j], end=' ')
        print()
    elif i == k:  # 모든 원소를 고려했으나 s != t
        return
    elif s > t:  # 합이 초과 -> 남은 원소를 고려할 필요가 없음
        return
    else:  # 남은 원소가 있지만 s < t
        bit[i] = 1
        sub_set(i + 1, k, t, s + A[i])  # 포함된 경우
        bit[i] = 0
        sub_set(i + 1, k, t, s)  # 포함되지 않은 경우


N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N  # A의 각 원소의 부분집합 포함 유무 표시
cnt = [0]
sub_set(0, N, 1, 0)
print(cnt)
