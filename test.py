from collections import deque

graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3]
]

visited = [0] * len(graph)
path = []


# def dfs(node):
#     for neighbor in graph[node]:
#         if visited[neighbor]:
#             continue
#
#         visited[neighbor] = 1
#         path.append(neighbor)
#         dfs(neighbor)


def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if visited[neighbor]:
                continue
            visited[neighbor] = 1
            print(visited)
            queue.append(neighbor)


visited[0] = 1
# path.append(0)
bfs(0)
