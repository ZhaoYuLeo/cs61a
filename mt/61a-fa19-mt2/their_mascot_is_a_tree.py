from link import *
from tree import *

def layer(t, d):
    """Return a linked list containing all labels of Tree T at depth D.
    >>> a_tree = tree(1, [tree('b', [tree('mas')]),
    ...                   tree('a', [tree('co')]),
    ...                   tree('d', [tree('t', [tree('!')])])])
    >>> print(layer(a_tree, 0))
    <1>
    >>> print(layer(a_tree, 1))
    <b a d>
    >>> print(layer(a_tree, 2))
    <mas co t>
    >>> print(layer(a_tree, 3))
    <!>
    """
    # not use lambda, if ,and, or or in the solution
    def helper(t, d, lnk):
        if d == 0:
            return Link(label(t), lnk)
        else:
            for b in reversed(branches(t)):
                lnk = helper(b, d - 1, lnk)
            return lnk
    
    return helper(t, d, Link.empty)

    # def helper(t, d):
    #     if d == 0:
    #         return Link(label(t))
    #     else:
    #         lnk = Link.empty
    #         for b in reversed(branches(t)):
    #             l = helper(b, d - 1)
    #             if l is not Link.empty:
    #                 lnk = Link(l.first, lnk)
    #         return lnk

    # return helper(t, d)
