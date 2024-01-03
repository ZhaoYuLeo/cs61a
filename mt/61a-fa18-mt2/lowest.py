# Implement lowest, which takes a list of numbers s and returns a list of
# only the elements of s with the smallest absolute value. You may only
# write a single name in each blank.
def lowest(s):
    """Return a list of the elements in s with the smallest absolute value.

    >>> lowest([3, -2, 2, -3, -4, 2, 3, 4])
    [-2, 2, 2]
    >>> lowest(range(-5, 5))
    [0]
    """
    return [e for e in s if abs(e) == min([abs(i) for i in s])]

def lowest_solu(s):
    """Return a list of the elements in s with the smallest absolute value.

    >>> lowest_solu([3, -2, 2, -3, -4, 2, 3, 4])
    [-2, 2, 2]
    >>> lowest_solu(range(-5, 5))
    [0]
    """
    return (lambda y: [x for x in s if abs(x) == y])(abs(min(s, key=abs)))
