from tree import *

def print_all_paths(t):
    """Print all the paths from the root to a leaf.
    >>> t = tree(1, [tree(2, [tree(3)]), tree(4)])
    >>> print_all_paths(t)
    [1, 2, 3]
    [1, 4]
    """
    for path in all_paths(t):
        print(path)
        
        
def all_paths(t):
    if is_leaf(t):
        yield t
    else:
        for b in branches(t):
            for path in all_paths(b):
                print("path is: " + str(path))
                yield [label(t)] + path

def all_paths_1(t):
    if is_leaf(t):
        return [t] # [label(t)]
    else:
        paths = []
        for b in branches(t):
            for path in all_paths_1(b):
                new_path = [label(t)] + path
                paths.append(new_path)
        return paths

