def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
      return True
    else:
      return False

# better use boolen operators when only return true or false
def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining

def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
       x=x+1
    return x / 0

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    assert n > 1, "The input is_prime(n) must be larger than 1"
    divisor = 2;
    while divisor < n:
      if n % divisor == 0:
        return False 
      divisor += 1
    return True 

