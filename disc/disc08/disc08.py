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

## 2 Linked Lists

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

def flip_two(lnk):
    """mutates lnk so that every pair is flipped.
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        # you shouldn't return anything
        return 
    lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
    flip_two(lnk.rest.rest)
    
def filter_link(link, f):
    """returns a generator which yields the values of link for
    which f returns True
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    # # iteration
    # while link is not Link.empty:
    #     if f(link.first):
    #         yield link.first
    #     link = link.rest
   
    # recursion
    if link is not Link.empty:
        if f(link.first):
            yield link.first
        yield from filter_link(link.rest, f)


## 3 Trees

def make_even(t):
    """takes in a tree t whose valuse are integers, and mutates the
    tree such that all the odd integers are increased by 1 and all
    the even integers remain the same
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 == 1:
        t.label += 1
    for b in t.branches:
        make_even(b)

def square_tree(t):
    """Mutates a Tree t by squaring all its elements.
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> square_tree(t)
    >>> t.label
    1
    >>> t.branches[0].branches[0].label
    9
    """
    # assume non-empty tree
    t.label *= t.label
    for b in t.branches:
        square_tree(b)

def find_paths(t, entry):
    """returns a list of lists containing the nodes along each path from
    the root of t to entry. Paths may return in any order.
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.label == entry:
        return [[entry]]
    for b in t.branches:
        for path in find_paths(b, entry):
            paths.append([t.label] + path)
    return paths


from operator import mul

def combine_tree(t1, t2, combiner):
    """combines the values of two trees t1 and t2 together with the combiner funtion
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    # assume that t1 and t2 have identical structure
    tree = Tree(combiner(t1.label, t2.label))
    if t1.is_leaf():
        return tree
    zipped = zip(t1.branches, t2.branches)
    tree.branches = [combine_tree(b1, b2, combiner) for b1, b2 in zipped]
    return tree

def alt_tree_map(t, map_fn):
    """ applies map_fn to all of the data at every other level of the tree,
    starting at the root
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    t.label = map_fn(t.label)
    for b in t.branches:
        for sub_b in b.branches:
            alt_tree_map(sub_b, map_fn)
    return t


class Link:
    """To check if a linked list is an empty linked list:
    if link is Link.empty:
        print('This linked list is empty!')
    else:
        print('This linked list is not empty!')
    """

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


class Tree:
    """
    >>> t = Tree(3, [Tree(4), Tree(5)])
    >>> t.label = 5
    >>> t.label
    5
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

