def partitions(n, m):
    """Yield all partitions of N using parts up to size M.
    >>> list(partitions(1, 1))
    ['1']
    >>> list(partitions(2, 2))
    ['2', '1 + 1']
    >>> list(partitions(4, 2))
    ['2 + 2', '2 + 1 + 1', '1 + 1 + 1 + 1']
    >>> for p in partitions(6, 4):
    ...     print(p)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    # if m <= 0 or n <= 0:
    #    return
    if m > 0 and n > 0:
    
        if n == m:
            yield str(n) 
        
        with_m = partitions(n - m, m)
        yield from [str(m) + ' + ' + i for i in with_m]
        
        yield from partitions(n, m - 1)


def partitions_solu(n, m):
    """
    >>> list(partitions_solu(1, 1))
    ['1']
    >>> list(partitions_solu(2, 2))
    ['2', '1 + 1']
    >>> list(partitions_solu(4, 2))
    ['2 + 2', '2 + 1 + 1', '1 + 1 + 1 + 1']
    >>> for p in partitions_solu(6, 4):
    ...     print(p)
    4 + 2
    4 + 1 + 1
    3 + 3
    3 + 2 + 1
    3 + 1 + 1 + 1
    2 + 2 + 2
    2 + 2 + 1 + 1
    2 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n == m:
        yield str(m)

    if n > 0 and m > 0:
        for p in partitions(n - m, m):
            yield str(m) + ' + ' + p
        yield from partitions(n, m - 1)


