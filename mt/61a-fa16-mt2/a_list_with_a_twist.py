
lamb = 'da'
def da(da):
    def lamb(lamb):
        nonlocal da
        def da(nk):
            da = nk + ['da']
            da.append(nk[0:2])
            return nk.pop()
    da(lamb)
    return da([[1], 2]) + 3

da(lambda da: da(lamb))

"""
Global frame
lamb        'da'
da          -> func da(da) [parent=Global]

f1: da [parent=Global] 
da          X -> func λ(da) <line=13> [parent=Global]
            -> func da(nk) [parent=f3]
lamb        -> func lamb(lamb) [parent=f1]

Return Value    5

f2: λ <line=13> [parent=Global]
da          -> points to func lamb(lamb) [parent=f1]

Return Value    None 

f3: lamb [parent=f1]
lamb        'da'
Return Value    None 


# Error
f4: da [parent=f3]
nk          -> [↓]
               [1]
da          -> [↓, 2, 'da', ↓, 2]
               [1]         [1]
Return Value    2

# shadow copy
f4: da [parent=f3]
nk          -> [↓]
               [1]←       ←[←, 2]
da          -> [↑, 2, 'da', ↑] 

"""
