def switch(s, t, k):
    """Return the list with the largest sum built by switching between S and T at most K times.
    >>> switch([1, 2, 7], [3, 4, 5], 0)
    [1, 2, 7]
    >>> switch([1, 2, 7], [3, 4, 5], 1)
    [3, 4, 5]
    >>> switch([1, 2, 7], [3, 4, 5], 2)
    [3, 4, 7]
    >>> switch([1, 2, 7], [3, 4, 5], 3)
    [3, 4, 7]
    """
    if k == 0 or len(s) == 0:
        return s 
    else:
        a = switch(t, s, k - 1)
        b = s[:1] + switch(s[1:], t[1:], k)
        return max(a, b, key=sum)

