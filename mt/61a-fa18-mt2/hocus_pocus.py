def put(hocus, pocus):
    hocus = 2
    you = pocus[hocus]
    def pocus():
        nonlocal hocus
        if type(spell.pop()) == list:
            you.append(hocus)
            return [pocus(), hocus]
        else:
            hocus = 3
            return spell[0:1]
    return pocus
spell = [6, 5, [4]]
you = spell
put(spell, you)()

"""
Global Frame
        put     →   func put(hocus, pocus) [parent=Global]
        spell   →   [6, 5, ↓] changed to [6, 5] in f2 changed to [6] in f3
                          [4] changed to [4, 2] in f2
        you     →   ↑ (points to spell)

f1 put [parent=Global]
        hocus   →   ↑ changed to 2 in f1 changed to 3 in f3
        pocus   →   ↑ changed to func pocus() [parent=f1] in f1
        you     →          ↑ (points to list [4, 2] in line 21
        Return Value    points to func pocus() [parent=f1]

f2 pocus [parent=f1]
                           
        Return Value    [↓, 2]    # Error! [↓, 3] nonlocal hocus, hocus has been changed to 3 when f2 returns

f3 pocus [parent=f1]
        Return Value    [6]
"""

"""
I guess this is not a good practice. We cannot rely on the order in which the expressions are evaluated.
>>> def put():
...     hocus = 2
...     def pocus():
...         nonlocal hocus
...         return [set(), hocus]
...     def set():
...         nonlocal hocus
...         hocus = 3
...     return pocus
...
>>> put()()
[None, 3]
>>> def put():
...     hocus = 2
...     def pocus():
...        nonlocal hocus
...        return [hocus, set()]
...     def set():
...        nonlocal hocus
...        hocus = 3
...     return pocus
... 
>>> put()()
[2, None]
"""
