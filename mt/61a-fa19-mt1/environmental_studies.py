def oski(oski):
    x = 1
    if oski(2) > x:
        return oski

bear = lambda z: (lambda y: z + 3)(x + 4)
x, z = 11, 12
x = oski(bear)

"""
Global frame:
oski        -> func oski(oski) [parent=Global]
bear        -> func λ(z)<line=5> [parent=Global]
x           -> points to λ(z)<line=5> [parent=Global] 
z           12

f1: oski [parent=Global]
oski        -> points to λ(z)<line=5> [parent=Global]
x           1
Return Value    -> points to λ(z)<line=5> [parent=Global]


f2: λ [parent=Global]
z           2
Return Value    5

f3: λ [parent=2]
y           15
Return Value    5
"""
