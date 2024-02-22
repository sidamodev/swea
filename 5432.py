import sys

sys.stdin = open('5432.txt', 'r')
T = int(input())
for t_c in range(1, T + 1):
    input_lst = list(input())
    # )( -> 마디, 쇠막대의 끝
    # 스택에 누적된 여는 괄호가 없음 -> 버리는 레이저
    # 가장 인접한 여는 괄호에서 닫는 괄호까지 괄호쌍의 수 + 1 누적
    # 반복문 -> 붙은 괄호쌍을 제외하고 구간내 레이저의 개수 + 1
    stk = ['(']
    cnt = 0
    laser = pipe = 0
    i = 1
    while i < len(input_lst):
        print(stk)
        if input_lst[i] == '(':
            stk.append(input_lst[i])
            if not stk:
                print(pipe, laser)
                cnt += pipe * (laser + 1)
                laser = 0
                pipe = 0
        else:
            if input_lst[i - 1] == '(':
                stk.pop()
                laser += 1
            else:
                stk.pop()
                pipe += 1
        i += 1
    print(cnt)