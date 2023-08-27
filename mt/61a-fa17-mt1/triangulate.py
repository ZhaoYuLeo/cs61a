def triangle(a, b, c):
    """Return whether a, b, and c could be the legs of a triangle.
    In any triangle, each side must be shorter than the sum of the other two.

    >>> triangle(3, 4, 5)
    True
    >>> triangle(3, 4, 6)
    True
    >>> triangle(6, 3, 4)
    True
    >>> triangle(3, 6, 4)
    True
    >>> triangle(9, 2, 2)
    False
    >>> triangle(2, 4, 2)
    False
    """
    return (a + b) > c and (b + c) > a and (a + c) > b

def triangle_solu(a, b, c):
    """
    >>> triangle_solu(3, 4, 5)
    True
    >>> triangle_solu(3, 4, 6)
    True
    >>> triangle_solu(6, 3, 4)
    True
    >>> triangle_solu(3, 6, 4)
    True
    >>> triangle_solu(9, 2, 2)
    False
    >>> triangle_solu(2, 4, 2)
    False
    """

    longest = max(a, b, c)

    sum_of_others = a + b + c - longest # or min(a+b, a+c, b+c)

    return longest < sum_of_others
