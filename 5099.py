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

sys.stdin = open('5099.txt', 'r')
T = int(input())
for _ in range(1, T + 1):
