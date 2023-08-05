def repeat_sum(f, x, n):
    """Compute the following summation of N+1 terms, where the last term
    calls F N times: x + f(x) + f(f(x)) + f(f(f(x))) + ... + f(f(...f(x)))

    >>> repeat_sum(lambda x: x*x, 3, 0) # 3
    3
    >>> repeat_sum(lambda x: x*x, 3, 1) # 3 + 9
    12
    >>> repeat_sum(lambda x: x+2, 3, 4) # 3 + 5 + 7 + 9 + 11
    35
    """
    if (n == 0):
        return x
    return x + repeat_sum(f, f(x), n - 1)

def repeat_sum_solu(f, x, n):
    """
    >>> repeat_sum_solu(lambda x: x*x, 3, 0)
    3
    >>> repeat_sum_solu(lambda x: x*x, 3, 1)
    12
    >>> repeat_sum_solu(lambda x: x+2, 3, 4)
    35
    """
    total, k = 0, 0
    while k <= n:
        total = total + x
        x = f(x)
        k = k + 1
    return total


def sum_squares(n):
    """Takes a non-negative integer n and uses repeat_sum to return the sum of the
    squares of the first n positive integers. U may use pow: pow(9, 2) is 81

    Return the sum of the first N perfect squares.
    >>> sum_squares(0)
    0
    >>> sum_squares(3) # 1**2 + 2**2 + 3**2
    14
    >>> sum_squares(5) # 1**2 + 2**2 + 3**2 + 4**2 + 5**2
    55
    """
    f = lambda x: pow(round(pow(x, 0.5) + 1), 2)
    return repeat_sum(f, 0, n)

def repeat_sum(f, k, n):
    total = k
    while (n > 0):
        k = f(k)
        total += k
        n -= 1
    return total
