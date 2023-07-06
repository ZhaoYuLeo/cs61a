def luhn_sum(n):
    """Return the Luhn sum of n.
    >>> luhn_sum(135) #1+6+5
    12
    >>> luhn_sum(175) # 1 + (1+4) + 5
    11
    >>> luhn_sum(138743) # From lecture: 2 + 3 + (1+6) + 7 + 8 + 3 30
    30
    """
    even = lambda d: d
    odd = lambda d: 2 * d % 10 + 2 * d // 10
    return alt(even, odd, n)

    def alt(f, g, x):
        if x == 0:
            return x
        else:
            return f(x % 10) + alt(g, f, x // 10)



def subsum(n, k):
    """Return the maximum sum of up to k consecutive digits in n.
    >>> subsum(162553, 1) # 6
    6
    >>> subsum(162553, 2) # 5 + 5
    10
    >>> subsum(162553, 3) # 6 + 2 + 5 OR 5 + 5 + 3
    13
    >>> subsum(5, 0)
    0
    >>> subsum(5432, 100) # 5 + 4 + 3 + 2
    14
    """
    if k == 0 or n == 0:
        return 0
    copy = n
    total = 0
    index = 0
    while index < k:
        total += copy % 10
        copy = copy // 10
        index += 1
    return max(total, subsum(n // 10, k))


def subsum2(n, k):
    """Return the maximum sum of up to k consecutive digits in n.
    >>> subsum2(162553, 1) # 6
    6
    >>> subsum2(162553, 2) # 5 + 5
    10
    >>> subsum2(162553, 3) # 6 + 2 + 5 OR 5 + 5 + 3
    13
    >>> subsum2(5, 0)
    0
    >>> subsum2(5432, 100) # 5 + 4 + 3 + 2
    14
    """
    largest = 0 
    while n:
        copy, total, index = n, 0, 0
        while index < k:
            total += copy % 10
            copy = copy // 10
            index += 1
        largest = max(largest, total)
        n = n // 10
    return largest


def subsum_solu(n, k):
    """Return the maximum sum of up to k consecutive digits in n.
    >>> subsum_solu(162553, 1) # 6
    6
    >>> subsum_solu(162553, 2) # 5 + 5
    10
    >>> subsum_solu(162553, 3) # 6 + 2 + 5 OR 5 + 5 + 3
    13
    >>> subsum_solu(5, 0)
    0
    >>> subsum_solu(5432, 100) # 5 + 4 + 3 + 2
    14
    """
    recent, total, largest = 0, 0, 0
    w = pow(10, k)
    while n:
        n, d = n // 10, n % 10
        recent = 10 * recent + d
        total = total + d - recent // w
        recent = recent % w
        largest = max(largest, total)
    return largest


def make_adder(a):
    def adder(b):
        return a + b
    return adder

x = make_adder(9 - 3)
subsum(x(x(4256)), 4) # 20

x1 = make_adder(18 - 3)
subsum(x1(x1(4256)), 4) # 20

# (4256 + a + a, 4)    
# 4 + 2 + 5 + 6 = 17; if we want 20, we shoud add 3, which could be 12, 30 (even, since two a)
# a is 6 or 15.
