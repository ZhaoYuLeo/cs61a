def kbonacci(n, k):
    """
    A k-bonacci sequence starts with K-1 zeros and then a one.
    Each subsequent element is the sum of the previous K elements.
                 n: 0, 1, 2, 3, 4, 5, 6,  7,  8,  9,...

    kbonacci(n, 2): 0, 1, 1, 2, 3, 5, 8, 13, 21, 35, ...
    kbonacci(n, 3): 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, ...
    kbonacci(n, 4): 0, 0, 0, 1, 1, 2, 4,  8, 15, 29, ...
    Takes non-negative integer n and positive integer k and return
    element N of a K-bonacci sequence.

    >>> kbonacci(1, 4)
    0
    >>> kbonacci(3, 4)
    1
    >>> kbonacci(9, 4)
    29
    >>> kbonacci(4, 2)
    3
    >>> kbonacci(8, 2)
    21
    """
    def helper(n, ks):
        if (n < len(ks)):
            return ks[n]
        next = ks[1:]
        next.append(sum(ks))
        return helper(n - 1, next)
    init = [(lambda x: 0 if x < k - 1 else 1)(x) for x in range(k)];
    return helper(n, init)


def kbonacci_direct(n, k):
    """
    >>> kbonacci_direct(1, 4)
    0
    >>> kbonacci_direct(3, 4)
    1
    >>> kbonacci_direct(9, 4)
    29
    >>> kbonacci_direct(4, 2)
    3
    >>> kbonacci_direct(8, 2)
    21
    """
    if n < k - 1:
        return 0
    if n == k - 1:
        return 1
    result = 0;
    for i in range(1, k + 1): 
        result += kbonacci_direct(n - i, k)
    return result

# Assume that all arguments to all of these functions are positive integers
# that do not contain any zero digits.
# For example, 1001 contains zero digits (not allowed), but 1221 does not (allowed).

def combine(left, right):
    """Return all of LEFT's digits followed by all of RIGHT's digits."""
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right

def reverse(n):
    """Return the digits of N in reverse.

    >>> reverse(122543)
    345221
    """
    if n < 10:
        return n
    else:
        return combine(n % 10, reverse(n // 10))

def remove(n, digit):
    """Return a number that consists of all digits of N that are not DIGIT.
    Assume that DIGIT is a positive integer less than 10.
    >>> remove(243132, 3)
    2412
    >>> remove(243132, 2)
    4313
    >>> remove(remove(243132, 1), 2)
    433
    """
    if n == 0:
        return 0
    else:
        if n % 10 == digit:
            return remove(n // 10, digit)
        else:
            return remove(n // 10, digit) * 10 + n % 10

def remove_solu(n, digit):
    """
    >>> remove_solu(243132, 3)
    2412
    >>> remove_solu(243132, 2)
    4313
    >>> remove_solu(remove_solu(243132, 1), 2)
    433
    """
    removed = 0
    while n:
        n, last = n // 10, n % 10
        if last != digit:
            removed = removed * 10 + last
    return reverse(removed)
