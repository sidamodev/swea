import sys

sys.stdin = open('5097.txt', 'r')


class que:
    def __init__(self, size):
        self.size = size
        self.head = self.tail = 0
        self.q = [0] * size

    def en_que(self, value):
        self.tail = (self.tail + 1) % self.size
        self.q[self.tail] = value

    def de_que(self):
        self.head = (self.head + 1) % self.size
        return self.q[self.head]

    def peek(self):
        return self.q[(self.head + 1)]


T = int(input())
for t_c in range(1, T + 1):
    N, M = map(int, input().split())
    in_num = list(map(int, input().split()))
    q = que(N + 1)
    for elem in in_num:
        q.en_que(elem)

    for i in range(M):
        q.en_que(q.de_que())

    print(f'#{t_c} {q.peek()}')
