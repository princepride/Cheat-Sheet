class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
            self.count -= 1

# 复杂版，包括启发式合并，查询时自动优化
class UnionFind:
    def __init__(self, num_nodes):
        self.parent = list(range(num_nodes))  # 父节点数组
        self.rank = [1] * num_nodes  # 节点深度
        self.num_sets = num_nodes  # 并查集中的集合数量

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return False
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root1] = root2
            self.rank[root2] += 1
        self.num_sets -= 1  # 合并两个集合时，集合数量减少
        return True
