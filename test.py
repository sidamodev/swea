in_str = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
data = list(map(int, in_str.split()))
V = 13

g = [[None] * 2 for _ in range(V + 1)]
for i in range(0, (V - 1) * 2, 2):
    if not g[data[i]][0]:  # node 번호가 0번부터 시작 -> not g[data[i]][0] == 0
        g[data[i]][0] = data[i + 1]
    else:
        g[data[i]][1] = data[i + 1]


def pre_order(v):
    if v is None:
        return
    pre_order(g[v][0])
    print(v, end=' ')
    pre_order(g[v][1])


pre_order(1)
print()
print(g)