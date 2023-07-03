def sixty_ones(s):
    """Return the number of times that 6 and 1 appear consecutively

    >>> once = Link(4, Link(6, Link(1, Link(6, Link(0, Link(1))))))
    >>> twice = Link(1, Link(6, Link(1, once)))
    >>> thrice = Link(6, twice)
    >>> apply_to_all(sixty_ones, [Link.empty, once, twice, thrice])
    [0, 1, 2, 3]
    """
    if s is Link.empty or s.rest is Link.empty:
        return 0
    elif s.first == 6 and s.rest.first == 1:
        return 1 + sixty_ones(s.rest.rest)
    else:
        return sixty_ones(s.rest)


def apply_to_all(f, s):
    return [f(x) for x in s]


def no_eleven(n):
    """Return a list of lists of 1's and 6's that do not contain 1 after 1.
    >>> no_eleven(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven(4)[:4] # first half
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven(4)[4:] # second half
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
    """
    if n == 0:
        return [[]]
    else:
        result = []
        for e in no_eleven(n - 1):
            if e and e[-1] == 1:
                e.append(6)
                result.append(e)
            else:
                result.append(e + [6])
                result.append(e + [1])
        return result


def no_eleven_solu(n):
    """Return a list of lists of 1's and 6's that do not contain 1 after 1.
    >>> no_eleven_solu(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven_solu(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven_solu(4)[:4] # first half
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven_solu(4)[4:] # second half
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
    """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6], [1]]
    else:
        a, b = no_eleven_solu(n - 1), no_eleven_solu(n - 2)
        # f(n) = (6)f(n-1) + (1, 6)f(n-1), after 1 is 6
        return [[6] + s for s in a] + [[1, 6] + s for s in b]


class Link:
    """
    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

