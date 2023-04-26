# Inheritance

##### attributes

Functions aren't particular to object-oriented programming, but methods are. So a methods are a function that's also a class attribute.

Fucnitons are objects. Bound methods are also objects with first argument ....

##### attributes assignment

##### inheritance

```python
class <name>(<base class>):
    <suite>
```

Two similar classes differ in their degree of specialization

The specialized class may have the same attributes as the general class, along with some special-case behavior.

```python
class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
```

##### looking up attribute names on classes

base class attributes aren't copied into subclasses!

```python
>>> ch = CheckingAccount('Tom') # calls Account.__init__
>>> ch.interest
0.01
>>> ch.deposit(20) # look up deposit, check in the ch instance, no; check in the CheckingAccount class, no; check in the Account class and get the method called deposit.
```

##### designing for inheritance

```python
class CheckingAccount(Account):
    # don't repeat what exist
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        # withdraw have been overridden, but can still accessible by Account.withdraw which look-up on base class
        return Account.withdraw(self, amount + self.withdraw_fee) # which is better than CheckingAccount.withdraw_fee which allows us to set specialized accounts for different instances
```

##### inheritance and composition

<!--composition类似于Java里面的委托吗，委托其他的类来实现某个功能，所以它可能和外面的类没有我们这里说的special case的关系，当你并不关心/不确定是否有is a关系的时候可以使用。cat and her claw。-->

```python
class Bank:
    """A bank *has accounts.*
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> johhn.balance
    10.2
    >>> to0_big_to_fail
    True
    """
    def __init__(self)
        self.accounts = []
      
    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts_append(account)
        return account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)
    
    def too_big_to_fail(self):
        return len(self.accounts) > 1
    
```

##### practice

All of the functions in this example have parent frame global.

So this structure was created by executing the first class statement.

![截屏2023-03-16 23.49.54](/Users/a/Desktop/截屏2023-03-16 23.49.54.png)

<!--you have to figure out what self refer to which does great favor-->

##### Multiple inheritance

```python
class SavingsAccount(Account):
    deposit_fee = 2
    def deposite(self, amount):
        reutrn Account.deposit(self, amount - self.deposit_fee)
        
        
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    """
    CleverBank marketing executive wants:
    - Low interest rate of 1%
    - A $1 fee for withdrawals
    - A $2 fee for deposits
    - A free dollar when you open your account
    """
    def __init__(self.account_holder):
        self.holder = account_holder
        self.balance = 1 # A free dollar!
        
>>> such_a_deal = AsSeenOnTVAccount("John")
>>> such_a_deal.balance # instance attribute
1
>>> such_a_deal.deposit(20) # SavingsAccount method
19
>>> such_a_deal.withdraw(5) # CheckingAccount method
13
```

You look at the subclass before you look at the base class.

##### complicated inheritance

But the thing to realize is that this tree is just growing exponentially at each layer, which implies that there are many, many more people in previous generations than there are now.

But that's actually not true. 100 years ago, there were many fewer people on Earth than there are now. So it can't be the case that these trees just grow wider and wider with different sets of people.

There must be some overlapping in the treee. So there's actually terminology for that sort of overlap.

![截屏2023-03-17 00.14.17](/Users/a/Desktop/截屏2023-03-17 00.14.17.png)



### QA

[00:03](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=3s) Is inheritance recommended these days?

<!--become unruly, extremist view-->

A more common belief is that inheriting methods is fine. It's inheriting attributes that's complicated because um yeah if you don't know where the attribute was originally declared then it's hard to kind of keep track of what's going on. So I see programs where yeah like functionality defined by a bunch of methods is inherited sometimes even multiple inheritances allowedd there but you just want to be careful about like having attributes defined in one place and then having a subclass that like tries to ignore some of those attributes because it's different enough that you don't want them all that gets messy pretty fast and it's usually better to just use composition instead.



yeah that sounds about right. I have to say I think I'm much more likely to use composition than inheritance that's really common.



 [01:34](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=94s) How do you evaluate b.z.z.z in the video called "Review: Attributes Lookup, Methods, & Inheritance"? 



b.z.z.z  taking the dot z of something but you don't know what it is until you compute it and to compute it you have to evaluate b.z.z .....

b is a name ..., the first z and the second z is not the same thing, they just happened to have the same name.



This is a good pedagogical example but not what your code should look like.



[04:50](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=290s) How do you evaluate a.z == b.z in the same video?

<!--Mute-->



 [08:21](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=501s) How do you refer to attributes of an object that is part of another object when not using inheritance? 



```python
class Account:
    def __init__(self, holder):
        self.holder = holder
        self.balance = 0
        
class Bank:
    def __init__(self):
        self.accounts = []
        
    def open_account(self, name):
        self.accounts.append(Account(name))
```



```python
>>> goldman = Bank()
>>> goldman.open_account('John') # we can't access account which is not in the global frame
>>> goldman
<__main__.Bank object at 0x10294c0d0>
>>> len(goldman.accounts)
1
>>> goldman.accounts[0].holder
'John'
>>> goldman.accounts[0].balance
0
>>>
```



The answer in general to your question of like when you're <u>using composition how do you access attributes of the parts</u> is often using some like <u>chain of dot expressions</u> where instead of having a name for this account. You have an expression that's like some compound expression for this account that goes in and gets part of the Goldman the bank .....



We could have a method does this instead that would have been fine but this is kind of the minimal example of how you would access some piece of composed bank. 



You can think about the account as just being as john just said <u>one level removed from you</u> instead of having a global variable that where you created the account. It's now stored in a list inside of another object so ......



<!--chain of dot expression在看ruby/rails的时候真是很长的chain-->



[11:37](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=697s) Can Account.deposit(...) be used to invoke a method even when not overriding an existing method?

```python
>>> a = Account('John')
>>> a.deposit(12)
12
>>> Account.deposit(a, 12) # inheritance when  method has been overwritten
24
```



 [13:32](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=812s) What is super() and how does it work?



```python
class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01
    
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
        # Alternatively:
        return super().withdraw(amount + self.withdraw_fee)
```



Is it weird John that you don't have to pass self when you use the super notation.

 Yeah so that's an interesting thing is the super isn't referring to the account class. It's like referring to a version of self as if account was it's class instead of checking account where it's  class so it's doing two things at once it's going and finding the account class and it's also filling in self for the withdraw method so you don't have to pass it in explicitly.

It is a lot to just like have a built-in function call with no argument and somehow it does all that magic that is what it is so you know you don't have to memorize this we don't test on.....



I would argue you probably should still do it as sort of a <u>built-in documentation</u> so that the user doesn't have to like you know scroll through your class to figure out which one. It's sort of nice thing I like about the making the explicit is you're telling somebody which one is it going to as opposed to relying on some default and then what if somebody actually comes in and puts up a draw function later on. I mean do you so sometimes <u>it's good to make things explicit even if there's a default um response you know.</u>

<!--Account.withdraw(self...) might be a better choose for it makes the relationship clearer.-->



Yeah, but one thing I whould say is like if you have

```python
class CheckingAccount(Account):
    ......
    def deposit_twice(self, amount):
        self.deposit(amount) # deposit doesn't exist in the current class but defined in the parent class, Account.
        self.deposit(amount)
        
```

you subclass can have totally new stuff in it um 

you don't really need to use any supers here or anything like that and you can trust that python will look it up for you correctly.





[17:15](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=1035s) If a class doesn't have __init__, can you pass in arguments when you construct an instance? 





[18:05](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=1085s) Do you have to call the constructor function __init__?



 [19:36](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=1176s) Why Does AsSeenOnTVAccount use the SavingsAccount deposit instead of the Account deposit?

If you're wondering whether it ever gets messy to figure out which thing happens first, the answer is definitely yes. In fact like python's now on its third version of how to resolve this question and because there were bugs in the first two so uh don't worry about it. This is beyond the scope of the course but multiple inheritance does leave lots of computer scientists scratching their heads about what's exactly going to happen which is why in generail you should try to avoid it.



 [22:15](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=1335s) Is the "Review: Attributes Lookup, Methods, & Inheritance" slide representative of what students are supposed to know for the midterm?



I think this semester we're just going to focuse more on getting things done rather than knowing exactly the mechanics but exactly the machanics of how the object system works as we've described it is part of the course so you should know it.

That's fine for life as well because you know getting things done is more important than understanding my very convoluted code.

But you know there will be cases in which you find some complicated things out there in the world and you have to trace through them so that is a useful skill to develop.



 [23:11](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=1391s) When writing a program, how do you keep track of what is an instance attribute and what's a class attribute?

This particular case where an instance attribute and a class attribute share a name does show up in practice usually when you're trying to get something to do a different behavior than was originally intended so you want to like change the way this particular instance works so that it behaves differently than whoevre wrote the class and that you know that is to be avoided when possible but sometimes when you're building off of other people's code and you can't get them to change it then you have to change it by yourself by adding an instance attribute that's got the same name as their class attribute so it's not like this never happens uh in practice but it's the rarest of the three cases so most common everything's an instance attribute second most common yeah there's class attributes out there but they have different names that the the instance attributes and then the third case is it is possible that you have a name collision and you should know what happens.



 [24:31](https://www.youtube.com/watch?v=xNeItvhnGag&list=PL6BsET-8jgYXpV7vl4Pvo25wh0FKRlecx&index=9&t=1471s) For Lab 4 Q 5, Maximum Subsequences, how do you understand the solution by tracing through it?



```python
def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
```



Well I‘d say at the outset that it's often the case that tracing through uh tree recursion is not something that humans can tolerate like it's it's just really messy sometimes um so the right answer is to shift the way in which you approach understanding uh implementation to get away from tracing and instead just treat the recursive calls as abstractions. They do the thing that they're supposed to do but how they do them is not your problem and then like you can put it together but this is not obvious or easy so um so maybe we can talk about that with a particular example.

I‘ll add one more thing to it. Tracing tree recursion is very hard you <u>have to hold a lot in your memory</u> um so one way to fix it is as he just said is to just think differently about it. It's not about tracing. It's about thinking about the fundamental nature of the functions and they just do what you want them to do and the other is to just use <u>toy examples</u>. So if you have really small inputs you can sometimes hold on to the recursion a little bit easier as opposed to something like this that has you know a ridiculous number of steps so :

If t is zero then I think we only have one choice.

I guess the last edge of n is the easiest thing to access because we can access it like that `n % 10`

I think is worth tracing. You should trace explicitly now what do you do.

You know you can think ahead you can say okay what I should do is keep the three because it's big but python doesn't know that yet. So avoid the instinct solving the problem for python and instead just like the computer work throught the details itself so you have the components now. It's your job to say well I have two options. Option one: keep last digit; 

```python
keep_last_digit = max_subseq(rest, t - 1) * 10 + last_digit
```

I think you could trace in the following way instead of looking at the body of max subsequence you should ask yourself if I pass in 12 and 1 into here, what am I going to get and you know the behavior of this thing, you know you're going to get 2 so 2 * 10 + 3 is going to give you 23. That's the degree to which it makes sense to trace is pretend that `max_subseq(rest, t - 1)` is some black box that does its thing but you don't know how it does it but you do know what its result is which is like what's the biggest digit in 12? Well, it's 2.

The other option is would be `drop_last_digit`

If you wanted to return the biggest one then:

```python
keep_last_digit = max_subseq(rest, t - 1) * 10 + last_digit # 23
drop_last_digit = max_subseq(rest, t)                       # 12
return max(keep_last_digit, drop_last_digit)                # 23
```

So at least in this example it seems like it's going to do the right thing that's the kind of tracing that I would do in a tree recursive problem and we realized that we never went back through the body of `max_subsequence` again instead we just asked ourselves what is this going to return and stop there.

So there's that big leap of faith right where you have to just trust that what you're doing is doing the right thing and by the way if you're wrong well then the code won't work and so it like that uh hold on.



### Lab 07: Object- Oriented Programming, Iterators

<!--print('vroom'), vroom; return 'vroom', 'vroom'.-->

<!--build abstraction, write your code; write your code, abstract it.-->

### Ants

<!--colony, muster, invade your territory, Irritate the bees, be vanquished, Fail to pester the airborne intruders adequately, succumb to the bees' wrath.-->

- `ants.py`: The game logic of Ants Vs. SomeBees
- `ants_gui.py`: The original GUI for Ants Vs. SomeBees
- `gui.py:` A new GUI for Ants Vs. SomeBees. Note that this doesn't work / is very buggy, but you can see the cute ants in motion here :)
- `graphics.py`: Utilities for displaying simple two-dimensional animations
- `utils.py`: Some functions to facilitate the game interface
- `ucb.py`: Utility functions for CS 61A
- `state.py`: Abstraction for gamestate for gui.py
- `assets`: A directory of images and files used by `gui.py`
- `img`: A directory of images used by `ants_gui.py`
- `ok`: The autograder
- `proj3.ok`: The `ok` configuration file
- `tests`: A directory of tests used by `ok`

more information about the autograder `ok`

```bash
python3 ok --local # do not record a backup, no information to be sent to course servers
python3 ok -q [question number] -i # test code interactively
print("DEBUG:", x) # not cause ok tests to fail with extra output.
```

<!--antagonistic, stings, elapsed, elapsed, insects-->

<!--There can be one Ant and many Bees in a single Place-->

hint:

```python
def __init__(self, armor=3):
    Ant.__init__(self, armor) # the default armor value of FireAnt is different with Ant's
```

<!--onslaught, perishes-->

# Representation

##### String representation

In python, all objects produce two string representations:

- **str** is legible to humans
- **repr** is legible to the python interpreter. (That is, it's supposed to be an expression)

##### The repr String for an Object

The **repr** function returns a Python expression (a string) that evaluates to an equal object.

```python
>>> repr(help)
'Type help() for interactive help, or help(object) for help about object.'
>>> help(repr)
 Return the canonical string representation of the object.
    
 For many object types, including most builtins, eval(repr(obj)) == obj.
```

The result of calling **repr** on a value is what Python prints in an interactive session.

```python
>>> 12e12
12000000000000.0
>>> eval(repr(12e12))
12000000000000.0
```

For some objects (e.g. compound things like functions or classes), there's no way to write down an expression that very easily <u>captures everything</u> at some object is or an expression for <u>how to create something that's equal to the original object.</u>

```python
>>> repr(min)
'<built-in function min>'
```

And this's just a human-readable description since generating a Python expression just didn't work out.

##### The str String for an Object

```python
>>> from fractions import Fraction
>>> half = Fraction(1, 2)
>>> half
Fraction(1, 2)
>>> repr(half)
'Fraction(1, 2)'
>>> str(half) # Python calls str when it prints
'1/2'
>>> print(half)
1/2
>>> eval(repr(half))
Fraction(1, 2)
>>> eval(str(half))
0.5
```

```python
>>> s = "Hello, World"
>>> s
'Hello, World'
>>> print(repr(s))
'Hello, World'
>>> print(s)
Hello, World
>>> print(str(s))
Hello, World
>>> str(s)
'Hello, World'
>>> repr(s)
"'Hello, World'"
>>> eval(repr(s))
'Hello, World'
>>> repr(repr(repr(s)))
'\'"\\\'Hello, World\\\'"\''
>>> eval(eval(eval(repr(repr(repr(s))))))
'Hello, World'
>>> eval(s) # Hello, World is not a valid python expression
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'Hello' is not defined
>>> eval(repr(s))
'Hello, World'
>>> eval("'Hello, World'")
'Hello, World'
```

##### polymorphic functions

A function that applies to many (poly) different forms (morph) of data.

asks its argument to what to do. In python, using a special method name which corresponds to a built-in function.

**repr** invokes `__repr__` on its argument.

```python
>>> half.__repr__() # instance attribute
'Fraction(1, 2)'
```

 **str** invokes  `__str__` on its argument.

```python
>>> half.__str__()
'1/2'
```

##### implementing repr and str

The behavior of **repr** is slightly more complicated than invoking `__repr__` on its arguments:

An instance attribute called `__repr__`is ignored! <!--would instance attribute be slightly different with class attribute.--> Only class attributes are found.

```python
def repr(x):
    return type(x).__repr__(x) # class attribute
```

If no `__str__`attribute is found, uses **repr** string. <!--only if you explicitly make them different that they differ.--> **str** is a class, not a function. So when you're calling str,  you're really calling the constructor for the built-in string type called str.

<!--nuances-->

```python
class Bear:
    """A Bear."""
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'this bear'
        
    def __repr__(self):
        return 'Bear()'
      
    def __str__(self):
        return 'a bear'
      
oski = Bear()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())

def repr(x):
    return type(x).__repr_(x)
  
def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
      else:
        return repr(x)
"""    
a bear
a bear
Bear()
this bear
oski
"""
```

**Interfaces**

So when I talked about object-oriented programming in the first place, I said that <u>the central to this metaphor</u> was that <u>objects would pass messages to each other</u> and that's how they would interact.

**Message passing**: Objects interact by looking up attributes on each other (passing messages)

Passing messages is the metaphor. <u>Looking up attributes</u> is what we actually do, in order to pass messages around. 

Now, the attibutes look-up rules are designed in a special way. They allow <u>different data types</u> to respond to the <u>same message</u> just by having the <u>same attribute name.</u>

And a **shared message**<!--same message-->, an attribute name that exists on many different classes and elicits the same behavior from those different classes, is a powerful method of abstraction.

<!--我觉得他看待interface的视角和我习惯的不一样。I means code reusing.-->

An interface is a set of shared messages and some specification that tells you what they're supposed to do, what they mean.

`__repr__`, `__str__` implement an interface for producing string representations.

##### special method names in python

Built-in behavior, `__<method_name>__`

`__init__`: constructed

`__repr__`: display an object as a Python expression

`__add__`: add one object to another

`__bool__`: convert an object to True or False

`__float__`: convert an object to a float (real number)

```python
>>> zero, one, two = 0, 1, 2
>>> one + two
3
>>> bool(zero), bool(one)
(False, True)

# same behavior using methods
>>> zero, one, two = 0, 1, 2
>>> one.__add__(two)
3
>>> zero.__bool__(), one.__bool__()
(False, True)
```

Using an interface in order to allow user-defined objects to interact with the built-in systems within Python. So Python is very extensible.

```python
>>> Ratio(1, 3) + Ratio(1, 6)
Ratio(1, 2)
>>> Ratio(1, 3).__add__(Ratio(1, 6))
Ratio(1, 2)
>>> Ratio(1, 6).__radd__(Ratio(1, 3)) # reverse
Ratio(1, 2)
```

<!--commutative-->

http://getpython3.com/diveintopython3/special-method-names.html

http://docs.python.org/py3k/reference/datamodel.html#special-method-names

```python
class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d
        
    def __repr(self):
        return 'Ratio{0}, {1}'.format(self.number, self.denom)
      
    def __str__(self):
        return '{0}/{1}'.format(self.number, self.denom)
      
    # 参数未必是同一种类型，函数的返回值也未必是同一种类型
    def __add__(self, other):
        # type dispatching
        if isinstance(other, int):
            n = self.number + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.number * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other # type coercion
        g = gcd(n, d)
        return Ratio(n//g, d//g)
      
    __radd__ = __add__ # 1 + Ratio(1, 3)
    
    def __float__(self):
        return self.numer/self.denom
      
def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n-d) # the greatest common divisor of n and d is the greatest common divisor of min(n, d) and abs(n-d)
    return n
```

These are twoo strategies that people use in order to have different classes interact.  **type dispatching**, inspect the type of an argument to decide what to do. **type coercion**, take an object of one type convert it into another type, in order to be able to combine it with some other value.

```python
class Kangaroo:
    """
    >>> k = Kangaroo()
    >>> print(k)
    >>> k.put_in_pouch("ball")
    >>> print(k)
    >>> k.put_in_pouch("hammer")
    >>> print(k)
    >>> k.put_in_pouch("ball")
    print(k)
    """
    def __init__(self):
        self.pouch_contents = []
        
    def put_in_pouch(self, s):
        for i in range(len(self.pouch_contents)):
            if (self.pouch_contents[i] == x):
                print('already in pouch')
                return
        self.pouch_contents.append(s)
            
    def __str__(self):
        if (len(self.pouch_contents) == 0) :
            return "The Kangaroo's pouch is empty."
        else:
            return "The Kangaroo' pouch contains: " + \
              str(self.pouch_contents)
```



### QA

[00:02](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=2s) Why does Prof. Farid not use object-oriented programming in his day-to-day programming?

I have to say except for like commercial things I don't think I've ever done object oriented like when I just code internally even when we build big things. Is that some a crappy programmer or that is there some obstacle uh still like I never build a lot of classes and do all the things that I teach. what's wrong.

well um object-oriented programming shines in this particular scenario when a bunch of stuff is changing. yeah.

and a lot of code that gets written these days especially data processing code doesn't really have like mutation going on. it doesn't have changing state over time or you're like tracking a lot of stuff. This happens more often in like software that's got a user interaction cycle or something like that.  So yeah if you're doing much data processing workflows then it just doesn't show up as much yeah

That's a good point.That is an interesting way I hadn't thought about it that way but I like that.

 [01:03](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=63s) What does it mean that str is a class and not a function?

```python
>>> str
<class 'str'>
>>> abs(2)
2
>>> str(2) # constructor creates an instance of str.
'2'
```

[02:12](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=132s) In the "Polymorphic Functions" video, repr and str are redefined after calls to print. Is that a mistake?

So anyway you're right that if you print before you make changes then those changes obviously won't be reflected.

 [02:58](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=178s) How does addition interact with user-defined classes using *_add_* and __radd__?

`x + y`

- if x has a user-defined class?
  - if it has an add method?
- whether y is a user defined class?
  - if it has an radd method?
- use the built -in edition that it has which basically only works for the built-in classes like ant and float and str
- if that doesn't apply then  you'll see an error.

Order matters.

 [05:01](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=301s) Could you use "in" instead of "for" to check the contents of a Kangaroo's pouch?



 [05:35](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=335s) Is isinstance(a, B) the same as type(a) == B?

```python
class A:
    """Base"""
class B(A):
    """Subclass"""
```

`isinstance` asks is a an instance of B or any of its subclasses.

You're future proofing your code by saying is it an instance of a Kangaroo if somebody comes up with this special subclass of like a short kangaroo, your code's still going to run correctly.

 [06:49](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=409s) What's the difference between repr and `__repr__` ?

```python
>>> repr([1, 2])
'[1, 2]'
>>> type([1, 2]).__repr__
```

 [09:12](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=552s) Does every class define `__repr__`? 

has some default behavior `<__main__.A object at 0x....>`

But it's not very useful. It's just like a placeholder.

[09:57](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=597s) How would you print all the paths from the root of a tree to one of its leaves?

```python
from tree import *

def print_all_paths(t):
    """Print all the paths from the root to a leaf.
    >>> t = tree(1, [tree(2, [tree(3)]), tree(4)])
    >>> print_all_paths(t)
    [1, 2, 3]
    [1, 4]
    """
    for path in all_paths(t):
        print(path)
        
        
def all_paths(t):
    if is_leaf(t):
        yield t
    else:
        for b in branches(t):
            for path in all_paths(b): # path might be [2, 3]
                yield [label(t)] + path # yielding [1, 2, 3]
```

A path comes from by finding a path from uh the root of the branch all the way to a leaf and then putting the current label at the front. That's like a recursive way to think about a path is that a path has the first thing and then it's got the rest of the elements in the path are a path in a smaller tree. A tree that starts at a branch. So one way to do this is to say that for every branch you want get all the path in that branch like here's branch`tree(2, [tree(3)])` and a path throught that branch would be [2, 3] but we want [1, 2, 3]. so if we go throught all the paths in the branch then what we want to return here is not just [2, 3], we want return [1, 2, 3] but there might be multiple of them so I'm going to write it as a generator function we can change it later if you want but what we uh yield here is [1, 2, 3].

John had this beautiful recursive definition in there he said what is a path. It's one if we start at the tree that he's just described up  top with the path of everything below.  That one statement is what wrote your function for you.

 [15:18](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=918s) How do you solve Fall 2015 Midterm 2 Question 3(a): d-k-complete trees?   

```python
def complete(t, d, k):
    """Return whether t is d-k-complete.
    A tree is d-k-complete if every node at a depth less than d has exactly k branches and every node at depth d is a leaf.
    Notes:
    The depth of a node is the number of steps from the root; the root node has depth 0.
    The built-in all function takes a sequence and returns whether all elements are true values: all([1, 2]) is True but all([0, 1]) is False.
    >>> complete(tree(1), 0, 5)
    True
    >>> u = tree(1, [tree(1), tree(1), tree(1)])
    >>> [ complete(u, 1, 3)  ,  complete(u, 1, 2)  ,  complete(u, 2, 3) ]
    [True, False, False]
    >>> complete(tree(1, [u, u, u]), 2, 3)
    True
    """
    if not t.branches(t):
        return d == 0
    bs = ([complete(b, d - 1, k) for b in t.branchest])
    return len(branches(t)) == k and all(bs)
```

[23:31](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=1411s) Why is it the case that repr(x) could be different from `x.__repr__()`?

```python
class Bear:
    "Nothing here"

oski = Bear()

def f():
    return 'gp bears'
  
oski.__repr__ = f

print(oski.__repr())
print(repr(oski))
```

<!--esoteric-->

Otherwise one thing python could have done to avoid this weirdness it says you can't define functions with double underscores before and after the name. Right that's what's basically happening here you're making something look like it's a member function using that default nomenclature but there's no protection of that.

So sometimes when you make something as flexible as python then uh then instructors find weird ways to abuse it and that's I guess what I've done here but uh yeah so so anyway  what you're supposed to learn is how wrapper methods like how you define wrapper methods within a class uh it happens to be that you can't put them on the instance or they won't work.

 [25:52](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=1552s) When you print an object with a *_repr_* method, why don't you see the str-string instead of the repr-string?

the default str is to just do whatever repr would do. That's just a fact about python.

 [27:08](https://www.youtube.com/watch?v=A_ZqNDuDW2A&list=PL6BsET-8jgYVDQ8Hwjl2jnxhOiLB7434j&index=6&t=1628s) How do *_add_* and *_radd_* relate? Are they always equal?

```python
class Rational:
    def __init__(self, n, d):
        self.n, self.d = n, d
        
    def __add__(self, other): # x + 3; other is 3
        return Rational(self.n + other * self.d, self.d)
      
    __radd__ = __add__
    
    # def __radd__(self, other); 3 + x; other is 3
    #     return Rational(self.n + other * self.d, self.d)
    
    def __repr__(self):
        return 'Rationl(' + str(self.n) + ', ' + str(self.d) + ')'
```



### Disc 07: Object- Oriented Programming

<!--python _init_ is not required for subclass oppose to Java.-->

# composition

##### linked list structure

A linked list is either empty or a first value and the rest of the linked list.

Link(3, Link(4, Link(5, Link.empty)))

```python
class Link:
    empty = () # some zero-length sequence (because that's what it is)
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
```

`help(isinstance)`: Return whether an object is an instance of a class or of a subclass.

##### example: range, map, and filter for linked lists

```python
square, odd = lambda x: x * x, lambda x: x % 2 == 1
list(map(square, filter(odd, range(1, 6)))) # [1, 9, 25]
map_link(square, filter_link(odd, range_link(1, 6))) # Link(1, Link(9, Link(25)))

class Link:
    ...
    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
      
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
        
def range_link(start, end):
    """
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))
      
def map_link(f, s):
    """
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))
    
def filter_link(f, s):
    """
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    filter_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filter_rest)
    else:
        return filter_rest
```

`python3 -m doctest ex.py`

<!--momentarily-->

##### linked lists can change

```python
>>> s = Link(1, Link(2, Link(3)))
>>> s.first = 5
>>> t = s.rest
>>> t.rest = s
>>> s.first
5
>>> s.rest.rest.rest.rest.rest.first
2
```

##### adding to an ordered list

```python
def add(s, v):
    """Add v to an ordered list s with no repeats, returning modified s, and make sure that s remains ordered.
    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5)))
    >>> add(s, 3)
    Link(1, Link(3, Link(5)))
    >>> add(s, 4)
    Link(1, Link(3, Link(4, Link(5)))
    >>> add(s, 6)
    Link(1, Link(3, Link(5, Link(6)))
    """
    asserts s is not List.empty # werid
    if s.first > v:
        s.first, s.rest = v , Link(s.first, s.rest)
    elif s.first < v and empty(s.rest):
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s   
    #if s is List.empty:
    #    return Link(v)
    #if v < s.first:
    #    return Link(v, s)
    #return Link(s.first, add(s.rest, v))
```

##### tree abstraction (review)

​			3

​	1				2

0 	1		1		1

​						0		1

A: **recursive description** (wooden trees):

- A **tree** has a **root label** and a list of **branches**
- each **branch** is a **tree**
- a **tree** with zero **branches** is called a **leaf**
- a **tree** starts at the **root**

B: **relative description** (family trees):

- Each location in a tree is called a **node**
- each **node** has a **label** that can be any value
- one node can be the **parent**/**child** of another
- the top node is the **root node**

*People often refer to labels by their location: "each parent is the sum of its children"*

```python
class Tree:
    """A tree is a label and a list of branches"""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)
```

Object-oriented programming / data abstraction <!--区别不大，class可以用dot notation，还是方便一些-->

<!--The main difference, aside from syntax, is that tree objects are mutable.  The tree objects is mutable!!! I didn't realize that-->

```python
class Tree:
    ...
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)
      
    def __str__(self):
        return '\n'.join(self.indented())
      
    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line) # add '  ' to the subtree. similar to “print_all_paths” which adds label to the paths of all branches.
        return [str(self.label)] + lines
```

```python
def fib_tree(n):
    """A Fibonacci tree."""
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])
    
def leaves(t):
    """Return a list of leaf labels in Tree T."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves
        
def height(t):
    """Return the number of transitions in the longest path in T."""
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])
```

##### Example: pruning trees

*pruning*: removing subtree from a tree

```python
def prune(t, n):
    """Prune all sub_trees whose label is n."""
    t.branches = [b for b in t.branches if b.label != n] # you can change the old branches but we make the same effect here.
    for b in t.branches:
        prune(b, n) # no return since we want to change the old tree
```

### QA

[00:03](https://www.youtube.com/watch?v=X6pi6EOBEis&list=PL6BsET-8jgYWRdk5tJgOMfZZ-gyt5FaBn&index=8&t=3s) Are linked lists used a lot, or do most people just use lists?

I've always taught linked lists. I think they're really great. Um, in in at google did you see people really using them or was it just you know we just use a list that's sort of easier.

I think that there are many more applications where you use a list than a linked list. 

Yeah that was my sense because it's there's clearly a benefit but it's not clear that it's outweighed by the you know the hassle of having to implement everything.

Yeah and I think um when there's a lot of mutation that's when it can matter because you can kind of stick something in the middle of a linked list and so you know definitely if we didn't have them then like something at google woouldn't work like it's supposed to work you know it's a necessay component but it doesn't show up all that often.

It doesn't remind me if I'm wrong python does this cool thing when you allocate memory for a list where it actually gives you more memory than you need so that as you're expanding it it's not having to sort of move things around in memory. Did I get that right? 

Yeah I think that's right they round up to the next power two or something like that. 

That righit it's always powers so actually it's a little bit better than constantly having to move things around when you're inserting in the list.

But even when you insert like you don't have to allocate new memory but you. do have to copy everything over to make room so still llinked lists are kind of nice.

oh that's yeah. that's true. By the way, beck in the day when we programmed in c you had to you had to every time you want to create a data structure you had to actually go in and allocate the memory for it and then you allocate the memory for it so that memory management is, was brutal.

Yeah that's how I started in my first computer science class and uh also when you did it wrong it didn't really tell you where you were and it was....

It was deterministic because sometimes you would run in the code would be fine and then sometimes you run the questions. I recently had to implement uh an algorithm and speak that it had to run really really fast in those four dimensional matrices and it took me like a week just to get the memory management right. Just don't write memory management yeah.

yeah no my initial reaction having to deal with memory management was like why does ever anyone take computer science courses is awful so you know I think learning computer science is still frustrating but in different ways.

now we sound like old guys but back in my day I had to allocate memeory. 

Exactly.



You could have made a linked list just a tree where you're only allowed to have one branch.

 

 [02:48](https://www.youtube.com/watch?v=X6pi6EOBEis&list=PL6BsET-8jgYWRdk5tJgOMfZZ-gyt5FaBn&index=8&t=168s) HW4 Q4: Permutations

```python
def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    e = seq[0]
    if len(seq) == 1:
        yield [e]
    else:
        for p in permutations(seq[1:]):
            new_range = range(len(p) + 1)
            for pos in new_range:
                # insert the first element of seq into array p at the index pos
                # pos = 0: [20, 30] -> [10, 20, 30];
                # pos = 1: [20, 30] -> [20, 10, 30];
                yield [p[i] if i < pos else p[i - 1] if i > pos else e for i in new_range]
```

```python
def permutation(s):
    """yield permutations of list s.
    >>> list(permutation([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if len(s) == 0
        yield []
    for i in range(len(s)):
        start = s[i] # 2
        rest = [s[j] for j in range(len(s)) if j != i] # [1, 3]
        # rest = s[:i] + s[i+1:]
        for rest_permutation in permutation(rest):
            yield [start] + rest_permutation # [2, 1, 3] or [2, 3, 1]
```

 [08:04](https://www.youtube.com/watch?v=X6pi6EOBEis&list=PL6BsET-8jgYWRdk5tJgOMfZZ-gyt5FaBn&index=8&t=484s) Are nested for loops necessary for permutations?

I think that nested loop is just inherent to this problem so there isn't really a way to get around it. I means you could use `yield from [[start] + rest_permutation for rest_permutation in permutation(rest)]` insead and try to do this all in one line if you really want to.But it's not like you've gotten rid of the for loop.

There's one loop that we agree we have to peel off the first element in the list. And the second loop has to permute everything that's left.

[`[1, 2, 3], [1, 3, 2]`, ` [2, 1, 3], [2, 3, 1]`, ` [3, 1, 2], [3, 2, 1]`]

[`[1, 2, 3], [2, 1, 3], [2, 3, 1]`, `[1, 3, 2], [3, 1, 2], [3, 2, 1]`]

 [09:13](https://www.youtube.com/watch?v=X6pi6EOBEis&list=PL6BsET-8jgYWRdk5tJgOMfZZ-gyt5FaBn&index=8&t=553s) Can permutations be solved by insertion? What can go wrong?

```python
if len(s) == 0
    yield []
    # yield '' # for string
else:
    first = s[0] # 1
		rest = s[1:] # [2, 3]
		for rest_permutation in permutation(rest): # [2, 3], [3, 2]
    		for i in range(len(s)):
        		# rest.insert(i, first) # insert is mutation operation you will get wrong answer.
        		result = list(rest_permutation)
        		result.insert(i, first)
        		yield result
        		# yield rest_permutation[:i] + [first] + rest_permutation[i:]
            # yield rest_permutation[:i] + first + rest_permutation[i:] # for string. you cann't insert into string apparently since it's immutable.
```

 [16:38](https://www.youtube.com/watch?v=X6pi6EOBEis&list=PL6BsET-8jgYWRdk5tJgOMfZZ-gyt5FaBn&index=8&t=998s) Is a circular linked list ever a good idea? 

You might want to represent some repeating deciaml of like you know what happens when you 1 / 7. well actaully this should go on forever and we could represent that as a circular linked list and then we .....

Circular lists. one of the benefits is as you're traversing a list, you know there's something nice that when you get to the last element you can get back to the first element. 

we could have had some notion of wrapping around and one way to do that is what's called a sentinel and you put a special node at the front of the list that indicates that it's not a data field. It's sentinel so you put something in the data field that specifies this is not data. It's showing you that at the beginning of the list and then when you start going through and you wrap back up to the sentinel. You know you've wrapped around so then the print statement could have said okay keep printing until I loop back and then have some notation to say this will keep going like `...`. You do have to put um precautions in place and circular linked lists are actually a common data type.

[20:05](https://www.youtube.com/watch?v=X6pi6EOBEis&list=PL6BsET-8jgYWRdk5tJgOMfZZ-gyt5FaBn&index=8&t=1205s) Discussion 5 Q 1.3 square_tree

```python
def square_tree(t):
    """Return a tree with the square of every element in t. Assume that every item is a number.
    >>> numbers = tree(1,
    >>> print_tree(square_tree(numbers))
    """
    return tree(label(t)**2, [square_tree(b) for b in branches(t)])
```

 [24:40](https://www.youtube.com/watch?v=X6pi6EOBEis&list=PL6BsET-8jgYWRdk5tJgOMfZZ-gyt5FaBn&index=8&t=1480s) Spring 2019 MT2 Q1

```python
items, n = [], 2
class Airpods:
    cost, k = 200, 0
    f = lambda self: print(self)
    def __init__(self):
        Airpods.k += 1
        Airpods.f(self)
        items.extend([self])
    def __repr__(self):
        return (Airpods.k < 2 and "lonely") or "pair"
class TwoAirpods(Airpods):
    def __init__(self):
        self.k = 2
        Airpods.__init__(self)
        Airpods.__init__(self)
def discount(a):
    a.cost //= 2
def u(w, u):
    return [print(u) for u in [w, u]]
discount(Airpods)

"""
>>> pow(10, 2)
100
>>> print(Link(2, Link(3)))
<2, 3>
>>> TwoAirpods.cost
100
>>> lost = Airpods()
lonely
>>> willbelost = TwoAirpods()
pair
pair
>>> str(lost)
'pair'
>>> [item.k for item in items]
[3, 2, 2]
>>> u(lost, willbelost)
pair
pair
[None, None]
"""
```

 [33:54](https://www.youtube.com/watch?v=X6pi6EOBEis&list=PL6BsET-8jgYWRdk5tJgOMfZZ-gyt5FaBn&index=8&t=2034s) Spring 2015 MT2 Q4(b)

```python
def decrypt(s, d):
    """List all possible decoded strings of s.
    Returns a list of all possible ways in which s can be decoded by splitting it into secret codes and separating the corresponding words by spaces.
    >>> codes = {
    ...     'alan': 'spooky',
    ...     'al': 'drink',
    ...     'antu': 'your',
    ...     'turing': 'ghosts',
    ...     'tur': 'scary',
    ...     'ing': 'skeletons',
    ...     'ring': 'ovaltine'
    ... }
    >>> decrypt('alanturing', codes)
    ['drink your ovaltine', 'spooky ghosts', 'spooky scary skeletons']
    """
    if s == '':
        return []
    message = []
    if s in d:
        message.append(d[s])
    for k in range(1, len(s)-1): # neither of first and suffix is empty
        first, suffix = s[:k], s[k:]
        if first in d:
            for rest in decrypt(suffix, d):
                messages.append(d[first] + ' ' + rest)  
    return message
```

You know as long as you treat your recursive call as a functional abstraction then maybe it's just not so bad that it happens to be in a for statement as long as you know like oh I have a way of taking the rest of the string and decrypting that.  I guess what we'll do is we'll go throught all the prefixes of the string that match something in codes and then we'll have the rest of the string that is after the part that we match so if we match the .... <!--simple example-->

### HW 05: Object-Oriented Programming, Linked Lists, Trees