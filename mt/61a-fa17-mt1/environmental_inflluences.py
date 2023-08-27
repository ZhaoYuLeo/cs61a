x = 1
def f(n):
    def g():
        return n + x
    x = n + 5
    if n % 3 == 0:
        return g
    else:
        return f(n + 1)

x = 10
z = f(2)
q = x + z()

"""
Global frame
x       10
f       -> func f(n) [parent=Global]
z       -> points to func g [parent=f2]
q       21

f1: f [parent=Global]
n       2
g       -> func g [parent=f1]
x       7
Return Value    points to func g [parent=f2]


f2: f [parent=Global]
n       3
g       -> func g [parent=f2]
x       8
Return Value    points to func g [parent=f2]

f3: g [parent=f2]
Return Value    11
"""
