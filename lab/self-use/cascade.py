def cascade(n):
    """Print a cascade of prefixes of n.
    >>> cascade(12)
    12
    1
    12
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

# It is not a rigid requirement that base cases be expressed before recursive calls. In fact, this function can be expressed more compactly by observing that print(n) is repeated in both clauses of the conditional statement, and therefore can precede it.
def cascade_compactly(n):
    """Print a cascade of prefixes of n.
    >>> cascade(12)
    12
    1
    12
    """
    print(n)
    if n >= 10:
        cascade(n//10)
        print(n)


def inverse_cascade(n):
    """Print a inverse cascade of prefixes of n.
    >>> inverse_cascade(123)
    1
    12
    123
    12
    1
    """
    def helper1(m):
        if m < 10:
            print(m)
        else:
            helper1(m//10)
            print(m)
    def helper2(m):
        if m != n:
            print(m)
        if m > 9:
            helper2(m//10)
    helper1(n)
    helper2(n)


# using higher order function, the progress is much more clear. I think this shows a higher abstraction
def inverse_cascade_higher_order(n):
    """Print a inverse cascade of prefixes of n.
    >>> inverse_cascade_higher_order(123)
    1
    12
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print,  shrink,  n//10)
