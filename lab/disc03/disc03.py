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

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    def hailstone_helper(n, count = 1):
        print(n)
        if n == 1:
            return count
        if n % 2 == 0:
            return hailstone_helper(n // 2, count + 1)
        else:
            return hailstone_helper(3 * n + 1, count + 1)
    return hailstone_helper(n)
    # print(n)
    # if n == 1:
    #     return 1 
    # if n % 2 == 0:
    #     return 1 + hailstone(n // 2)
    # else:
    #     return 1 + hailstone(3 * n + 1)
