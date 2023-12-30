identity = lambda x: x
increment = lambda x: x + 1

def fif(c, t, f, x):
    if c(x):
        return t(x)
    else:
        return f(x)

def bounce(x, y):
    while x < y:
        if x <= (y and x):
            print('a');
        if x > 0:
            print('b')
        elif x > -5:
            print('c')
        x, y = -y, increment(x - y)
        print(y)

crazy = lambda rich : 100 * rich
crazy = lambda rich : crazy(crazy(rich))

def ok(py):
    def h(w):
        print(py // 10)
        return ok(py)
    return lambda h: h(py)

"""
>>> pow(10, 2)
100
>>> print(4, 5) + 1
4 5
Error
>>> print(None, print(1, 2))
1 2
None None
>>> fif(abs, print, print, -2)
-2

>>> bounce(1, 2)
a
b
0
a
c
-1
>>> crazy(88)
Error/Forever
>>> ok(314)(identity)
314
"""

