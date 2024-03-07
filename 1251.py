import sys
import math

sys.stdin = open('1251.txt', 'r')

T = int(input())
# 지옥의 하나로마트

for t_c in range(1, T + 1):
    N = int(input())
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))
    E = float(input())
    MST = [0xfffffff] * N
    for i in range(N - 1):
        for j in range(i + 1, N):
            dst = math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
            if dst < MST[i]:
                MST[i] = dst
    print(MST)
