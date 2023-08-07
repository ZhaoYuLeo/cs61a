def quota(f, limit):
    """Takes a one-argument function f and a non-negative integer limit. The
    function it returns has the same behavior as f, except that each value is
    only returned up to limit times. After that, the function returns an "Over
    quota" message instead, and the limit is decreased by 1 for future calls.
    A decorator that limits the number of times a value can be returned.
    >>> square = lambda x: x * x
    >>> square = quota(square, 3)
    >>> square(6)                       # 1st call with return value 36
    36
    >>> [square(5) for x in range(3)]   # 3 calls when the limit is 3
    [25, 25, 25]
    >>> square(5)                       # 4th call with return value 25
    'Over quota! Limit is now 2'
    >>> square(-6)                      # 2nd call with return value 36
    36
    >>> square(-6)                      # 3rd call when the limit is 2
    'Over quota! Limit is now 1'
    >>> square(7)                       # 1st call when the limit is 1
    49
    >>> square(5)                       # 5th call with return value 25
    'Over quota! Limit is now 0'
    """
    prevs = {}
    def limited(x):
        nonlocal limit
        r = f(x)
        t = prevs.get(r)
        if not t:
            prevs[r] = 1
        elif t < limit:
            prevs[r] = t + 1
        else:
            limit -= 1
            return 'Over quota! Limit is now ' + str(limit)
        return r
    return limited


def quota_solu(f, limit):
    """
    >>> square = lambda x: x * x
    >>> square = quota_solu(square, 3)
    >>> square(6)                       # 1st call with return value 36
    36
    >>> [square(5) for x in range(3)]   # 3 calls when the limit is 3
    [25, 25, 25]
    >>> square(5)                       # 4th call with return value 25
    'Over quota! Limit is now 2'
    >>> square(-6)                      # 2nd call with return value 36
    36
    >>> square(-6)                      # 3rd call when the limit is 2
    'Over quota! Limit is now 1'
    >>> square(7)                       # 1st call when the limit is 1
    49
    >>> square(5)                       # 5th call with return value 25
    'Over quota! Limit is now 0'
    """
    values = []
    def limited(n):
        nonlocal limit
        y = f(n)
        count = len([x for x in values if x == y])
        values.append(y)

        if count < limit:
            return y
        limit = limit - 1
        return 'Over quota! Limit is now ' + str(limit)
    return limited

