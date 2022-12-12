class UnionFind:
    def __init__(self, n):
        self.count = n
        self.father = [i for i in range(n)]
    
    def find(self, x):
        if self.father[x] == x:
            return x
        return self.find(self.father[x])
    
    def connect(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.father[rootA] = rootB
            self.count -= 1
            