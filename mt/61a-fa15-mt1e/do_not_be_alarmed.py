def fire(alarm, y):
    if vlsb(y):
        return alarm(y+1)

def vlsb(x):
    print(x)
    if x > 3:
        return vlsb(x-1)
    return True

siren = lambda loud: fire(print, y)
y = 4

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

"""
>>> pow(2, 3)
8
>>> print(4, 5) + 1
4 5
Error
>>> compose1(print, print)(5)
5
None
>>> fire(vlsb, 1)
1
2
True
>>> fire(siren, 2)
2
4
3
5
"""
