# You may not use a list, set, or any other data type not covered yet in the course.
def repeat(k):
    """when called repeatedly, print each repeated argument.
    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda i: i == k)

def repeat_solu(k):
    """when called repeatedly, print each repeated argument.
    >>> f = repeat_solu(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda n: False)(k)

def detector(f):
    def g(i):
        if f(i):
            print(i)
        return detector(lambda n: n == i or f(n))
    return g

def repeat_digits(n):
    """Print the repeated digits of non-negative integer n.
    >>> repeat_digits(581002821)
    2
    0
    1
    8
    """
    f = repeat
    while n:
        f, n = f(n % 10), n // 10
