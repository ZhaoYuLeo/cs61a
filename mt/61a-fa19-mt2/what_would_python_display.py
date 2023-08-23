class C:
    x = 'e'
    def f(self, y):
        self.x = self.x + y
        return self

    def __str__(self):
        return 'go'

class Big(C):
    x = 'u'
    def f(self, y):
        C.x = C.x + y
        return C.f(self, 'm')

    def __repr__(self):
        return '<bears>'


m = C().f('i')
n = Big().f('o')

def g(y):
    def h(x):
        nonlocal h
        k = 2
        if len(x) == 1:
            h = lambda x: y
            k = 1
        return [-x[0]] + h(x[k:])
    return h(y)

py = {3: {5: [7]}}
thon = {5: 6, 7: py}
thon[7][3] = thon

q = range(3, 5)
r = iter(q)
code = [next(r), next(iter(q)), list(r)]

"""
m is new C object with x equals to 'ei'

C.x = 'eo'

n is new Big object with x equals to 'um'

thon = {5: 6, 7: {3: {5: [7]}}}
thon = {5: 6, 7: {3: self}}

code = [3, 3, [4]]


>>> pow(10, 2)
100
>>> print(4, 5) + 1
4 5
Error
>>> [m.x, n.x]
['ei', 'um']
>>> [C.f(n, 'a').x, C().x]
['uma', eo]
>>> print(m, n)
go <bears> # Wrong: go go. Attention: str -> parent str -> repr 
>>> n
<bears>
>>> g([3, 4, 5])
[-3, -5, 3, 4, 5]
>>> py[3][5]
[7] # Wrong: 6. py -> {3: ↓}
                thon -> {5: 6,  7: ↑}
>>> py
{3: {5: 6, 7: {...}}}
>>> thon
{5: 6, 7: {3: {...}}}
>>> code
[3, 3, [4]]
"""
