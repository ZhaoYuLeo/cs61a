def decompose1(f, h):
    """Return g such that h(x) equals f(g(x)) for any non-negative integer x.
    >>> add_one = lambda x: x + 1
    >>> square_then_add_one = lambda x: x * x + 1
    >>> g = decompose1(add_one, square_then_add_one)
    >>> g(5)
    25
    >>> g(10)
    100
    """
    def g(x):
        #return f(g(x+1)) - h(x+1) + h(x)
        def r(y):
            if f(y) == h(x):
                return y
            else:
                return r(y + 1)
        return r(0)
    return g

def compose1(f, g):
    return lambda x: f(g(x))

def make_adder(a):
    def adder(b):
        return a + b
    return adder

e, square = make_adder(1), lambda x: x*x
decompose1(e, compose1(square, e))(3) + 2000

