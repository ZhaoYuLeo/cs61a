
equals = lambda a, b: a == b
nemo = lambda n: lambda: print(n)
ray = nemo(1)

def if_function(f, g, h):
    if h:
        f()
    elif h:
        f(f())
    else:
        print(5 or 6)
    g()

def dory():
    print('fish')
    return lambda: 1/0


"""
>>> pow(2, 3)
8
>>> print(4, 5) + 1
4 5
Error
>>> equals(3==4, equals(5, equals(5, 5)))
True
>>> print(print(print(2)), print(3))
2
None
3
None, None
>>> print(nemo(print(5))())
5
None
None
>>> if_function(nemo(3), dory, 2)
3
fish
>>> if_function(dory, nemo(2), ray())
1
5
2
"""
