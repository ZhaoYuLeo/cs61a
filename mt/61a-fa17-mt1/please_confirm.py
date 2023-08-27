def confirmer(code):
    """Return a confirming function for CODE.

    >>> confirmer(204)(2)(0)(4) # The digits of 204 are 2, then 0, then 4.
    True
    >>> confirmer(204)(2)(0)(0) # The third digit of 204 is not 0.
    False
    >>> confirmer(204)(2)(1)    # The second digit of 204 is not 1.
    False
    >>> confirmer(204)(20)      # The first digit of 204 is not 20.
    False
    """
    def check(last, result):
        def f(d):
            if (last == d):
                return result
            else:
                return False
        return f

     
    # generate a series of check method for each digit of n
    def helper(n, result):
        left, last = n // 10, n % 10
        if left == 0:
            return check(last, result)
        else:
            return helper(left, check(last, result))

    return helper(code, True)


def confirmer_solu(code):
    """Return a confirming function for CODE.

    >>> confirmer_solu(204)(2)(0)(4) # The digits of 204 are 2, then 0, then 4.
    True
    >>> confirmer_solu(204)(2)(0)(0) # The third digit of 204 is not 0.
    False
    >>> confirmer_solu(204)(2)(1)    # The second digit of 204 is not 1.
    False
    >>> confirmer_solu(204)(20)      # The first digit of 204 is not 20.
    False
    """
    def confirm1(d, t):
        def result(digit):
            if d == digit:
                return t
            else:
                return False
        return result

    def extend(prefix, rest):
        """Return a confirming function that returns REST when given the digits of
        PREFIX. For example, if c = extend(12, confirmer(34)), then c(1)(2) returns
        confirmer(34), so that c is a confirming function for 1234.
        """
        left, last = prefix // 10, prefix % 10
        if prefix < 10:
            return confirm1(prefix, rest)
        else:
            return extend(left, confirm1(last, rest)) # or extend(left, extend(last, rest))

    return extend(code, True)



def decode(f, y=0):
    """Return the code for a confirming function f.
    >>> decode(confirmer(12001))
    12001
    >>> decode(confirmer(56789))
    56789
    """
    for d in range(10):
        new_f = f(d)
        if new_f is True:
            return 10 * y + d
        if callable(new_f):
            return decode(new_f, 10 * y + d)


def decode_solu(f, y=0):
    """Return the code for a confirming function f.

    >>> decode_solu(confirmer(12001))
    12001
    >>> decode_solu(confirmer(56789))
    56789
    """
    d = 0
    while d < 10:
        x, code = f(d), 10 * y + d
        if x == True:
            return code
        elif x == False:
            d = d + 1
        else:
            return decode(x, code)

