from collections import deque#双端队列(double-ended queue)
d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())
#G
#H
#I

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
print(d)                                # show the representation of the deque
#deque(['f', 'g', 'h', 'i', 'j'])

d.pop()                          # return and remove the rightmost item
#'j'
d.popleft()                      # return and remove the leftmost item
#'f'
list(d)                          # list the contents of the deque
#['g', 'h', 'i']
d[0]                             # peek at leftmost item
#'g'
d[-1]                            # peek at rightmost item
#'i'

list(reversed(d))                # list the contents of a deque in reverse
#['i', 'h', 'g']
'h' in d                         # search the deque
#True
d.extend('jkl')                  # add multiple elements at once
print(d)
#deque(['g', 'h', 'i', 'j', 'k', 'l'])
d.rotate(1)                      # right rotation
print(d)
#deque(['l', 'g', 'h', 'i', 'j', 'k'])
d.rotate(-1)                     # left rotation
print(d)
#deque(['g', 'h', 'i', 'j', 'k', 'l'])

deque(reversed(d))               # make a new deque in reverse order
#deque(['l', 'k', 'j', 'i', 'h', 'g'])
d.clear()                        # empty the deque
d.pop()                          # cannot pop from an empty deque
#Traceback (most recent call last):
#    File "<pyshell#6>", line 1, in -toplevel-
#        d.pop()
#IndexError: pop from an empty deque

d.extendleft('abc')              # extendleft() reverses the input order
print(d)
#deque(['c', 'b', 'a'])