def square(x):
    return x * x

def argentina(n):
    print(n)
    if n > 0:
        return lambda k: k(n+1)
    else:
        return 1 / n

def germany(n):
    if n > 1:
        print('hallo')
    if argentina(n-2) >= 0:
        print('bye')
    return argentina(n+2)

"""
(a)
>>> print(1, print(2))
2
1 None
>>> argentina(0)
0
Error
>>> argentina(1)(square)
1
4
>>> germany(1)(square)
-1
3
16
>>> germany(2)(germany)
hallo
0
Error
"""

(lambda t: argentina(t)(germany)(square))(0.5)
