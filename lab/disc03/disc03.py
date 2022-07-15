def multiply(m, n):
    """Return two positive integers' product by adding the integer m nth time.
    >>> multiply(5, 3)
    15
    >>> multiply(1, 19)
    19
    >>> multiply(200, 200)
    40000
    """
    assert m > 0 and n > 0, "Assume arguments are both positive integers"
    def multiply_helper(small, large, result = 0):
        if small == 0:
            return result
        return multiply_helper(small - 1, large, result + large) 
    if m < n:
        return multiply_helper(m, n)
    else:
        return multiply_helper(n, m)
