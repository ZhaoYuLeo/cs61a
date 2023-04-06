# actually quite hard to write without tree recursion.

def trace(f):
    def g(n, m):
        result = f(n, m)
        print(f.__name__ + '(' + str(n) + ', ' + str(m) + ') -> ' + str(result))
        return result
    return g

# can you write your own function acts as trace

@trace
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m
