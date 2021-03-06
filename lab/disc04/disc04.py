def count_stair_ways(n):
    """Return the number of ways you can go up the flight of stairs which has n steps by taking 1 or 2 steps each time
    Assume n is positive
    >>> count_stair_ways(3)
    3 
    """
    assert n > 0 and isinstance(n, int), "Steps of the flight of stairs are larger than zero"
    def helper(steps):
        if steps < 0:
            return 0
        if steps == 0:
            return 1
        return helper(steps - 1) + helper(steps - 2)
    return helper(n)


# another description of count_partitions ? no, full permutation 
def count_k(n, k):
    """Return the number of paths
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4) # 4, 3 + 1, 1 + 3, 2 + 1 + 1, 1 + 2 + 1, 1 + 1 + 2, 1 + 1 + 1 + 1
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    total = 0
    # huge
    for i in range(1, k + 1):
        total += count_k(n - i, k)
    return total


def even_weighted(s):
    """Takes a list s and returns a new list that keeps only the even-indexed elements of s and multiplies them by their corresponding index.
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [index * number for index, number in enumerate(s) if index % 2 == 0]


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive elements of s.
    
    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
