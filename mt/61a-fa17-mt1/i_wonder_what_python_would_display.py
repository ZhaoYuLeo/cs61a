aaron, burr = 2, 5
aaron, burr = 4, aaron + 1

hamil = 10

def alex(hamil):
    def g(w):
        hamil = 2 * w
        print(hamil, w)
        w = hamil
        return hamil
    w = 5
    alex = g(w + 1)
    print(w, alex, hamil)


def el(i, za):
    def angelica():
        return i + 1
    if i > 10:
        return za()
    elif i > 4:
        print(angelica())
        return el(i * i, za)
    else:
        return el(i * i, angelica)


K = lambda x: lambda y: x

def pr(x):
    print(x)
    return x

"""
>>> pow(2, 3)
8
>>> print(4, 5) + 1
4 5
Error
>>> print(aaron, burr)
4 3
>>> alex(3)
12 6
5 12 3
>>> el(3, el)
10
4
>>> K
Function
>>> K(3)
Function
>>> K(3)(2)
3
>>> pr(True) and pr(0) and pr(1)
True
0
0
"""
