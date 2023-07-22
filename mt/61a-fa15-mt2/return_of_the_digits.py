from tree import *

def complete(t, d, k):
    """Return whether t is d-k-complete.
    A tree is d-k-complete if every node at a depth less than d has exactly k branches and every node at depth d is a leaf.
    Notes:
    The depth of a node is the number of steps from the root; the root node has depth 0.
    The built-in all function takes a sequence and returns whether all elements are true values: all([1, 2]) is True but all([0, 1]) is False.
    >>> complete(tree(1), 0, 5)
    True
    >>> u = tree(1, [tree(1), tree(1), tree(1)])
    >>> [ complete(u, 1, 3)  ,  complete(u, 1, 2)  ,  complete(u, 2, 3) ]
    [True, False, False]
    >>> complete(tree(1, [u, u, u]), 2, 3)
    True
    """
    if is_leaf(t):
        return d == 0
    else:
        if len(branches(t)) != k:
            return False
        return  all([complete(b, d - 1, k) for b in branches(t)])


def complete_solu(t, d, k):
    """
    >>> complete_solu(tree(1), 0, 5)
    True
    >>> u = tree(1, [tree(1), tree(1), tree(1)])
    >>> [ complete_solu(u, 1, 3)  ,  complete_solu(u, 1, 2)  ,  complete_solu(u, 2, 3) ]
    [True, False, False]
    >>> complete_solu(tree(1, [u, u, u]), 2, 3)
    True
    """
    if is_leaf(t):
        return d == 0
    bs = [complete_solu(b, d - 1, k) for b in branches(t)]
    # clear logic
    return len(branches(t)) == k and all(bs)


def adder(x, y):
    """
    Takes two lists x and y of digits representing positive numbers. It mutates
    x to represent the result of adding x and y.
    Notes: The built-in reversed function takes a sequence and return its element in reverse order.
    Assume that x[0] and y[0] are both positive.
    Adds y into x for lists of digits x and y representing positive numbers.
    >>> a = [3, 4, 5]
    >>> adder(a, [5, 5])            # 345 + 55  = 400
    [4, 0, 0]
    >>> adder(a, [8, 3, 4])         # 400 + 834 = 1234
    [1, 2, 3, 4]
    >>> adder(a, [3, 3, 3, 3, 3])   # 1234 + 33333 = 34567
    [3, 4, 5, 6, 7]
    >>> b = [9, 9, 9, 4, 5]
    >>> adder(b, [5, 5])
    [1, 0, 0, 0, 0, 0]
    >>> c = [9, 4, 5]
    >>> adder(c, [5, 5])
    [1, 0, 0, 0]
    >>> d = [5, 5]
    >>> adder(d, [9, 9, 9, 4, 5])
    [1, 0, 0, 0, 0, 0]
    """
    if len(x) < len(y):
        x, y = y, x
    i, carry = len(x) - 1, 0
    for b in reversed(y):
        b = x[i] + b + carry
        x[i], carry = b % 10, b // 10
        i -= 1
    while carry and i > -1:
        b = x[i] + carry
        x[i], carry = b % 10, b // 10
        i -= 1
    if carry:
        x.insert(0, carry)
    return x


def adder_solu(x, y):
    """
    >>> a = [3, 4, 5]
    >>> adder_solu(a, [5, 5])            # 345 + 55  = 400
    [4, 0, 0]
    >>> adder_solu(a, [8, 3, 4])         # 400 + 834 = 1234
    [1, 2, 3, 4]
    >>> adder_solu(a, [3, 3, 3, 3, 3])   # 1234 + 33333 = 34567
    [3, 4, 5, 6, 7]
    >>> b = [9, 9, 9, 4, 5]
    >>> adder_solu(b, [5, 5])
    [1, 0, 0, 0, 0, 0]
    >>> c = [9, 4, 5]
    >>> adder_solu(c, [5, 5])
    [1, 0, 0, 0]
    >>> d = [5, 5]
    >>> adder_solu(d, [9, 9, 9, 4, 5])
    [1, 0, 0, 0, 0, 0]
    """
    #TODO: fix it 
    carry, i = 0, len(x) - 1
    for d in reversed([0] + y):
        if i == -1:
            x.insert(0, 0)
            i = 0
        d = carry + x[i] + d
        carry = d // 10
        x[0 if len(x) - i == len(y) + 1 and d >= 10 else i:i + 1] = adder_solu(x[0:i + 1], [0] * i)
        i -= 1 
        if x[0] == 0:
            x.remove(0)
        return x


def multiples(k, s):
    """Takes a positive integer k and a linked list s of digits greater than 0 and less than 10.
    It returns a linked list of all positive n that are multiples of k greater than k and made up
    of digits only from s. The digits in each n must appear in the same order as they do in s,
    and each digit from s can appear only once in each n.
    Return a linked list of all multiples of k selected from digits in s.
    2^n
    >>> odds = Link(1, Link(3, Link(5, Link(7, Link(9))))) # 63
    >>> multiples(5, odds)
    Link(135, Link(15, Link(35)))
    >>> multiples(7, odds)
    Link(1379, Link(357, Link(35)))
    >>> multiples(9, odds)
    Link(1359, Link(135))
    >>> multiples(2, odds)
    ()
    """
    t = Link.empty
    def helper(n, s):
        nonlocal t
        if s is Link.empty:
            if n > k and n % k == 0:
                t = Link(n, t)
        else:
            mult = s.first + 10 * n
            helper(n, s.rest)
            helper(mult, s.rest)
    helper(0, s)
    return t


def multiples1(k, s):
    """
    >>> odds = Link(1, Link(3, Link(5, Link(7, Link(9)))))
    >>> multiples1(5, odds)
    Link(135, Link(15, Link(35)))
    >>> multiples1(7, odds)
    Link(1379, Link(357, Link(35)))
    >>> multiples1(9, odds)
    Link(1359, Link(135))
    >>> multiples1(2, odds)
    ()
    """
    def helper(n, s):
        if s is Link.empty:
            if n > k and n % k == 0:
                return Link(n, s)
            else:
                return s
        else:
            mult = s.first + 10 * n
            without_cur = helper(n, s.rest)
            with_cur = helper(mult, s.rest)
            return extend_link(with_cur, without_cur) # expensive
    return helper(0, s)


def partition(n, m):
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partition(n-m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partition(n, m-1)
        return with_m + without_m


def count(f):
    def counted(n, s):
        counted.call_count += 1
        return f(n, s)
    counted.call_count = 0
    return counted


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


def bits(nums):
    """ Encodes a list of nums using sequences of 0's and 1's that tell you
    whether each power of 2 is used, starting with pow(2, 0)
    A set of nums represented as a function that takes 'entry', 0, or 1.
    >>> t = bits([4, 5]) # Contains 4 and 5, but not 2
    >>> t(0)(0)(1)('entry') # 4 = 0 * pow(2, 0) + 0 * pow(2, 1) + 1 * pow(2, 2)
    True
    >>> t(0)(1)('entry')    # 2 = 0 * pow(2, 0) + 1 * pow(2, 1)
    False
    >>> t(1)(0)(1)('entry') # 5 = 1 * pow(2, 0) + 0 * pow(2, 1) + 1 * pow(2, 2)
    True
    """
    def branch(last):
        if last == 'entry':
            return 0 in nums
        return bits([k // 2 for k in nums if k % 2 == last])
    return branch


def int_set(contents):
    """Higher-order function that takes a list of non-negative integers called
    contents and returns a function that takes a non-negative integer n and returns
    whether n appears in contents. Clue: Every integer can be expressed uniquely
    as a sum of powers of 2.

    Return a function that represents a set of non-negative integers.
    >>> int_set([1, 2])(1) ,  int_set([1, 2])(3)  # 1 in [1, 2] but 3 is not
    (True, False)
    >>> s = int_set([1, 3, 4, 7, 9])
    >>> [s(k) for k in range(10)]
    [False, True, False, True, True, False, False, True, False, True]
    """
    t = bits(contents)
    def in_contents(n):
        nonlocal t
        if n == 0:
            r = t('entry')
            # the return type of bits is not always the same, iteration may be better. You should clear the status before loop
            t = bits(contents)
            return r
        t = t(n % 2)
        return in_contents(n // 2)
    return in_contents


def int_set_solu(contents):
    """
    >>> int_set_solu([1, 2])(1) ,  int_set_solu([1, 2])(3)  # 1 in [1, 2] but 3 is not
    (True, False)
    >>> s = int_set_solu([1, 3, 4, 7, 9])
    >>> [s(k) for k in range(10)]
    [False, True, False, True, True, False, False, True, False, True]
    """
    index = bits(contents)
    def contents(n):
        t = index
        while n:
            last, n = n % 2, n // 2
            t = t(last)
        return t('entry')
    return contents


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

