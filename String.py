s = "abcd"
s.find('bc') # 1
s.find('abe') # -1
s.replace('a','e') # 'ebcd'
s[:-2] # 'eb'
s.upper() # 'EBCD'
s.lower() # 'ebcd'
a = "  abcd   "
a.strip() # "abcd"
a.lstrip() # "abcd   "
a.rstrip() # "  abcd"
import re  
str = "A man, a plan, a canal: Panama"
print(re.sub("[^a-zA-Z0-9]", "", str))
# "AmanaplanacanalPanama"