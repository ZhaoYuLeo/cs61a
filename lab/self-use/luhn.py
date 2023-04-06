"""
Sum all digits up. Double even digits, if it is greater than 9, sum digits up
How can you keep track of you are on a odd digit or an even digit?
These is mutual recursion when two functions call each other. Now base cases can appear in both those functions or in only one. In this case, it appears in both.
For credit card number, result % 10 == 0
"""
def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

# figure out waht state must be maintained by the iterative function.
def sum_digits_iter(n):
    digit_sum = 0
    while(n > 0):
        n, last = split(n)
        digit_sum += last
    return digit_sum

# Iteration is a special case of recursion
# the state of an iteration can be passed as arguments.
def sum_digits_rec(n, digit_sum):
    if n == 10:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, last + digit_sum)

# that is what programming language said, you can not only recurse yourself but also other functions
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhu_sum_double(all_but_last) + last

def luhu_sum_double(n):
    all_but_last, last = split(n)
    print(last)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
