def jazz(hands):
    print(hands, out)
    if hands < out:
        return hands * 5
    else:
        return jazz(hands // 2) + 1

def twist(shout, it, out=7):
    while shout:
        shout, out = it(shout), print(shout, out)
    return lambda out: print(shout, out)

hands, out = 2, 3
# hands = 2
# (lambda out: jazz(8))(9) would lead to nameerror: 'out' is not defined

"""
>>> pow(2, 3)
8
>>> print(4, 5) + 1
4 5
Error
>>> print(None, print(None))
None
None None
>>> jazz(5)
11
>>> (lambda out: jazz(8))(9) # attention, out is 3. jazz is defined in global frame
12
>>> twist(2, lambda x: x-2)(4)
2 7
0 4
>>> twist(5, print)(out)
5
5 7
None 3
>>> twist(6, lambda hands: hands-out, 2)(-1)
6 2
3 None
0 -1
>>> out = 6
>>> twist(6, lambda hands: hands-out, 2)(-1)
6 2
0 -1
"""
