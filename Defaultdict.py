from collections import defaultdict
d = defaultdict(lambda: -1)
print(d['a']) # -1
d['a'] += 1
print(d['a']) # 0
d['a'] = 2
print(d['a']) # 2

dic = {}
dic['a'] = dic.get('a', 0) + 1 # get()返回键值'a'，若没有则返回0
sorted(dic.items(), key = lambda kv: -kv[1]) #按值从大到小排序
sorted(dic.items(), key = lambda kv: kv[0]) #按键从小到大排序