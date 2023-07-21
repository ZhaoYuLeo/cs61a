def f(it):
    it.append(it[1]())


def b(it):
    def steps():
        nonlocal it
        it = fit[0]
        return fit.pop()
    return steps

fit = [1, [2]]

bit = [fit, b(fit[1])]
f(bit)


"""
Global frame
f       -> func f(it) [parent=Global]
b       -> func b(it) [parent=Global]
fit     -> [1, ->[2]]
bit     -> [-> fit, ]

f1: b [parent=Global]
it      -> points to 
steps   -> func steps [parent=f1]
Return Value    -> points to func steps in f1 frame
"""




a = [1, 1]

b = [1, 1]

c = a + [b]

d = c[1:2]

while a:
    b.extend([[a.pop()]])
    d, b = b, d
a = b

b[2][0], d = c, b[2]


"""
Global frame
a   -> [1, 1]
b   -> [1, 1]
c   -> [1, 1, -> b]
d   -> [1]

Global frame
a   -> [1] => -> [] => -> b
b   -> [1] => [1, 1, -> [1]]
c   -> [1, 1, -> b]
d   -> [1, 1, -> [1]] => [1, -> [1]]

Global frame
a   -> b
b   -> [1, 1, ->[-> c]]
c   -> [1, 1, -> b]
d   -> [-> b[2]]

a → |1|1| |
b ↑↑     ┕------┓
   ┗-----┒      ↓
c → |1|1| |    | |
  ↑            |↑
  ┗------------┛|
d --------------┛
"""
