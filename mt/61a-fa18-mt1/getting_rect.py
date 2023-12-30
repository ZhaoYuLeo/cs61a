# Hint: The built-in function round takes a number as its argument and returns the nearest integer.
# For example, round(2.0) evaluateds to 2, and round(2.5) evaluates 3.
def rect(area, perimeter):
    """Return the longest side of a rectangle with AREA and PERIMETER that has integer sides.
    >>> rect(10, 14)  # A 2 x 5 rectangle
    5
    >>> rect(5, 12)   # A 1 x t rectangle
    5
    >>> rect(25, 20)  # A 5 x 5 rectangle
    5
    >>> rect(25, 25)  # A 2.5 x 10 rectangle doesn't count because sides are not integers
    False
    >>> rect(25, 29)  # A 2 x 12.5 rectangle doesn't count because sides are not integers
    False
    >>> rect(100, 50) # A 5 x 20 rectangle
    20
    >>> rect(5, 11)
    False
    >>> rect(4, 11)
    False
    """
    h = 1
    while 2 * h <= perimeter:
        w = round((perimeter - 2 * h) / 2)
        if area == h * w and perimeter == 2 * (h + w):
            return w
        h += 1
    return False 



def rect_solu(area, perimeter):
    """Return the longest side of a rectangle with AREA and PERIMETER that has integer sides.
    >>> rect_solu(10, 14)  # A 2 x 5 rectangle
    5
    >>> rect_solu(5, 12)   # A 1 x t rectangle
    5
    >>> rect_solu(25, 20)  # A 5 x 5 rectangle
    5
    >>> rect_solu(25, 25)  # A 2.5 x 10 rectangle doesn't count because sides are not integers
    False
    >>> rect_solu(25, 29)  # A 2 x 12.5 rectangle doesn't count because sides are not integers
    False
    >>> rect_solu(100, 50) # A 5 x 20 rectangle
    20
    >>> rect_solu(5, 11)
    False
    >>> rect_solu(4, 11)
    False
    """
    side = 1
    while side * side <= area:
        other = round(perimeter / 2 - side)
        if side * other == area and 2 * (side + other) == perimeter:
            return other
        side = side + 1
    return False 

