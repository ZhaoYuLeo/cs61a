from tree import *

def max_tree(t, key):
    """Return the label n of t for which key(n) returns the largest value.
    >>> t = tree(6, [tree(3, [tree(5)]), tree(2), tree(4, [tree(7)])])
    >>> max_tree(t, key=lambda x: x)
    7
    >>> max_tree(t, key=lambda x: -x)
    2
    >>> max_tree(t, key=lambda x: -abs(x - 4))
    4
    """
    if is_leaf(t):
        return label(t)

    largest = label(t)
    for b in branches(t):
        value = max_tree(b, key)
        if (key(value) > key(largest)):
            largest = value

    return largest 
            

def max_tree_one_line(t, key):
    """Return the label n of t for which key(n) returns the largest value.
    one line using a call to the built-int max function
    >>> t = tree(6, [tree(3, [tree(5)]), tree(2), tree(4, [tree(7)])])
    >>> max_tree_one_line(t, key=lambda x: x)
    7
    >>> max_tree_one_line(t, key=lambda x: -x)
    2
    >>> max_tree_one_line(t, key=lambda x: -abs(x - 4))
    4
    """
    return max([label(t)] + [max_tree_one_line(b, key) for b in branches(t)], key=key)
