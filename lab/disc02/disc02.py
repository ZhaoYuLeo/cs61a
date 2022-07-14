def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n + 1):
        if cond(i): print(i)


def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def keeper(cond):
        for i in range(1, n + 1):
            if cond(i): print(i)
    return keeper

def lambda_curry2(h):
    """ Returns a Curried version of a two-argument function h.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    return lambda x: lambda y: h(x, y)

def print_delayed(x):
    """Return a new function. This new function, when called, will print out x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed> # a function is returned
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print
