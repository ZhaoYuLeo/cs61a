from tree import *

def full(t):
    """Returns whether all the branches of s have the same number of leaves
    for every subtree s of it. If r and s are two different subtrees of t,
    then a branch of r can have a different number of leaves than a branch
    in s, but all branches of r must have the same number of leaves.
    Whether every subtree in t has the same number of leaves in each branch.
    >>> full(tree(1))
    True
    >>> t = tree(1, [tree(1), tree(1)])
    >>> full(t)
    True
    >>> full(tree(1, [t, t]))
    True
    >>> not_full = tree(1, [tree(1, [tree(1)]), t])
    >>> full(not_full)
    False
    >>> full(tree(1, [not_full, not_full]))
    False
    """
    is_first = True
    for b in branches(t):
        if not full(b):
            return False
        if is_first:
            is_first = False
            # k = len(leaves(branches(t)[0]))
            k = len(leaves(b))
        elif len(leaves(b)) != k:
            return False
    return True

def leaves(t):
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(t)], [])


def adder(x, y):
    """Adds y into x for lists of digits x and y representing positive numbers.
    >>> a = [3, 4, 5]
    >>> adder(a, [5, 5])           #  345 +    55 =   400
    [4, 0, 0]
    >>> adder(a, [8, 3, 4])        #  400 +   834 =  1234
    [1, 2, 3, 4]
    >>> adder(a, [3, 3, 3, 3, 3])  # 1234 + 33333 = 34567
    [3, 4, 5, 6, 7]
    """
    carry, i = 0, len(x) - 1
    for d in reversed([0] + y):
        if i == -1:
            x.insert(0, 0)
            i = 0
        d = carry + x[i] + d
        carry = d // 10
        x[i] = d % 10
        i -= 1;
    if x[0] == 0:
        x.remove(0)
    return x


def pizza(k, n):
    """ Takes non-negative integers k and n. It returns a linked list of all ways
    of dividing k pieces of pizza, among n people. Each element of the returned
    linked list should be a Python list of integers of length n in which each element
    is the number of slices for a person. Nobody eats only one slice!
    Return a linked list of all ways of splitting k slices among n people.
    >>> _ = map_link(print, pizza(8, 3))
    [2, 2, 4]
    [2, 3, 3]
    [2, 4, 2]
    [3, 2, 3]
    [3, 3, 2]
    [4, 2, 2]
    """
    extra = k - 2 * n
    if extra < 0:
        return Link.empty

    def add_to(e, times):
        if times == 1:
            return Link([e])
        result = Link.empty
        for n in range(e + 1):
            l = map_link(lambda x: [n] + x, add_to(e - n, times - 1))
            result = extend_link(l, result) 
        return result

    return map_link(lambda x: [i + 2 for i in x], add_to(extra, n))


def pizza_solu(k, n):
    """Θ(n^2)
    >>> _ = map_link(print, pizza_solu(8, 3))
    [2, 2, 4]
    [2, 3, 3]
    [2, 4, 2]
    [3, 2, 3]
    [3, 3, 2]
    [4, 2, 2]
    """
    assert k >= 0 and n >= 0
    if n == 0 and k == 0:
        return Link([])
    elif n == 0:
        return Link.empty
    else:
        splits = Link.empty
        for s in range(2, k + 1):
            f = lambda p: [s] + p    
            r = pizza_solu(k - s, n - 1)
            splits = extend_link(splits, map_link(f, r))         
        return splits
                                     
                                     
def extend_link(s, t):               
    if s is Link.empty:              
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))

def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def digits(nums):
    """A set of nums represented as a function that takes 'entry' or a digit.
    >>> t = digits([302, 35])   # Contains 302 and 35 but not 7
    >>> t(2)(0)(3)('entry')     # 102 = 2 * 1 + 0 * 10 + 3 * 100
    True
    >>> t(5)(3)('entry')        # 35 = 5 * 1 + 3 * 10
    True
    >>> t(7)('entry')           #
    False
    """
    def branch(last):
        if last == 'entry':
            return 0 in nums
        return digits([k // 10 for k in nums if k % 10 == last])
    return branch


def int_set(contents):
    """Return a function that represents a set of non-negative integers

    >>> int_set([1, 2])(1) ,  int_set([1, 2])(3)  # 1 in [1, 2] but 3 is not
    (True, False)
    >>> s = int_set([101, 103, 104, 107, 109])
    >>> [s(k) for k in range(100, 110)]
    [False, True, False, True, True, False, False, True, False, True]
    """
    g = digits(contents)
    def contains(n):
        t = g
        while n:
            last, n = n % 10, n // 10
            t = t(last)
        return t('entry')
    return contains


class Link:
    """A linked list.

    >>> s = Link(3, Link(4, Link(5)))
    >>> s
    Link(3, Link(4, Link(5)))
    >>> print(s)
    <3 4 5>
    >>> s.first
    3
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.first
    4
    >>> s.rest.first = 7
    >>> s
    Link(3, Link(7, Link(5)))
    >>> s.first = 6
    >>> s.rest.rest = Link.empty
    >>> s
    Link(6, Link(7))
    >>> print(s.rest)
    <7>
    >>> t = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> t
    Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print(t)
    <1 <2 3> 4>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
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


