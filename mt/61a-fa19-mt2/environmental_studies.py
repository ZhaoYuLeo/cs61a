def power(cut):
    def wind(y):
        nonlocal cut
        cut, g = cut - 1, cut
        y = [e]
        return y is e
    if cut and not wind('y'):
        return power(cut)
    else:
        return [g, 'e']

g = 'p'
e = [g]
g = 2
e.append(power(1))




"""
Global frame:
power       -> func power(cut) [parent=Global] 
g           2
e           -> ['p', points to the return list in f3 frame] 

f1: power [parent=Global]
cut         0
wind        -> func wind(y) [parent=f1]
Return Value        -> points to the return list in f3 frame      

f2: wind [parent=Global]
y           -> [points to e]
g           1
Return Value        False

f3: power [parent=Global]
wind        -> func wind(y) [parent=f3]
cut         0
Return Value        [2, 'e']
"""
