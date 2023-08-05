def counter(d):
    """Takes a non-negative single-digit integer d. It returns a function count
    that takes a non-negative integer n and returns the number of times that d
    appears as a digit in n. You may not use recursive calls or any features of
    Python not yet covered in the course.
    Return a function of N that returns the number of times D appears in N.
    >>> counter(8)(8018)
    2
    >>> counter(0)(2016)
    1
    >>> counter(0)(0)
    0
    """
    def count(n):
        k = 0
        while (n):
            n, digit = n // 10, n % 10
            if (digit == d):
                k += 1
        return k
    return count


def significant(n, k):
    """Takes positive integers n and k. It returns the k most significant digits
    of n as an integer. These are the first k digits of n, starting from the left.
    If n has fewer than k digits, it returns n. You may not use round, int, str,
    or any functions from the math module. You may use pow, which raises its first
    argument to the power of its second: pow(9, 2) is 81 and pow(9, 0.5) is 3.0.

    Return the K most significant digits of N.
    >>> significant(12345, 3)
    123
    >>> significant(12345, 7)
    12345
    """
    if (n < pow(10, k)):
        return n
    return significant(n // 10, k)
