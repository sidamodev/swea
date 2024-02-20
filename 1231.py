import sys

sys.stdin = open('1231.txt', 'r')


def inorder_traversal(v):
    if graph[v][1]:
        inorder_traversal(graph[v][1])
    print(graph[v][0], end='')
    if graph[v][2]:
        inorder_traversal(graph[v][2])


for test_case in range(1, 11):
    N = int(input())
    graph = [[None] * 3 for _ in range(N + 1)]
    for i in range(1, N + 1):
        input_str = [None] * 4
        tmp = input().split()
        for j, elem in enumerate(tmp):
            if j > 1:
                input_str[j] = int(elem)
            else:
                input_str[j] = elem
        graph[i][0] = input_str[1]
        graph[i][1] = input_str[2]
        graph[i][2] = input_str[3]
    print(f'#{test_case} ',end='')
    inorder_traversal(1)
    print()
