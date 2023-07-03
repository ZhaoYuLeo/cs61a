# Your project partner has invented an abstract representation of a sequence called a slinky,
# which uses a transition function to compute each element from the previous element.
# A slinky explicitly stores only those elements that cannot be computed by calling transition, 
# using a starts dictionary.
# Each entry in starts is a pair of an index key and an element value.

def length(slinky):
    return slinky[0]
def starts(slinky):
    return slinky[1]
def transition(slinky):
    return slinky[2]


def slinky(elements, transition):
    """Return a slinky containing elements using transition.
    Θ(n), n is the initial length of elements.
    >>> s = slinky(range(3, 10), lambda x: x+1)
    >>> length(s)
    7
    >>> starts(s)
    {0: 3}
    >>> get(s, 2)
    5
    >>> t = slinky([2, 4, 10, 20, 40], lambda x: 2*x)
    >>> starts(t)
    {0: 2, 2: 10}
    >>> get(t, 3)
    20
    >>> slinky([], abs)
    [0, {}, <built-in function abs>]
    >>> slinky([5, 4, 3], abs)
    [3, {0: 5, 1: 4, 2: 3}, <built-in function abs>]
    """
    starts = {}
    for i in range(len(elements)):
        if i == 0 or elements[i] != transition(elements[i - 1]):
            starts[i] = elements[i]
    return [len(elements), starts, transition]


def get(slinky, index):
    """Return the element at index of slinky."""
    start = index
    # find floor 
    while start not in starts(slinky):
        start -= 1
    value = starts(slinky)[start]
    while start != index:
        value = transition(slinky)(value)
        start += 1
    return value
