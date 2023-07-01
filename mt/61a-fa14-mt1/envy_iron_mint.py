def peace(today):
    harmony = love+2
    return harmony + today(love+1)

def joy(peace):
    peace, love = peace+2, peace+1
    return love // harmony

love, harmony = 3, 2
peace(joy)

"""
Global frame
peace   -> func peace(today) [parent=Global]
joy     -> func joy(peace) [parent=Global]
love    3
harmony 2

f1: peace [parent=Global]
today   -> points to the joy in global frame
harmony 5
Return Value 7

f2: joy [parent=Global]
peace   6
love    5
Return Value 2 #important, harmony == 2, where joy defined.
"""

def k(g, b):
    def n(s, a):
        return g-p
    return b(n(b, p))

g, p = 3, 7
k(p+1, lambda s: g+3)

"""
Global frame
k       ->  func k(g, b) [parent=Global]
g       3
p       7
            func λ(s) <line 36> [parent=Global] 

f1: k [parent=Global]
g       8
b       ->  points to λ <line 36> in global frame
n       ->  func n(s, a) [parent=f1]
Return Value    6

f3: n [parent=f1] 
s       ->  points to λ <line 36> in global frame
a       7   #attention, we found p in global frame, g in f1 frame.
Return Value    1

f2: λ <line 36> [parent=Global]
s       1
Return Value    6 #attention, we found g in global frame.
"""
