def stable(s, k, n):
    """Return whether all pairs of elements of S within distance at most K differ by at
    most N.
    >>> stable([1, 2, 3, 5, 6], 1, 2)  # All adjacent values differ by at most 2.
    True
    >>> stable([1, 2, 3, 5, 6], 2, 2)  # abs(5-2) is a difference of 3.
    False
    >>> stable([1, 5, 1, 5, 1], 2, 2)  # abs(5-1) is a difference of 4.
    False
    """
#    for d in range(k):
#        for i in range(d, len(s), k):
#            if (abs(s[i] - s[i - d]) > n):
#                return False
#    return True

#    for i in range(k, len(s)):
#        for d in range(i - k, i):
    for i in range(len(s)):
        for d in range(max(0, i - k), i):
            if (abs(s[d] - s[i]) > n):
                return False
    return True


def stable_solu(s, k, n):
    """
    >>> stable_solu([1, 2, 3, 5, 6], 1, 2)
    True
    >>> stable_solu([1, 2, 3, 5, 6], 2, 2)
    False
    >>> stable_solu([1, 5, 1, 5, 1], 2, 2)
    False
    """
    for i in range(len(s)):
        near = range(max(0, i - k), i)
        if any([abs(s[i] - s[j]) > n for j in near]):
            return False
    return True
