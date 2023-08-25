def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def ramp(n):
    """Return whether non-negative integer N has more increases than decreases.
    >>> ramp(123)   # 2 increases (1 -> 2, 2 -> 3) and 0 decreases
    True
    >>> ramp(1315)  # 2 increases (1 -> 3, 1 -> 5) and 1 decreases (3 -> 1)
    True
    >>> ramp(176)   # 1 increases (1 -> 7) and 1 decreases (7 -> 6)
    False
    >>> ramp(5)     # 0 increases and 0 decreases
    False
    """
    n, last, result = n // 10, n % 10, 0
    while (n):
        n, last, result = n // 10, n % 10, result + sign(last - n % 10)
    return result > 0 


def over_under(y):
    """Return a function that takes X and returns:
        -1 if X is less than Y
         0 if X is equal to Y
         1 if X is greater than Y
    >>> over_under(5)(3)    # 3 < 5
    -1
    >>> over_under(5)(5)    # 5 == 5
    0
    >>> over_under(5)(7)    # 7 > 5
    1
    """
    return lambda x: sign(x - y)


def process(n, tally, result):
    """Process all pairs of adjacent digits in N using functions TALLY and RESULT.
    """
    while n >= 10:
        tally, result = tally(n % 100 // 10, n % 10)
        n = n // 10
    return result()


def ups(k):
    """Return tally and result functions that compute whether N has exactly K increases.
    >>> f, g = ups(3)
    >>> process(1200849, f, g)      # Exactly 3 increases: 1 -> 2, 0 -> 8, 4 -> 9
    True
    >>> process(94004, f, g)        # 1 increase: 0 -> 4
    False
    >>> process(122333445, f, g)    # 4 increases: 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5
    False
    >>> process(0, f, g)            # 0 increases
    False
    """

    def f(left, right):
        m = k
        if (left < right):
            m -= 1
        return ups(m)

    return f, lambda : k == 0
        

def ups_solu(k):
    """
    >>> f, g = ups_solu(3)
    >>> process(1200849, f, g)      # Exactly 3 increases: 1 -> 2, 0 -> 8, 4 -> 9
    True
    >>> process(94004, f, g)        # 1 increase: 0 -> 4
    False
    >>> process(122333445, f, g)    # 4 increases: 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5
    False
    >>> process(0, f, g)            # 0 increases
    False
    """
    def f(left, right):
        return ups(min(k, k + sign(left - right)))

    return f, lambda: k == 0


def at_most(n, k):
    """Return whether non-negative integer N has at most K increases.

    >>> at_most(567, 3)
    True
    >>> at_most(567, 2)
    True
    >>> at_most(567, 1)
    False
    """
    result = False
    while k >= 0:
        f, g = ups(k)
        result = result or process(n, f, g)
        k -= 1
    return result
