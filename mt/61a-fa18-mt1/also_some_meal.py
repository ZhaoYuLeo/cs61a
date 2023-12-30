def al(so):
    me = 1
    def al(to):
        return so + me
    so = 2
    return al

def me(al):
    me = 3
    return al(lambda: 4) + so

so = 5
so = me(al(6)) + so

"""
Global frame
al          →   func al(so) [parent=Global]
me          →   func me(al) [parent=Global]
so          13


f1: al [parent=Global]
so          2
me          1
al          →   func al(to) [parent=f1]
Return Value    points to func al(to) [parent=f1]

f2: me [parent=Global]
al          →   points to func al(t) [parent=f1]
me          3
            → func λ <line=10> [parent=f2] 
Return Value    8

f3: al  [parent=f1]
to          →   points to func λ <line=10> [parent=f2]
Return Value    3
"""
