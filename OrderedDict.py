from collections import OrderedDict
cache = OrderedDict()
cache['a'] = 1
cache['b'] = 2
cache['c'] = 3
cache['d'] = 4
cache['e'] = 5
print(cache)
#OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
cache.pop('b')
print(cache)
#OrderedDict([('a', 1), ('c', 3), ('d', 4), ('e', 5)])
cache['b'] = 2
print(cache)
#OrderedDict([('a', 1), ('c', 3), ('d', 4), ('e', 5), ('b', 2)])
cache.popitem(last=False)
print(cache)
#OrderedDict([('c', 3), ('d', 4), ('e', 5), ('b', 2)])
cache.popitem()
print(cache)
#OrderedDict([('c', 3), ('d', 4), ('e', 5)])
cache.move_to_end('c')
print(cache)
#OrderedDict([('d', 4), ('e', 5), ('c', 3)])