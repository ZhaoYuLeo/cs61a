# You may not use pow, **, log, str, or len in your solution.
def sequence(n, term):
    """Takes a positive integer n and a function term.
    Return the first n terms of a sequence as an integer.
    Assume the term function takes a positive integer argument and returns a positive integer.
    >>> sequence(6, abs)                    # Terms are 1, 2, 3, 4, 5, 6
    123456
    >>> sequence(5, lambda k: k+8)          # Terms are 9, 10, 11, 12, 13
    910111213
    >>> sequence(4, lambda k: pow(10, k))   # Terms are 10, 100, 1000, 10000
    10100100010000
    """
    r, k = 0, 1
    while k <= n:
        f = 1
        m = term(k)
        while f <= m:
            f *= 10
        r = r * f + m
        k += 1
    return r
