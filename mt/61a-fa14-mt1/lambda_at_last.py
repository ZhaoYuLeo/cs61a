# line evaluates to 2014. You may only use the names two_thousand, two, k, four,
# and teen and parentheses in your expression (no numbers, operators, etc.).

two_thousand = lambda two : lambda k: k(two)(two)
two_thousand(7)(lambda four: lambda teen: 2000 + four + teen)



# You may only use the names if_fn, condition, a, b, n, factorial, base, and
# recursive and parentheses in your expression (no numbers, operators, etc.).

def if_fn(condition):
    if condition:
        return lambda a, b: a
    else:
        return lambda a, b: b

def factorial(n):
    """Compute n! = 1 * 2 * 3 * ... * n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    def base():
        return 1
    def recursive():
        return n * factorial(n - 1)
    return if_fn(n)(recursive, base)()
