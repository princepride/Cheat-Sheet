class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.tree = [0] * (4 * len(array))

    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = self.array[start]
        else:
            mid = (start + end) // 2
            self.build_tree(2 * node, start, mid)
            self.build_tree(2 * node + 1, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return float("inf")
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        q1 = self.query(2 * node, start, mid, left, right)
        q2 = self.query(2 * node + 1, mid + 1, end, left, right)
        return min(q1, q2)