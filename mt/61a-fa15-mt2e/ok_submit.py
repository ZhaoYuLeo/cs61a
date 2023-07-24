from operator import add

class Ok:
    py = [31, 41, 59, 26, 53]
    def __init__(self):
        self.ie = self.py.pop()
    def why(self, eye):
        print(self.why(eye))
        return self.ok.py
    def __str__(self):
        return str(self.ie)


class Go(Ok):
    def __init__(self, py):
        self.ie = py
        self.ok = Ok()
    def why(self, help):
        return [help + 3, Ok.py.pop()]

oh = Go('no')
Go.py = [3.14]


"""
>>> 'z' * 3
'zzz'
>>> print(4, 5) + 1
4 5
Error
>>> oh.py
[3.14]
>>> oh.why(3)
[6, 26]
>>> print(oh, oh.ok)
no 53
>>> add(Ok.py[1:], Ok().py[1:])
[41, 59, 41]
>>> Ok.why(oh, 5)
oh.why(5)
[8, 41]
[31]
>>> Ok().why(5)
RecursionError: maximum recursion depth exceeded
"""
