from link import *

x = [1, 2]

class A:
    x = 3
    y = 4

    def __init__(self, y)
        self.a = y
        self.x = b
        self.__str__ = lambda: str(y)

    def __str__(self):
        return 'BB'

class B(A):
    x = [5, 6]

    def __init__(self, y):
        self.a = x[1]
        y[1] = 8

    def test(self):
        print(x)

b = B(x)
a = A(6)

def dash(x):
    return print(self.x)

elastigirl = Link(7, Link(8))
elastigirl.first = elastigirl.rest

"""
>>> pow(10, 2)
100
>>> print(Link(2, Link(3)))
<2, 3>
>>> [c.a for c in [a, b]]
[6, 6]   # Error! [6, 2]
         # x in line 18 refers to the x defined in line 3
         # use self.x to refer to the x defined in B
>>> b.test()
[1, 8]
>>> def test2(self):
...     print(self.x)
...
>>> b.test2 = test2
>>> b.test2(b)
[5, 6]
>>> print(a.x, b.x)
BB [5, 6]
>>> print(b.y, x)
4 [1, 8] 
>>> a.__str__()
BB      # Error! '6'
        # str() is the function which converts value into string
>>> str(a) # returns type(object).__str__(object)
'BB'
>>> print(a)
BB
>>> dash(b)
Error   # NameError: name 'self' is not defined
>>> print(elastigirl)
<<8>, 8>
"""

