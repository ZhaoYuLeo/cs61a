# Whenever the interpreter would report an error, write Error.
# You should include any lines displayed before an error. 
# Reminder: The interactive interpreter displays the repr string
# of the value of a successfully evaluated expression, unless it is None.

class Worker:
    greeting = 'Sir'
    def __init__(self):
        self.elf = Worker
    def work(self):
        return self.greeting + ', I work'
    def __repr__(self):
        return Bourgeoisie.greeting
class Bourgeoisie(Worker):
    greeting = 'Peon'
    def work(self):
        print(Worker.work(self))
        return 'My job is to gather wealth'
class Proletariat(Worker):
    greeting = 'Comrade'
    def work(self, other):
        other.greeting = self.greeting + ' ' + other.greeting
        other.work() # for revolution
        return other
jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'

"""
>>> 5*5
25
>>> 1/0
Error
>>> Worker().work()
'Sir, I work'
>>> jack
Peon
>>> jack.work()
'Maam, I work'
>>> john.work()[10:]
Peon, I work
'to gather wealth'
>>> Proletariat().work(john)
Comrade Peon, I work
Peon
>>> john.elf.work(john)
'Comrade Peon, I work'
"""
