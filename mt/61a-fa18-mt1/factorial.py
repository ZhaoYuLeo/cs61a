def factorial(n):
    """The factorial of positive n: n * (n-1) * (n-2) * ... * 1
    >>> factorial(4)   # 4 * 3 * 2 * 1
    24
    >>> factorial(1)
    1
    """
    # You may use any of functions defined above.
    # You may not write if, else, and, or, or lambda in your solution.
    return n * fif(identity, factorial, increment, n - 1) 

def fif(c, t, f, x):
    if c(x):
        return t(x)
    else:
        return f(x)

identity = lambda x: x
increment = lambda x: x + 1
