
def splash(klay, curry):
    while curry == 3:
        steph = klay
        klay = lambda klay: steph(curry + 1)
        curry = curry + 2
        return klay
    return curry // 5

steph = lambda klay: splash(11, curry) - 3
steph, curry = splash(steph, 3), 30
steph(4)


"""
Global frame
splash      -> func splash(klay, curry) [parent=Global]
steph       -> points λ<line=5>
curry       30

f1: splash [parent=Global]
klay        -> func λ(klay) <line=5> [parent=f1]
curry       5
steph       -> func λ(klay) <line=10> [parent=Global]
Return Value    -> points λ<line=5>

f2: λ <line=5> [parent=f1]
klay        4
Return Value    3

f3: λ <line=10> [parent=Global]
klay        6
Return Value    3

f4: splash [parent=Global]
klay        11
curry       30
Return Value    6
"""

