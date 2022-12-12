from queue import PriorityQueue
#自定义排序方式：
#ListNode.__lt__ = lambda self, other:self.val<other.val
q = PriorityQueue()

q.put(4)
q.put(2)
q.put(5)
q.put(1)
q.put(3)
while not q.empty():
    next_item = q.get()
    print(next_item)
#1
#2
#3
#4
#5