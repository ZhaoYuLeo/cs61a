class Version:
    """A version of a string after an edit.

    >>> s = Version('No power?', Delete(3, 6))
    >>> print(Version(s, Insert(3, 'class!')))
    No class!
    >>> t = Version('Beary', Insert(4, 'kele'))
    >>> print(t)
    Bearkeley
    >>> print(Version(t, Delete(2, 1)))
    Berkeley
    >>> print(Version(t, Delete(4, 5)))
    Bear
    """
    def __init__(self, previous, edit):
        self.previous, self.edit = previous, edit
        

    def __str__(self):
        return self.edit.apply(str(self.previous))


class Edit:
    def __init__(self, i, c):
        self.i, self.c = i, c


class Insert(Edit):
    def apply(self, t):
        return  t[:self.i] + self.c + t[self.i:]



class Delete(Edit):
    def apply(self, t):
        return t[:self.i] + t[self.i + self.c:]


