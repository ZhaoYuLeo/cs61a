from Link import *

class Party:
    guests = Link.empty
 
    def __init__(self, time):
        Party.guests = Link(time+1, Party.guests)
 
    def attend(self):
        self.guests.rest = Link(self.guests.rest)
        return self.guests

class Costume(Party):
    def __init__(self, bow, tie):
        Party.guests.rest = Link(bow)
        self.ie = Link(self)

    def attend(self):
        print(repr(self.ie))
        Party.attend = lambda self: Party(9).guests

    def __repr__(self):
        print('Nice')
        return 'Costume'

"""
>>> Link(1, Link.empty)
Link(1)
>>> Link(1, Link(2))
Link(1, Link(2))
>>> Party(1).guests
Link(2)
>>> Party(3).attend()
Link(4, Link(Link(2)))
>>> Costume(5, 6).attend()
Nice
Link('Costume')
>>> Party(7).attend()
Link(10, Link(8, Link(4, Link(5))))
"""
