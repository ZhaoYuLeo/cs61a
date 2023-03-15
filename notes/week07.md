# Mutable Functions

functions that have data associated with them that changes.

A function with behavior that varies over time.

Example: withdraw money from bank account

```shell
>>> withdraw = make_withdraw(100) # the balance stored in the parent frame of the function. withdraw has a body and a parent environment
>>> withdraw(25)
75
>>> withdraw(25)
50
>>> withdraw(60)
'Insufficient funds'
```



------



##### Reminder: Local Assignment

```python
def percent_difference(x, y):
  difference = abs(x-y) # binds name(s) to value(s) in the first frame of the current environment
  return 100 * difference / x
diff = percent_difference(40, 50)
```

**Execution rule for assignment statements:**

1. Evaluate all expressions right of =, from left to right
2. **Bind** the names on the left to the <u>resulting values in the **current frame** (local scope)</u>

<!--为什么我们需要nonlocal，去掉nonlocal无法运行成功-->

------



##### Non-Local Assignment & Persistent Local State

```python
def make_withdraw(balance):
  """Return a withdraw function with a starting balance."""
  def withdraw(amount):
    nonlocal balance
    if amount > balance:
      return 'Insufficient funds'
    # Re-bind balance in the first non-local fram in which it was bound previously
    balance = balance - amount
    return balance
  return withdraw
```

------



##### The Effect of Nonlocal Statements

`nonlocal <name>, <name>, ...`

**Effect**:  Future assginments to that name change its pre- existing binding in the **first non-local frame** of the current environment in which that name is bound.

Python Docs:  an "enclosing scope"

Names listed in a nonlocal statement must refer to <u>pre-existing</u> bindings in an <u>enclosing scope</u>.

Names listed in a nonlocal statement must not <u>collide with pre-existing</u> bindings in the <u>local scope</u> (current frame).

------



##### Python Particulars

Python pre-computes which frame contains each name before executing the body of a function. Within the body of a function, <u>all instances of a name must refer to the same frame.</u>

—— which means you're not allowed to have the same name in the same function body acutally refer to two different frames that just doesn't work.

```python
def make_withdraw(balance):
  def withdraw(amount):
    if amount > balance: # non-local lookup of balance
      return 'Insufficient funds'
    balance = balance - amount # local assignment
    return balance
  return withdraw
```



```shell
>>> w = make_withdraw(100)
>>> w
<function ...>
>>> w(10)
Traceback (most recent call last):
...
UnboundLocalError: local variable 'balance referenced before assignment'
>>>
```

------



##### Mutable Values & Persistent Local State

Mutable values can be changed *without* a nonlocal statement .

```python
def make_withdraw_list(balance):
  b = [balance]
  def withdraw(amount):
    """
    we have no non-local statements because we're never changing what B is bound to or what balance is bound to or what withdraw is bound to from within the body of withdraw
    """
    if amount > b[0]:
      return 'Insufficient funds'
    b[0] = b[0] - amount # changing mutable values
    return b[0]
  return withdraw

withdraw = make_withdraw_list(100)
withdraw(25)
```



<!--这样看起来assignment=在面对mutable value和immutable value时的表现，看起来有些区别。你想说的是前者bind，后者change吗-->



##### referential transparency

Expression are **referentially transparent** if substituting an expression with its value does not change the meaning of a program

<!--如果用表达式的值替换表达式不会改变程序的含义，则表达式是引用透明的。-->

```python
# same program
mul(add(2, mul(4, 6)), add(3, 5))
mul(add(2, 24), add(3, 5))
mul(26, add(3, 5))
```

<u>Mutation</u> operations violate the condition of referential transparency because they do more than just return a value; **they change the environment.**

```python
def f(x):
  x = 4
  def g(y):
    def h(z):
      nonlocal x
      x = x + 1
      return x + y + z
    return h
  return g

a = f(1)
b = a(2)
total = b(3) + b(4)
# total = 10 + b(4)
```



### QA

1. Is Nonlocal assignment used much in practice?

​		it's unusual

2. When a list refers to itself, how does that work?

   ```python
   >>> t = [1, 2, 3]
   >>> t[1:3] = [t]
   >>> t
   [1, [...]]
   >>> t[1][1][1][1][0]
   1
   ```

   

   there‘s two things going on. There's how the list is being stored and then how it's represented when you try to print it and those are distinct things

   

   <!--t[1]指向t，正想问题所说的那样是个refer to itself-->

3. How do you solve a tree problem with that involves two labels for nodes that aren't next to each other?

   some mechanism for getting the information in one part of the tree available as you‘re processing another part of a tree

   so um I guess there‘s two kinds of questions there’s questions that involve just like some fact about all the labels like what‘s the second largest label in the whole tree and in those you kind of want to process the whole tree but as you go you need to keep track of what's going on so I think you'd have to keep track of both the biggest and the second biggest thing you've seen so far and whenever you see something that's bigger than one of those then you need to kind of update that. so that's one kind of problem.

   And another kind of problem might be um for two nodes at the same depth but not necessarily direct siblings um which one's the biggest or something like that like yeah what's the largest difference between two nodes that are at the same depth and this um it similarly involves just processing the whole tree but at the same time keeping track of an additional piece of information which is what depth you're at.

   Y: but let me offer another thought here is processing data in a tree is just a slightly more complicated than processing data in a list so in a list you have neighbor elements right there are indexes different by one. In a tree you have the parent-child relationship but if I want to know for example that John was just saying what the smallest element in the list I've got to traverse the whole list if I want to know what the smallest element in the tree is I have to traverse the whole tree and there's <u>a couple different ways</u> of doing that. <u>You can go all the way down and then start making you way back</u> and the only other example I could think of too was that same notion of maybe you want to come because there's there's another sort of dimension if you will to a tree it's just not the ordering there's sort of the depth ordering that's the only other thing I can think about in which case as you're traversing a tree you have to keep track of that sort of informantion and then sort of analyze things at the back end.



4. How do you sovle Q1 of Quize 4 from the exam prep section?

```python
from tree import *

def profit(t):
    """Return the max profit.
    >>> t = tree(2, [tree(3), tree(4, [tree(5)])])
    >>> profit(t) # 2_4 or 2_5 or 3_5 since they are not connected directly.
    8
    """
    return helper(t, False)
  
def helper(t, used_parent):
    if used_parent:
        return                       sum([helper(b, False) for b in branches(t)])
    else:
        use_label_total = label(t) + sum([helper(b, True) for b in branches(t)])
        skip_label_total =       0 + sum([helper(b, False) for b in branches(t)])
        return max(use_label_total, skip_label_total)
```

John DeNero:

but in both cases I guess we are illustrating exactly the general principle we were talking about before which is that sometimes as you <u>traverse a  tree</u> you have to <u>keep track of information about the rest of the tree</u> that <u>you can't see right now</u>. So at the very beginning you can see the whole tree but later on as you're making recursive calls you can only see the current node and what's below it. if you need <u>information</u> about what's <u>above it</u> like whether you included the parent and the total the you need to keep track of that information by <u>passing it as an argument</u> and this recursive call <!--sum([helper(b, False) for b in branches(t)])--> is telling the function that's going to process the branch some information about what's going on above that branch.



Y:

it's always easy to sovle the problem when you know the answer.



5. Why when you assign to a local name that is the same as a nonlocal name, you get an error when referencing the nonlocal name?

```python
def f(x):
    def g(y):
        print(x + 1) # UnboundLocalError: local variable "x" referenced before assignment
        x = y
    return g

  f(3)(4)
```



John DeNero:

there‘s many concerns in programming languages but two of them are it should be easy for the user to <u>express the program that they want</u> and uh that <u>program should run reasonably fast.</u> There's this <u>particular optimization</u> I think python does which is that it has a constraint that says <u>all the  names within a function that are the same</u> so like all the x‘s within this body of g have to refer to the same frame that‘s just like a restriction that exists in the language that means you can't have two x's in the same body where one refers to the global frame and one refers to the local frame or something like that and they do this so that like basically when you‘re figuring out what your program means and you‘re going to execute it, it's easy to figure out like where in memory something lives.

I think I think it‘s sort of an optimization but why isn‘t important.

I think as a programmer you just need to know that this is a constraint so there‘s no way to write a program that kind of accesses this x and then changes an x in here and this line would in fact change an x in here as opposed to anywhere else this is local assignment so why is it that you get the error here instead of here. 

well, in some sense you could say like python‘s broken and that‘s a perfectly reasonable reaction um there is an error so whether it shows up here or here I don't know if it‘s that big of a deal like there’s a problem with this code and python is telling you there‘s a problem with this code and so you got to go fix it. 

I would have if I were designing the language I would prefer for the error to like come up somewhere else or to say something other than this is particularly misleading. 

The error really is that you‘re trying to use an x from the f1 frame and then assgin to an x in an f2 frame and  that isn't allowed. X needs to refer to one particular variable in a particular frame whenever it‘s uh used multiple times in the definition of the same function so one way to think about it is um the problem is not so much line 4. It‘s really the combination of line 3 and 4.

Y：

It's that you‘re using the variable in different ways so if I had taken out line 3, line 4 would have been fine so that‘s a one way to convince yourself that you know it‘s the combination of the two lines so you may as well do it in the first one but it also means that <u>python knows what‘s happening downstram right.</u> It‘s not It’s not blind to the code it is about to <u>evaluate</u>.



John DeNero:

Yeah yeah this is the particularly spooky part I think for student who sees this is like well you mean python knows the future of what the rest of the code looks like and in fact it does so there‘s multiple stages to interpreting a program and one of them is just to read the code and make sure that all the parentheses line up and all the brackets line up and actually that happens for your entire python file before anything gets executed is that it kind of does a <u>syntax check</u>. Now that syntax check in python tends to be a little bit more involved because it's trying to set up the program to run quickly so it doesn't just make sure the parentheses are matched it also figures out that f<u>or every name which frame is it going to refer to</u> and so it has kind of looked ahead at your code to figure out is this a local x or is this a non-local x like where in the environment is this x going to be and it saw this line and <u>determined it was going to be local</u> and then when it tried to execute this, it didn‘t find that x defined yet and so that‘s why you got this particular error but that‘s just like a detail of how the interpreter works not so much about the language but like about <u>how the language mechanics actually run</u> which i guess now you know but uh the mistake of having x try to refer to two places at once is something that like everyone should know because that‘s a constraint about the language.



Y：

and by the way I agree that the error message here is awful right they should be able to give us a better error message than that yeah.



<!--看起来他们好像在尽量避免把话题引到更深的interpret上，试图站在一个client的角度上向学生解释what is going on.--> 

<!--他是否隐含使用local variable对于python来说more effective？--> 

6. How do you solve Q7 of Summer 2020 Midterm 2?

```python
def village(apple, t):
    """
    The `village` operation takes
        a function `apple` that maps an integer to a tree where 
            every label is an integer.
        a tree `t` whose labels are all integers.
        
    And applies `apple` to every label in `t`.
    
    To recombine this tree of trees into a a single tree,
        simply copy all its branches to each of the leaves
        of the new tree.
        
    For example, if we have
        apple(x) = tree(x, [tree(x + 1), tree(x + 2)])
    and
        t =   10
             /  \
           20    30
    We should get the output
        village(apple, t)
          =                 10
                         /      \
                      /            \
                     11             12
                   /    \         /    \
                 20      30      20      30
                /  \    /  \    /  \    /  \
               21  22  31  32  21  22  31  32

    >>> t = tree(10, [tree(20), tree(30)])
    >>> apple = lambda x: tree(x, [tree(x + 1), tree(x + 2)])
    >>> print_tree(village(apple, t))
    10
      11
        20
          21
          22
        30
          31
          32
      12
        20
          21
          22
        30
          31
          32
    """
    def graft(t, bs):
        """
        Grafts the given branches `bs` onto each leaf
        of the given tree `t`, returning a new tree.
        """
        if ______:
            return ______
        new_branches = ______
        return tree(______, ______)
    base_t = ______
    bs = ______
    return graft(base_t, bs)
    
  
```

call graft on some tree and some branches and your question was how come these aren't part of graft or hwo come they're indented the way that they are. This structure says define a new function called graft which in principle has access to the apple function and the t which we might need.

um and then, after you're done defining this function build some new things a tree and some branches and call graft on those two things.



Let me just start with one obvious thing. that graph function is embedded in a larger function.



So we need to build we need to call apple one the label of the tree. We need to um kind of recursively do this I think. Uh we either do it now or we do it later. It's not clear to me how this is set up. uh

`base_t = apple(label(t))`

I guess we need to know what we're going to graft on and that will be the result of calling village a branch of tree using apple. Apple‘s the first argument. for every b in branches of t.

`bs = [village]`

okay, now we do the grafting and what does that grafting look like. well if t is a leaf

`is_leaf(t)`

then to graft these things on.

what a strange structure we have here. 

Y：

so we are making a tree. Do you have to return a tree with t in the node and bs as the children? 



is that right?

`tree(label(t), graft)`

I guess what we could do is we could uh graft these branches on all to onto all the branches of the tree.

`tree(label(t), [graft(b, bs) for b in branches(t)])`



Y：I was thinking that was going to be our base case. I wasn't expecting a recursive call there

Yeah I'm  just trying to fit the template

Y: yeah

Okay so now we've got a leaf. Uh oh I see so they're trying to set us up to do this here I think

Y: yeah that makes more sense

`return tree(label(t))`

`new_branches = [graft(b, bs) for b in branches(t)]) `

seems like this template has multiple possible solutions but we'll uh do it this way okay so to if we reach a leaf then we create a tree with a bunch of branches otherwise we do this recursively and create a tree with these new branches. It looks better.

that works at least for one example.



How do you know since the output tree is a different structure than the input tree how is it that we have kept track of the original tree well enough to build the output tree without kind of getting the two confused with each other and without changing the original tree?

so one thing about changing is that we are just building new stuff all the time we're not editing the contents of the original tree we know that because we don't see any `append` `extend element``assignment` `slice assignment`anything like that. All we're doing is going through the original tree and building new trees along the way.

um now how is it that we're building these new trees and still kind of keeping track of where we were in the original tree ?

That's a great question we're kind of relying on recursion to do that for us so when we make a recursive call to village we are making it on the branches of the original tree so all those calls to village that will happen along the way because of the recursion are going to be processing parts of the original tree and there's no risk that they will instead be processing something else because we only call village on parts of the original tree which then calls village on parts of that original branch etc

And the building of new tree with the new structure <u>only really happens in the return value</u> to the viilage which does have this like unusual structure with a lot of repetition in it but but that all gets constructed after you kind of go through and make sure you call village on each note.



7. What's the difference between adding two lists together and using append?

```shell
>>> a = [1, 2]
>>> b = [3, 4]
>>> c = a
>>> a is c
True
>>> a = a + b
>>> a 
[1, 2, 3, 4]
>>> b
[3, 4]
>>> c
[1, 2]
```



```shell
>>> a = [1, 2]
>>> b = [3, 4]
>>> c = a
>>> a is c
True
>>> a += b # += quite like extend
>>> a 
[1, 2, 3, 4]
>>> b
[3, 4]
>>> c
[1, 2, 3, 4]
```



### Lab 06: Nonlocal, Mutability

# Iterators



A container can provide an iterator that provides access to its elements in some order.

`iter(iterable)`: Return an iterator over the elements of an iterable value

`next(iterable)`: Return the next element in an iterator

```python
>>> s = [[1, 2], 3, 4]
>>> s
[[1, 2], 3, 4]
>>> next(s)
>>> next(s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not an iterator
>>> t = iter(s)
>>> next(t)
[1, 2]
>>> next(t)
3
>>> list(t)
[4]
>>> next(t)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

##### Dictionary Iteration

All iterators are mutable objects.

The order of items in a dictionary is the order in which they were added (Python 3.6+)

Historically, items appeared in an arbitrary order (Python 3.5 and earlier)

```python
>>> d = {'one': 1, 'two': 2}
>>> k = iter(d)
>>> next(k)
'one'
>>> d['zero'] = 0
>>> next(k)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
>>> d
{'one': 1, 'two': 2, 'zero': 0}
>>> k = iter(d)
>>> next(k)
'one'
>>> next(k)
'two'
>>> d['zero'] = 5 # didn't change the shape
>>> next(k)
'zero'
>>>
```

##### for statement

```python
>>> r = range(3, 6)
>>> list(r)
[3, 4, 5]
>>> for i in r:
...     print(t)
... 
<list_iterator object at 0x7fd54817a3a0>
<list_iterator object at 0x7fd54817a3a0>
<list_iterator object at 0x7fd54817a3a0>
>>> for i in r:
...     print(jhghkl)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'jhghkl' is not defined
>>> for i in r:
...     print(i)
... 
3
4
5
>>> ri = iter(r)
>>> ri
<range_iterator object at 0x7fd54821eba0>
>>> next(ri)
3
>>> for i in ri:
...     print(i)
... 
4
5
>>> 
```



```python
>>> r = range(3, 6)
>>> ri = iter(r)
>>> for i in ri:
...     print(i)
... 
3
4
5
>>> for i in ri:
...     print(i)
... 
```



If I use an iterator in a for statement, I can still go through all of the elements until I reach the end. But that will advance the iterator so that I can't use it again. For iterable object, it is different.



##### Built-in Iterator functions

Many build-in Python sequence operation return iterators that compute results <u>lazily</u> 

Only compute when needed.

`map(func, iterable)` `filter(func, iterable)` `zip(first_iter, second_iter)` `reversed(sequence)`

`list(iterable) ` `tuple(iterable) ` `sorted(iterable) `

<!--非常像我们在ML中实现的那些经典的function，和iterable，higher order function有关的那章。不过python的这些是lazily的-->

```python
>>> bcd = ['b', 'c', 'd']
>>> [x.upper() for x in bcd]
['B', 'C', 'D']
>>> map(lambda x: x.upper(), bcd)
<map object at 0x7fd54821eca0>
>>> m = map(lambda x: x.upper(), bcd)
>>> next(m)
'B'
>>> next(m) # perform different with list com...
'C'
>>> next(m)
'D'
>>> next(m)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```



```python
>>> map(double, [3, 5, 7])
<map object at 0x7fd54821e820>
>>> m = map(double, [3, 5, 7])
>>> next(m)
** 3 => 6 **
6
>>> next(m)
** 5 => 10 **
10
>>> next(m)
** 7 => 14 **
14
>>> next(m)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration


>>> m = map(double, range(3, 7))
>>> f = lambda y: y >= 10
>>> t = filter(f, m)
>>> next(t)
** 3 => 6 **
** 4 => 8 **
** 5 => 10 **
10
>>> next(t)
** 6 => 12 **
12
>>> list(t)
[]
>>> list(filter(f, map(double, range(3, 7))))
** 3 => 6 **
** 4 => 8 **
** 5 => 10 **
** 6 => 12 **
[10, 12]


>>> t = [1, 2, 3, 2, 1]
>>> t
[1, 2, 3, 2, 1]
>>> reversed(t)
<list_reverseiterator object at 0x7fd54817a3a0>
>>> reversed(t) == t
False
>>> list(reversed(t)) == t # emmm, seems different with '==' in Java. Python compares what in this case ??? TODO
True
>>> 

def double(x):
    print('**', x, '=>', 2*x, '**')
    return 2*x

```



##### Generators and Generator Functions

```python
>>> def plus_minus(x):
...     yield x
...     yield -x
... 
>>> t = plus_minus(3)
>>> next(t)
3
>>> next(t)
-3
>>> t
<generator object plus_minus at 0x7fd548237040>
>>> 
```

A *generator function* is a function that **yields** values instead of **return**ing them

A normal function **returns** once; a *generator function* can **yield** multiple times

A *generator* is an iterator created automatically by calling a *generator function*

When a *generator function* is called, it returns a *generator* that iterates over its yields.



```python
def evens(start, end):
  even = start + (start % 2)
  while even < end:
      yield even # pause off
      # continue where it left off when "next"
      even += 2

>>> list(evens(1, 10))
[2, 4, 6, 8]
>>> t = even(2, 10)
>>> next(t)
2
>>> next(t)
4
>>>
```

##### Generators & Iterators

##### Generators can Yield from Iterators

A **yield from** statement yields all values from an iterator or iterable (Python 3.3)

```python
>>> list(a_then_b([3, 4], [5, 6]))
[3, 4, 5, 6]

def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x

def a_then_b(a, b):
    yield from a
    yield from b
```



```python
>>> list(coutdown(5))
[5, 4, 3, 2, 1]

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k - 1)
```



```python
def countdown(k):
    if k > 0:
        yield k
        yield countdown(k - 1) # When a *generator function* is called, it returns a *generator* that iterates over its yields.

>>> t = countdown(3)
>>> next(t)
3
>>> next(t)
<generator object countdown at 0x7fd548237040>
>>> next(t)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```



```python
def countdown(k):
    if k > 0:
        yield k
        # yield from countdown(k - 1)
        for x in countdown(k - 1):
            yield x
    else:
        yield 'Blast off'
```



```python
def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

>>> prefixes('both')
<generator object prefixes at 0x7fd548237190>
>>> list(prefixes('both'))
['b', 'bo', 'bot', 'both']
>>> 
```



```python
def substring(s):
    if s: # s isn't empty string
        yield from prefixes(s)
        yield from substring(s[1:])

>>> list(substring('tops'))
['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
```



### QA

[00:03](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=3s) What is the relationship between "yield from" and a for statement that yields? 

"Yield from" goes through all the elements of some iterable and yields each of them so it's just a syntactic shortcut.

[02:27](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=147s) Do you always need a yield after a "yield from" statement?



 [02:54](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=174s) What does prefixes(s[:-1]) evaluate to in the prefixes example from lecture?



 [03:38](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=218s) Why does removing the yield statement in prefixes cause the function not to yield anything? 



```python
>>> prefixes('dogs')
<generator object prefixes at 0x7fc610160f90>
>>> list(prefixes('dogs'))
[]
>>> # why is that?

def prefixes(s):
    if s:
        for x in prefixes(s[:-1]):
            yield x
        # yield s
```

Well we've written something that just yields the prefixes for the like smaller version so if this is dogs we're yielding whatever we get be calling prefixes on dog which in turn would yield whatever we get for calling prefixes on  do which would return whatever we get for calling prefixes on d which could return nothing. We've reached oh sorry which would return the result of calling prefixes on the empty string and that would yield nothing. So the base case here is like if there's no letters then there's no yield therefore we're not producing anything and since we don't produce anything in the base case and this ever says `yield from prefix(s[:-1])`is yield whatever the next recursive call would yield. We end up not yielding anything at all so in general if you like ever have a function where you yield from an empty list`yield from []`that's not going to yield anything at all.



[05:03](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=303s) If an iterator is not a list, then what is it?

So in that sense it's it has different behavior than a list because it's both a list and like a marker for where you are. 

But list iterators are not the only kind of iterators. You could have an iterator through the labels in a tree you could have an iterator through the prefixes in a strnig. You could have iterator through anything and it‘s just a description of something that lets you go through multiple elements in some order by calling next on the iterator and getting the next value and you can do that over and over again.

So it's quite an abstract thing as opposed to feeling quite as concrete as for example a list.



 [06:25](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=385s) When should you use built-in Python features instead of reimplementing them?

.... Gnarly .... compatible .... but if you are doing rapid prototyping and you just want to get something built sure using all the built-in functions is great it saves you from writing a lot of code and doing a lot of debugging.



I think everyone who's building software has come to a point that they've written a ton of code and then realized oh this is just like a special case of some genral thing that's built in I've basically just like rewritten all the mechanics of a dictionary or something like that when in fact I could have just like used the one that's built in and it would have been on line and that's okay. Um happens to all of us and you know is the version that you wrote better or the built-in one better. Uh it depends on how it's going to be used uh like **connie** said especially if something's just recently been introduced then it's probably worth avoiding it for a while if you want to be kind of compatible with everybody else. 

But using the build-in functionality means that your program might get better without you having to do anything at all like .......



 [09:34](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=574s) What happens if you reverse the order of "yield" and "yield from" in the prefixes example?

for posterity's sake

python is going to go through and do these things in the order that you write them and that will have an impact on exactly what happens. 

Some interesting concurrency benefits to yielding ..... in their like sophistication of programming .....



 [11:45](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=705s) Why do you need to "yield from" the recursive call to countdown instead of just yielding it?

[5, <generator object>]

you can call next() on that generator object

It is still there. It's just sort of that lazy evaluation that you have to now unpack it.

 [13:30](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=810s) Why does calling list on an iterator twice return an empty list the second time?

The iterator is used up as a side effect of calling list on it.

list() is kind of like calling next over and over again and putting all the results in a list.

```python
t = iter([1, 2, 3])
list(t) # t is changing
list(t)
```

think of these iterators as one use disposable operators.

It's like snapchat right. The image came in you look at it and then it vanishes and it's gone.



 [16:30](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=990s) What are the practical applications of yield, rather than just returning?

There's this kind of like pipeline of information flow where stuff sort of is becoming available incrementally and you want to yield it as soon as it's available that's where it's used a lot.

John does natural language processing so he talks about text. I do images in video so my examples is we take a video and we have to decompress the video to do an analysis of it.





 [19:10](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=1150s) Is it true that a generator is always an iterator, but an iterator is not always a generator?

Generator are more specific but the way you use a generator is the same as how you use an iterator. It's just talking about where it came from.



 [19:53](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=1193s) How would you solve the Summer 2020 Midterm Question 2?



```python
def schedule(galaxy, sum_to, max_digit):
    """
    A 'galaxy' is a string which contains either digits or '?'s.

    A 'completion' of a galaxy is a string that is the same as galaxy, except
    with digits replacing each of the '?'s.

    Your task in this question is to find all completions of the given `galaxy`
    that use digits up to `max_digit`, and whose digits sum to `sum_to`.

    Note 1: the function int can be used to convert a string to an integer and str
        can be used to convert an integer to a string as such:

        >>> int("5")
        5
        >>> str(5)
        '5'

    Note 2: Indexing and slicing can be used on strings as well as on lists.

        >>> 'evocative'[3]
        'c'
        >>> 'evocative'[3:]
        'cative'
        >>> 'evocative'[:6]
        'evocat'
        >>> 'evocative'[3:6]
        'cat'


    >>> schedule('?????', 25, 5)
    ['55555']
    >>> schedule('???', 5, 2)
    ['122', '212', '221']
    >>> schedule('?2??11?', 5, 3)
    ['0200111', '0201110', '0210110', '1200110']
    """
    def schedule_helper(galaxy, sum_sofar, index):
        if ______ and ______:
            return [galaxy]
        elif ______:
            return []
        elif ______:
            return ______
        ans = []
        for x in ______:
            modified_galaxy = ______
            ______
        return ans

    return ______
```

Let's take a look. Seems we'll do some recursion. Uh we have a helper which has a galaxy. um the fact that there's a galaxy here in a galaxy here means that maybe we'll be changing this along the way like filling in digits for example. Here we have a sum so far, which could tell us whether we've reached the sum we're tring to eventually achieve and the index I guess means that we're going to walk through here, element by element.

Okay, so we'll call schedule helper

`schedule_helper(galaxy, 0, 0)`

on the original galaxy. The sum so far I think is zero we haven't done anything yet and we'll start at the beginning and we'll see what we do.

If it's the case that we're done then we're going to return a list containing galaxy okay that's good. But this means the galaxy that gets passed in here has to have all the question marks filled in if we're going to returning it so we know we're going to be kind of filling in things as we go. 

If it's case that maybe we've reached a sum that's too big then we have a problem so I think there's probably some base case like 

`some_sofar > sum_to`

then we have a probelm there might be some other base cases that we have to think about as well. 

And I'm not sure what's going on here yet, we'll think about that later.

Here's kind of main recursive loop which is that we build a list we go through every x in something.  Probably the digits  from zero to 9 or something like that. 

Uh and we fill in a question mark that seems like what modified galaxy is going to be all about.

Um so I kind of feel like this is going to be the case where there's no question mark and this is going to be the case where there is question mark and then you have to like try all the possibilities. So it might be something like,

`galaxy[index] != '?'`

and we'll just use that first value so we'll call schedule

`schedule_helper(galaxy, sum_sofar + int(galaxy[index]), index + 1) `

what if there's a question mark so here

`#this is`

In fact I'm just going to rewrite it

`elif galaxy[index] == '?': `

and I think this will do the same thing right.

We're gonna find all the different ways of doing this. Um go through the digits zero one two three four five...

`for x in range(10)`

We're gonna build a new string which is

`galaxy[:index] + str(x) + galaxy[index + 1:]` 

That might work so let's just like look what this does for an example before we go on whould be nice to know that it works so

`x = 4; index = 2; galaxy = "23?56"; ...`

There is this long line wo what do we do well we have to get some more answers in there. Uh I'm gonna recursively call schedule_helper

`anx.extend(schedule_helper(modified_galaxy, sum_ssofar + x, index + 1))`

And we do this for all the index like why is it  the case that I called schedule helper here. This is where I'm going to fill in all the other question marks that are later on and make sure that I got the sum right. 

All right now I think we need to get this base case of when we have found a fully complete galaxy so this would be like 

`if index == len(galaxy) and sum_sofar == sum_to: `

then maybe we're done.

`doctest`

Nope W

`elif sum_sofar > sum_to or index >= len(galaxy)`

so if you kind of like get to the end and you don't have a sum that's big enough then I guess you need to stop

`doctest`

what on earth

oh I don't think you're supposed to use...

oh parts of the size max digit 

yeah

You can't always go to ten.

`range(max_digit + 1)`

You should probably read the question first. 

okay now it works.

##### review

So what got us here well we kind of track of

what information we needed to maintain along the way and there were like some pretty good clues in the question of what to do based on the name `sum_to` and `sum_sofar` and it took a minute to kind of think through the base cases and I think we could have figured this out without running  the code just by kink of like considering different cases uh reading the question carefully uh but since we had it all set up we just ran the `doctest` instead to get a clue about whether we had done it right or not.

##### refactor

`list()`

`yield galaxy`

`# do nothing` `return`

`yield from schedule_helper`

`yield from schdule_helper`



 [28:50](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=1730s) Is a for statement just building an iterator and then calling next on it?

I think there are cases in which python tries to like find a faster way to do it like if you iterator over a range maybe it's doing something fancy underneath I don't know but from your programmer's perspective the behavior is identical to create an iterator out of this thing that you're running the for loop over and call next repeatedly ...

 [29:33](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=1773s) Is there any way to reset an iterator to its original position?

You just have to make a new one.

It might be that you're trying to write a program where you're kind of forgetting the past because maybe the stuff that you've iterated over is so big. It's like a whole video files that you can't store them all in memory at once so this idea of like resetting would require you to remember everthing you had seen before and that's exactly what you might be trying to avoid an iterator.

It's up to you. I think there might be some like build-in stuff in the python standard library to remember an iterator and kind of cycle through it but I don't know exactly what it looks like.

 [30:28](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=1828s) Do "yield from" statements have to make recursive calls?

I think it's iterative because you're unpacking a `for` loop,  john.

It happens to be that you can uh can mix together recursion and yielding. <u>If the goal of your recursion is to build uo a sequence of things</u> which is not totally unusual. 

Our first examples of recursion where like cout the number of ways that you could partition up a number using parts up to size m and then we just did a homework problem which was actually list out all the ways and so you know it's the same basic recursive structure in both cases except for counting you just return a number whereas if you're listing out all the possibilities then you have to either return a list or you have to yield yeah good question.

 [32:01](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=1921s) Can yield be used within a larger expression? 

No. because they‘re not expressions themselves. They're statements, they have to show up on their own line.

[32:46](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=1966s) Can you do more than one thing in the body of a list comprehension?

that expression could be a compound expression

`[[print(1), print(2)] for x in range(4)]`

 [33:52](https://www.youtube.com/watch?v=80JznV82Fbg&list=PL6BsET-8jgYXMKOdcoi0Hy_Gn4fuY_XzL&index=8&t=2032s) How does new content get added to an iterator after some other code has already started consuming the iterator?

```python
def read_papes(root='www.nytimes.com'):
    this_page = read_url(root)
    yield this_page
    for other_page in get_all_links(this_page):
        yield from read_pages(other_page)
```



### Disc 06: Nonlocal, Mutability, Iterators

# Objects







### HW 04: Nonlocal, Iterators