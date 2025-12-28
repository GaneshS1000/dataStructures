#program to make use of Ordered Dict

from collections import OrderedDict

d = OrderedDict()
d.update({1:'a',2:'b',4:'d'})
print(d)
d[3]='c'
print(d.keys())

d1 = dict()
d1.update({1:'a',2:'b',4:'d'})
d1[3]='c'
print(d1)
print(d1.keys())