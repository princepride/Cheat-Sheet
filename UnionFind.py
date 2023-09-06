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

# 复杂版，包括启发式合并，查询时自动优化，删除，移动
class UnionFind:
    def __init__(self, num_nodes):
        self.parent = list(range(num_nodes))  # 父节点数组
        self.rank = [1] * num_nodes  # 节点深度
        self.size = [1] * num_nodes  # 各集合的大小
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
            self.size[root1] += self.size[root2]
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.parent[root1] = root2
            self.rank[root2] += 1
            self.size[root2] += self.size[root1]
        self.num_sets -= 1
        return True

    def delete(self, x):
        root = self.find(x)
        # 如果 x 是根节点
        if root == x:
            for i in range(len(self.parent)):
                if self.find(i) == x:
                    self.parent[i] = i  # 重置为它们自己
            self.num_sets += self.size[root] - 1  # 增加集合数量
        else:
            self.size[root] -= 1
        self.parent[x] = x
        self.rank[x] = 1

    def move(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        # 如果 x 是根节点
        if root_x == x:
            for i in range(len(self.parent)):
                if self.find(i) == x:
                    self.parent[i] = i  # 重置为它们自己
            self.num_sets += self.size[root_x] - 1  # 增加集合数量
        else:
            self.size[root_x] -= 1
        self.parent[x] = root_y
        self.size[root_y] += 1
