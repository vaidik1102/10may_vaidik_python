#Write a Python program to combine two dictionary adding values for common keys.  d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}  Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).  
from collections import Counter
a1 = {'a': 100, 'b': 200, 'c':300}
a2 = {'a': 300, 'b': 200, 'd':400}
a = Counter(a1) + Counter(a2)
print(a)
