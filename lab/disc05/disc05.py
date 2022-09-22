def height(t):
    """Return the height of a tree which is the length of the longest path from the root to a leaf.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0

    return 1 + max([height(branch) for branch in branches(t)])

def max_path_sum(t):
    """Return the maximum path sum of the tree which is the maximum sum of the values along any path in the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)

    return label(t) + max(max_path_sum(branch) for branch in branches(t)) 

def square_tree(t):
    """Return a tree with the square of every element in t. Assume that every item is a number.
    >>> numbers = tree(1,
    >>> print_tree(square_tree(numbers))
    """
    return tree(label(t)**2, [square_tree(b) for b in branches(t)])

def find_path(tree, x):
    """Return a list containing the nodes along the path required to get from the root of the tree to a node containing x. If x is not present in the tree, return None. Assume that the entries of the tree are unique.
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    def helper(tree):
        if label(tree) == x:
            return [label(tree)]

        for b in branches(tree):
            path = helper(b)
            if path:
                # I hope I could add label(tree) to the front, but it's too expensive for a list
                # and I don't want to create a list for each branch.
                path.append(label(tree))
                return path 

        return None

    result = helper(tree)
    if result:
        result.reverse()
    return result


# Tree ADT

def tree(label, branches=[]):
     for branch in branches:
         assert is_tree(branch), 'branches must be trees'
     return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
        

def copy_tree(t):
    return tree(label(t), [copy_tree(b) for b in branches(t)])
