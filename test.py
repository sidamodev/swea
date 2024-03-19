lst = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
arr = list(map(int, lst.split()))


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child):
        if not self.left:
            self.left = child
            return

        if not self.right:
            self.right = child
            return
        return

    def inorder(self):
        # self가 0인 경우도 고려..
        if self is not None:
            if self.left:
                self.left.inorder()
            print(self.value, end=' ')
            if self.right:
                self.right.inorder()

    def preorder(self):
        if self is not None:
            print(self.value, end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self is not None:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.value, end=' ')


nodes = [TreeNode(i) for i in range(14)]

for i in range(0, len(arr), 2):
    p, c = arr[i], arr[i + 1]
    nodes[p].insert(nodes[c])

nodes[1].postorder()