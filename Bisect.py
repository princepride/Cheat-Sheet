import bisect
a = [1,3,3,3,5]
x = 3

t = bisect.bisect_left(a, x) # 返回可左插入的下标
t = bisect.bisect_right(a, x) # 返回可右插入的下标
bisect.insort_left(a, x) # 左插入
bisect.insort_right(a, x) # 右插入