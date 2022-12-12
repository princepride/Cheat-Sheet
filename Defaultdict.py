from collections import defaultdict
d = defaultdict(lambda: -1)
print(d['a']) # -1
d['a'] += 1
print(d['a']) # 0
d['a'] = 2
print(d['a']) # 2