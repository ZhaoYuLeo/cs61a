# Nonlocal

def stepper(num):
    """
    >>> step1 = stepper(10)
    >>> step1()                 # Modifies and returns num
    11
    >>> step1()                 # num is maintained across separate calls to step
    12
    >>> step2 = stepper(10)     # Each returned step function keeps its own state
    >>> step2()
    11
    """
    def step():
        nonlocal num # declares num as a nonlocal name
        num = num + 1 # modifies num in the stepper frame
        return num
    return step

# nonlocal is useful for maintaining state across different calls to the same function.

# However, there are two important caveats
# 1. A variable declared nonlocal must be defined in a parent frame which is not the global frame
# 2. Names in the current frame cannot be overridden using the nonlocal keyword.
# i.e.
# num_global = 10
# def step(num_global): # name 'num_global' is assigned to before nonlocal declaration
#     nonlocal num_global # no binding for nonlocal 'num_global' found
#     num_global = num_global + 1 # local variable 'num_global' referenced before assignment
#     return num_global

def memory(n):
    """Takes in a number n and returns a one-argument function. The returned function takes in a function that is used to update n and returns the updated n.
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def update_n_with(f):
        nonlocal n
        n = f(n)
        return n
    return update_n_with


# Mutation

# >>> pizza = ['cheese', mushrooms']
# >>> new_pizza = pizza + ['onions'] # creates a new python list
# This is silly, considering that all La Val’s had to do was add onions on top of pizza instead of making an entirely new pizza.
# In Python, some objects, such as lists and dictionaries, are mutable, meaning that their contents or state can be changed over the course of program execution. Other objects, such as numeric types, tuples, and strings, are immutable, meaning they cannot be changed once they are created.

# >>> s1 = [1, 2, 3]
# >>> s2 = s1
# >>> s1.append([-1, 0, 1])
# >>> s3 = s2[:]
# >>> s1[3] is s3[3]
# True
# >>> s1[:3] is s2[:3]
# False
# >>> s1[:3] == s2[:3]
# True

def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)


def group_by(s, fn):
    """Takes in a sequence s and a function fn and returns a dictionary. The values of the dictionary are lists of elements from s. Each element e in a list should be constructed such that fn(e) is the same for all elements in that list. The key for each value should be fn(e). For each element e in s, check the value that calling fn(e) returns, and add e to the corresponding group. 
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for e in s:
        key = fn(e)
        if grouped.get(key):
            grouped[key].append(e)
        else:
            grouped[key] = [e]
    return grouped 


def add_this_many(x, el, s):
    """ Takes in a value x, a value el, and a list s. Adds el to the end of s the number of times x occurs in s. Make sure to modify the original list using list mutation techniques.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    times = 0
    for v in s:
        if v == x:
            times += 1
    return s.extend([el for i in range(0, times)])


# Iterators

# Calling the iter function on an iterable will create an iterator over that iterable. Each iterator keeps track of its position within the iterable. Calling the next function on an iterator will give the current value in the iterable and move the iterator's position to the next value.
# The relationship between an iterable and an iterator is analogous to the relationship between a book and a bookmark - an iterable contains the data that is being iterated over, and an iterator keeps track of your position within that data.
# Once an iterator has returned all the values in an iterable, subsequent calls to next on that iterable will result in a StopIteration exception. In order to be able to access the values in the iterable a second time, you would have to create a second iterator.
# Most iterators are alse iterables - that is, calling iter on them will return an iterator. This means that we can use them inside for loops. However, calling iter on most iterators will not create a new iterator - instead, it will simply return the same iterator.

"""
>>> s = [[1, 2]]
>>> i = iter(s)
>>> j = iter(next(i))
>>> next(j)
1
>>> s.append(3)
>>> next(i)
3
>>> next(j)
2
>>> next(i)
>>> next(i)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> try:
        next(i)
    except StopIteration:
        print('No more values')
No more values
"""


# Generators

# When a generator function(including a yield statement) is called, it returns a generator object, which is a type of iterator(has a next method). A generator function is a special kind of Python function that uses a yield statement instead of a return statement to report values.
# The yield statement is similar to a return statement. However, while a return statement closes the current frame after the function exits, a yield statement causes the frame to be saved until the next time next is called, which allows the generator to automatically keep track of the iteration state.
# Once next is called again, execution resumes where it last stopped and continues until the next yield statement or the end of the function. A generator function can have multiple yield statements.
# When yield from is called on an iterator, it will yield every value from that iterator.

def filter(iterable, fn): 
    """ A generator function only yields elements of iterable for which fn returns True
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for e in iterable:
        if fn(e):
            yield e


def merge(a, b): 
    """ A generator function takes in two infinite generators a and b that are in increasing order without duplicates and returns a generator that has all the elements of both generators, in increasing order, without duplicates.
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    item_a, item_b = next(a), next(b)
    while True:
        if item_a < item_b:
            yield item_a
            item_a = next(a)
        elif item_a == item_b:
            yield item_a
            item_a, item_b = next(a), next(b)
        else:
            yield item_b
            item_b = next(b)
