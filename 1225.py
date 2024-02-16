import sys


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
        return self.q[(self.head + 1) % self.size]


sys.stdin = open('1225.txt', 'r')
for _ in range(1, 11):
    t_c = int(input())
    num_list = list(map(int, input().split()))
    q = que(9)
    for elem in num_list:
        q.en_que(elem)
    tmp = 0
    breaker = 0
    while breaker == 0:
        for i in range(1, 6):
            t_v = q.de_que()
            # print(q.head, q.tail)
            if t_v - i <= 0:
                q.en_que(0)
                breaker = 1
                break
            else:
                q.en_que(t_v - i)
    result = [q.de_que() for _ in range(8)]
    print(f'#{t_c}',*result)