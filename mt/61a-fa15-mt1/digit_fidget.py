# Each digit in a non-negative integer n has a digit position.
# Digit positions begin at 0 and count from the right-most digit of n.
# In 568789, the digit 9 is at position 0 and digit 7 is at position 2.
# The digit 8 appears at both positions 1 and 3.

def find_digit(n, d):
    """Return the largest digit position in n for which d is the digit.
    >>> find_digit(567, 7)
    0
    >>> find_digit(567, 5)
    2
    >>> find_digit(567, 9)
    False
    >>> find_digit(568789, 8)
    3
    """
    # Assume n is a non-negative integer and d is a digit greater than 0 and less than 10
    count = 0
    position = False
    while (n > 0):
        if (n % 10 == d):
            position = count
        count += 1;
        n = n // 10
    return position

# Circle all values of y for which the final expression below evaluates to True.
# Assume that find_digit is implemented correctly.
# 1 2 3 4 5 6 7 8 9

f = lambda x: find_digit(234567, x) #6 in 1 position, 5 in 2 position ...

def compose1(f, g):
    return lambda x: f(g(x))

for y in range(2, 6):
    print(compose1(f, f)(y) == y)

def luhn_sum(n):
    """Return the Luhn sum of n.
    The Luhn sum of a non-negative integer n adds the sum of each digit in an even position
    to the sum of doubling each digit in an odd position.
    If doubling an odd digit results in a two-digit number, those two digits are summed to
    form a single digit.
    >>> luhn_sum(135)     # 1 + 6 + 5
    12
    >>> luhn_sum(185)     # 1 + (1+6) + 5
    13
    >>> luhn_sum(138743)  # From lecture: 2 + 3 + (1+6) + 7 + 8 + 3
    30
    """
    # Assume n is a non-negative integer
    total = 0
    position = 0
    while n:
        n, last = n // 10, n % 10
        if position % 2:
            last *= 2
            total += last % 10 + last // 10
        else:
            total += last
        position += 1
    return total

def luhn_sum2(n):
    """
    >>> luhn_sum2(135)     # 1 + 6 + 5
    12
    >>> luhn_sum2(185)     # 1 + (1+6) + 5
    13
    >>> luhn_sum2(138743)  # From lecture: 2 + 3 + (1+6) + 7 + 8 + 3
    30
    """
    total = 0
    def odd(last):
        return last
    def even(last):
        last *= 2
        return last % 10 + last // 10
    while n:
        n, last = n // 10, n % 10
        total += odd(last)
        n, last = n // 10, n % 10
        total += even(last)
    return total


def luhn_sum_solu(n):
    """
    >>> luhn_sum_solu(135)     # 1 + 6 + 5
    12
    >>> luhn_sum_solu(185)     # 1 + (1+6) + 5
    13
    >>> luhn_sum_solu(138743)  # From lecture: 2 + 3 + (1+6) + 7 + 8 + 3
    """
    def luhn_digit(digit):
        x = digit * multiplier
        return (x // 10) + x % 10
    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total = total + luhn_digit(last)
        multiplier = 3 - multiplier #impressive
    return total


def check_digit(n):
    """Add a digit to the end of n so that the result has a valid Luhn sum.
    A non-negative integer has a valid Luhn sum if its Luhn sum is a multiple of 10.
    >>> check_digit(153) # 2 + 5 + 6 + 7 = 20
    1537
    >>> check_digit(13874)
    138743
    """
    return n * 10 + (10 - luhn_sum(n * 10) % 10) % 10 # attention
