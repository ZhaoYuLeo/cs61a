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
    assert isinstance(n, int) and n > 0, "Argument of hailstone must be positive integer."
    def hailstone_helper(n, count = 1):
        print(n)
        if n == 1:
            return count
        if n % 2 == 0:
            return hailstone_helper(n // 2, count + 1)
        else:
            return hailstone_helper(3 * n + 1, count + 1)
    return hailstone_helper(n)
    # # non tail recursive version
    # print(n)
    # if n == 1:
    #     return 1 
    # if n % 2 == 0:
    #     return 1 + hailstone(n // 2)
    # else:
    #     return 1 + hailstone(3 * n + 1)



def merge(n1, n2):
    """ Merges two numbers with digits in decreasing order and returns a single number with all of the digits of the two, in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    assert n1 >= 0 and n2 >= 0, "Assume two arguments are both positive"
    assert isinstance(n1, int) and isinstance(n2, int), "Assume two arguments are both integers"
    def merge_helper(n1, n2, result = 0, digit = 0):
        if n1 == 0 and n2 == 0:
            return result
        if n1 == 0:
            return n2 * 10 ** digit + result
        if n2 == 0:
            return n1 * 10 ** digit + result
        rem1, rem2 = n1 % 10, n2 % 10
        if rem1 < rem2:
            return merge_helper(n1 // 10, n2, rem1 * 10 ** digit + result, digit + 1)
        else:
            return merge_helper(n1, n2 // 10, rem2 * 10 ** digit + result, digit + 1)
    return merge_helper(n1, n2)
   # # non tail recursive version
    # if n1 == 0 and n2 == 0:
    #     return 0
    # if n1 == 0:
    #     return n2
    # if n2 == 0:
    #     return n1
    # rem1, rem2 = n1 % 10, n2 % 10
    # if rem1 < rem2:
    #     return rem1 + 10 * merge(n1 // 10, n2) 
    # else:
    #     return rem2 + 10 * merge(n1, n2 // 10)


def make_func_repeater(f, x):
    """Return another function which takes in another integer n and returns the result of applying f to x nth time.
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    # assert will execute nth times, seems not good.
    def repeat(n):
        assert n >= 0 and isinstance(n, int), "Repeat times must be a positive integer"
        if n == 0:
            return x
        else:
            return f(repeat(n - 1))
    return repeat


def is_prime(n):
    """Return True if positive integer n is a prime number(has exactly two unique factors: 1 and itself) and False otherwise.
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    assert n > 0 and isinstance(n, int), "is_prime takes in one positive integer."
    def prime_helper(count = 2):
        if n == 1:
            return False 
        if count > n - 1:
            return True 
        if n % count == 0:
            return False
        else:
            return prime_helper(count + 1)
    return prime_helper()
