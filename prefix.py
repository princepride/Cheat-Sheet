from itertools import accumulate

# 示例列表
lst = [1, 2, 3, 4, 5]

# 计算前缀和
prefix_sum = list(accumulate(lst))

print(prefix_sum)