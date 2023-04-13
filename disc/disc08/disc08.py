# Linked Lists, Trees, Representation

## 1 Representation - A Note on Str and Repr

""""
>>> A("one")
one
>>> print(A("one"))
oneone
>>> str(A("two"))
'twotwo'
>>> repr(A("two"))
'two'
>>> print(repr(A("two")))
two
>>> b = B()
boo!
>>> b.add_a(A("a"))
>>> b.add_a(A("b"))
>>> b
2
aabb
"""

class A():
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return self.x
    def __str__(self):
        return self.x * 2

class B():
    def __init__(self):
        print("boo!")
        self.a = []
    def add_a(self, a):
        self.a.append(a)
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret

## Linked Lists

def sum_nums(lnk):
    """takes in a a linked list and returns the sum of all its elements
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    # assume all elements in lnk are integers
    if lnk is Link.empty:
        return 0
    return lnk.first + sum_nums(lnk.rest)

def multiply_lnks(lst_of_lnks):
    """takes in a list of linked lists and multiplies elements in the 
    same depth. Returns the new linked list whose length is that of
    the shortest linked list given.
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # assume the Link objects are shallow linked lists and
    # that lst_of_lnks contains at least one linked list.
    first, rest_lnks = 1, []
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return lnk
        first *= lnk.first
        rest_lnks.append(lnk.rest)
    return Link(first, multiply_lnks(rest_lnks))

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
