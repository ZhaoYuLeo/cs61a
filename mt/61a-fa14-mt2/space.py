def locals(only):
    def get(out):
        nonlocal only
        def only(one):
            return lambda get: out
        out = out + 1
        return [out + 2]
    out = get(-only)
    return only
only = 3
earth = locals(only)
earth(4)(5)


"""
Global frame
locals  -> func locals(only) [parent=Global]
only    3
earth   -> points to the func only(one) [parent=f2]


f1: locals [parent=Global]
only    -> func only(one) [parent=f2] #used to be 3 but been overrided in the following operations
get     -> func get(out) [parent=f1]
out     -> points to list in f2
Return Value    -> points to func only [parent=f2]

f2: get [parent=f1]
out     -2
Return Value    -> [0]

f3: only [parent=f2]
one     4
Return Value    -> func λ(get) <line=5> [parent=f3]

f4: λ <line=5> [parent=f3]
get     5
Return Value    -2 #attention, out == -2
"""

spock, yoda = 1, 2
luke = [[yoda], [spock], yoda ]
yoda = 0
yoda = [luke, luke[yoda][yoda] ]
yoda.append(luke[:spock])

"""
Global frame
spock   1
yoda    2 changed to 0 changed to -> [->, 2, ->]
                                     luke    [->]
                                             the first item in luke
luke    ->  [->, ->, 2]
            [2]  [1]
"""
