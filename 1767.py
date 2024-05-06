import sys, pprint

sys.stdin = open('1767.txt', 'r')
T = int(input())

d_ij = ((0, 1), (0, -1), (1, 0), (-1, 0))


def connect(d, core):
    ni, nj = core[0] + d_ij[d][0], core[1] + d_ij[d][1]
    wire_cnt = core_cnt = 0
    # 전원까지 연결 여부를 파악
    while (0 <= ni < N and 0 <= nj < N) and arr[ni][nj] == 0:
        ni, nj = ni + d_ij[d][0], nj + d_ij[d][1]
    # 연결되었다면 전선 표시하기
    if ni == -1 or ni == N or nj == -1 or nj == N:
        # 코어 기준 좌표 다시 초기화
        ni, nj = core[0] + d_ij[d][0], core[1] + d_ij[d][1]
        core_cnt = 1
        # 전원에 닿을 때까지 2 표시 반복
        while 0 <= ni < N and 0 <= nj < N:
            wire_cnt += 1
            arr[ni][nj] = 2
            ni, nj = ni + d_ij[d][0], nj + d_ij[d][1]
    return wire_cnt, core_cnt


def disconnect(d, core):
    ni, nj = core[0] + d_ij[d][0], core[1] + d_ij[d][1]
    while 0 <= ni < N and 0 <= nj < N:
        arr[ni][nj] = 0
        ni, nj = ni + d_ij[d][0], nj + d_ij[d][1]


# 연결한 코어 개수, 누적 전선 길이, 연결한 코어 개수
# 최대 코어 개수에서 하나씩 감소
def dfs(lev, acc_len, core_total):
    global max_core, min_wire
    if lev == K:
        if core_total > max_core:
            max_core = core_total
            min_wire = acc_len
        elif core_total == max_core and acc_len < min_wire:
            min_wire = acc_len
        return
    if max_core > core_total + K - lev:
        return
    for k in range(4):  # 4방향 코어 연결
        tmp_wire, tmp_cnt = connect(k, core_lst[lev])
        if not tmp_cnt: continue
        dfs(lev + 1, acc_len + tmp_wire, core_total + 1)
        # 백트래킹 -> 이전 가지로 돌아가기
        disconnect(k, core_lst[lev])
        # 해당 프로세서를 연결하지 않고 넘어가는 경우
    dfs(lev + 1, acc_len, core_total)


for t_c in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    core_lst = [(i, j) for i in range(N) for j in range(N) if not (i == 0 or i == N or j == 0 or j == N) and arr[i][j]]
    max_core = 0
    min_wire = int(1e9)
    K = len(core_lst)
    dfs(0, 0, 0)
    print(f'#{t_c} {min_wire}')
