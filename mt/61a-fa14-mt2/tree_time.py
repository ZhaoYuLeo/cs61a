# A GrootTree g is a binary tree that has an attribute parent.
# Its parent is the GrootTree in which g is a branch.
# If a GrootTree instance is not a branch of any other GrootTree instance,
# then its parent is BinaryTree.empty.
# BinaryTree.empty should not have a parent attribute.
# Assume that every GrootTree instance is a branch of at most one other
# GrootTree instance and not a branch of any other kind of tree.

    
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

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


class BinaryTree(Tree):
    empty = Tree(None)
    empty.is_empty = True

    def __init__(self, root, left=empty, right=empty):
        Tree.__init__(self, root, [left, right])

    @property
    def entry(self):
        return self.label

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]


class GrootTree(BinaryTree):
    """A binary tree with a parent."""
    def __init__(self, entry, left=BinaryTree.empty, right=BinaryTree.empty):
        BinaryTree.__init__(self, entry, left, right)
        self.parent = BinaryTree.empty
        for b in [left, right]:
            if b is not BinaryTree.empty:
                b.parent = self


def fib_groot(n):
    """Return a Fibonacci GrootTree.
              3
        1           2
    0        1   1       1
                     0      1
    >>> t = fib_groot(3)
    >>> t.entry
    2
    >>> t.parent.is_empty
    True
    >>> t.left.parent.entry
    2
    >>> t.right.left.parent.entry
    1
    >>> t.right.left.parent.right.parent.entry
    1
    """
    if n == 0 or n == 1:
        return GrootTree(n)
    else:
        left, right = fib_groot(n - 2), fib_groot(n - 1)
        return GrootTree(left.entry + right.entry, left, right)

def paths(g, s):
    """The number of paths through g with entries s.
    Assume that the GrootTree class is implemented correctly and that
    the list s is non-empty.
    >>> t = fib_groot(3)
    >>> paths(t, [1])
    0
    >>> paths(t, [2])
    1
    >>> paths(t, [2, 1, 2, 1, 0])
    2
    >>> paths(t, [2, 1, 0, 1, 0])
    1
    >>> paths(t, [2, 1, 2, 1, 2, 1])
    8
    """
    # assume the list s is non-empty
    if g is BinaryTree.empty or g.entry != s[0]:
        return 0
    elif len(s) == 1 and g.entry == s[0]:
        return 1
    else:
        return paths(g.left, s[1:]) + paths(g.right, s[1:]) + paths(g.parent, s[1:])

def paths_solu(g, s):
    """
    >>> t = fib_groot(3)
    >>> paths_solu(t, [1])
    0
    >>> paths_solu(t, [2])
    1
    >>> paths_solu(t, [2, 1, 2, 1, 0])
    2
    >>> paths_solu(t, [2, 1, 0, 1, 0])
    1
    >>> paths_solu(t, [2, 1, 2, 1, 2, 1])
    8
    """
    if g is BinaryTree.empty or s == [] or g.entry != s[0]:
        return 0
    elif len(s) == 1 and g.entry == s[0]:
        return 1
    else:
        extensions = [g.left, g.right, g.parent]
        return sum(paths(x, s[1:]) for x in extensions)
