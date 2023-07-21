class Ok:
    py = [3.14]
    def __init__(self, py):
        self.ok = self.py
        Ok.py.append(3 * py)
    def my(self, eye):
        print(self.my(eye))
        return self.ok.pop()
    def __str__(self):
        return str(self.ok)[:4]


class Go(Ok):
    def my(self, help):
        return [help+3, len(Ok.py)]

oh = Go(5)
Go.py = [3, 1, 4]
oh.no = {'just': Go(9)}

"""
>>> 'z' * 3
'zzz'
>>> print(4, 5) + 1
4 5
Error
>>> oh.py
[3, 1, 4]
>>> oh.my(3) # Go(5), Go(9), [3.14, 15, 27]
[6, 3]
>>> oh.ok + oh.no['just'].ok 
[3.14, 15, 27, 3, 1, 4]
>>> oh.ok is Ok.py
True
>>> oh.no['just'].ok is Go.py
True
>>> print(oh)
[3.1
>>> Ok('go').my(5) # Go('go'), [3.14, 15, 27, 'gogogo'] infinite loop
"Error"
>>> Ok.my(oh, 5)
[8, 4]
'gogogo'
"""
