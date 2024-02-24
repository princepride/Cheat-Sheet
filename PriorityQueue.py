from queue import PriorityQueue
# 自定义排序方式：
# ListNode.__lt__ = lambda self, other:self.val<other.val
q = PriorityQueue()

q.put(4)
q.put(2)
q.put(5)
q.put(1)
q.put(3)

# get()方法移除并返回堆顶元素
while not q.empty():
    next_item = q.get()
    print(next_item)
#1
#2
#3
#4
#5

# 返回所有最小的元素
import heapq
def heap_pop_all(h):
    min_elements = []
    min_element = heapq.heappop(h)
    min_elements.append(min_element)
    while h and h[0] == min_element:
        # 如果是，弹出并添加到结果列表中
        min_elements.append(heapq.heappop(h))
    return min_elements

# 针对某一属性的优先队列, 元组的第一项
data = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
h = [(item[2], item) for item in data]
heapq.heapify(h)
