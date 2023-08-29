def f(L, x):
    L[1] = L
    def g(c, h, b):
        nonlocal x
        x = c
        if c == 0:
            b.append(5)
            b = L + b
            return h
        else:
            return g(c - 1, lambda: [c, x], b)
    p = g(1, None, [4])
    x += 3
    return p()
r = f([0, 0], 1)

"""
Global frame:
f       -> func f(L, x) [parent=Global]
r       -> points to list [1, 3] in f4

f1: f [parent=Global]
L       -> [0, |]
            ↑--┙ 
x       3 
g       -> func g(c, h, b) [parent=f1]
p       -> points to λ <line 13> in f2
Return Value:   -> points to list [1, 3] in f4

f2: g [parent=f1]
c       1
h       None
b       -> [0, 0, 4, 5] # Wrong: [4, 5], we pass link as argument, append will change the content in b, + will return a new one
Return Value:    -> points to λ <line 13> in f2

f3: g [parent=f1]
c       0
h       -> func λ <line 13> [parent=f2]
b       -> [0, points to L, 4, 5]
Return Value:    -> points to λ <line 13> in f2

f4: λ <line 13> [parent=f2]
Return Value:    -> [1, 3]
"""
