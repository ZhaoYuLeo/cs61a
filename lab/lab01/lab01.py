def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    assert isinstance(k, int), "The second argument must be an integer"
    assert k >= 0, "The second argument must be positive"
    if k == 0:
      return 1
    return n * falling(n - 1, k - 1)


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    assert isinstance(y, int), "The input sum_digits(y) must be an integer"
    is_negative = True if y < 0 else False
    if is_negative:
      y = -y
    count = 0
    while (y // 10) != 0:
      count += y % 10
      y = y // 10
    count += y
    return -count if is_negative else count

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    pre_digit = n % 10
    while n // 10 != 0:
      n = n // 10
      if n % 10 == pre_digit:
        return True 
      pre_digit = n % 10
    return False
