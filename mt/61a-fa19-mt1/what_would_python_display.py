def mint(y):
    return print(-2)

def snooze(e, f):
    if e and f():
        print(e)
    if e or f():
        print(f)
    if not e:
        print('naughty')


def lose():
    return -1


def alarm():
    print('Midterm')
    1 / 0
    print('Time')

def sim(b, a):
    while a > 1:
        def sc(ar):
            a=b+4
            return b
        a, b = a // 2, b - a
        print(a)
    print(sc(b - 1), a)

pumbaa = lambda f: lambda x: f(f(x))
pumbaa = pumbaa(pumbaa)
rafiki = 1
timon = lambda y: y + rafiki
rafiki = -1

"""
>>> pow(10, 2)
100
>>> print(4, 5) + 1
4 5
Error
>>> print(mint(print))
-2
None
>>> print(snooze(1, lose))
1
Function
None
>>> snooze(print(1), alarm)
1
Midterm
Error
>>> sim(3, 3)
1
0 1
>>> pumbaa(timon)(5)
1

timon = lambda y: y - 1
pumbaa(timon)(5) = (lambda x: λ(λ(x)))(timon)(5) = λ(λ(timon))(5)
= λ(lambda x: timon(timon(x)))(5) = (lambda x : (lambda x : (timon(timon(x))))(lambda x : (timon(timon(x)))))(5) = 5 - 1 - 1 - 1 - 1 = 1

"""
