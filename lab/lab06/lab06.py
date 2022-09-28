this_file = __file__


def make_adder_inc(a):
    """Takes in an integer a and returns a one-argument function. This function should take in some value b and reuturn a + b the first time it is called, similar to make_adder. The second time it is called, however, it should return a + b + 1, then a + b + 2 the third time, and so on. 
    Stream, isn't
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    c = -1 
    def adder_inc(b):
        nonlocal c
        c += 1
        return a + b + c 
    return adder_inc

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    pre1, pre2 = 0, 1
    def fib():
        nonlocal pre1, pre2
        cur = pre1
        pre1 = pre2
        pre2 = cur + pre2 
        return cur 
    return fib

def make_fib_2():
    def helper(pre1, pre2):
        print(pre1)
        def fib():
            return helper(pre2, pre1 + pre2)
        return fib
    return helper(0, 1)

def insert_items(lst, entry, elem):
    """Takes in a list lst, an argument entry, and another argument elem. This function will check through each item present in lst to see if it is equivalent with entry. Upon finding an equivalent entry, the function should modify the list by placing elem into the list right after the found entry. At the end of the function, the modified list should be returned. Use list mutation to modify the original list, no new lists should be created or returned.
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    index_to_insert = [i for i,x in enumerate(lst) if x == entry]
    for i, index in enumerate(index_to_insert):
        lst.insert(i + index + 1, elem)
    return lst
    # skip = False
    # for i, x in enumerate(lst):
    #     if skip:
    #         skip = False
    #         continue
    #     if x == entry:
    #         # infinite loop when entry and elem are equal
    #         lst.insert(i + 1, elem) # !!modified the object being iterated
    #         if entry == elem:
    #             skip = True
    # return lst
