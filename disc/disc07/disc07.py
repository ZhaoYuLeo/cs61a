# 1 Object Oriented Programming


## 1.1

"""
>>> callahan = Professor("Callahan")
>>> elle = Student("Elle", callahan)
There are now 1 students
>>> elle.visit_office_hours(callahan)
Thanks, Callahan
>>> elle.visit_office_hours(Professor("Paulette"))
Thanks, Paulette
>>> elle.understanding
2
>>> [name for name in callahan.students]
['Elle']
>>> x = Student("Vivian", Professor("Stromwell")).name
There are now 2 students
>>> x
'Vivian'
>>> [name for name in callahan.students]
['Elle']
"""

class Student:
    students = 0 # this is a class attribute

    def __init__(self, name, staff):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


## 1.2

class MinList:
    """A list that can only pop the smallest element """
    def __init__(self):
        self.items = []
        self.size = 0
    
    def append(self, item):
        """Appends an item to the MinList >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
        self.size += 1
    
    def pop(self):
        """ Removes and returns the smallest item from the MinList >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        if self.size < 1:
            print("No element to pop")
            return
        # smallest = min(self.items)
        # self.items.remove(smallest)
        # self.size -= 1
        # return smallest
        
        smallest_index = 0
        for id, i in enumerate(self.items):
            if i < self.items[smallest_index]:
                smallest_index = id
        self.size -= 1
        return self.items.pop(smallest_index)


## 1.3


class Email:
    """Every email object has 3 instance attributes: the message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """Each Server has an instance attribute clients, which is a dictionary that associates client names with client objects.
    """
    def __init__(self):
        self.clients = {}
    
    def send(self, email):
        """Take an email and put it in the inbox of the client it is addressed to.
        """
    
    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them to the clients instance attribute.
        """
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is used for addressing emails to the client), server
    (which is used to send emails out to other clients), and inbox (a list of all emails the client has received).
    """

    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server
    
    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client.
        """
        mail = Email(msg, self.name, recipient_name)
        self.server.send(mail)

    
    def receive(self, email):
        """Take an email and add it to the inbox of this client.
        """
        self.inbox.append(email)

# 2 Inheritance


## 2.1

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
  
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):
    # Because Dog inherits from Pet, we didn't have to redefine __init__ or eat.
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives
    
    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + " says meow!")
    
    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive' becomes False. If this is called after lives has reached zero, print out that the cat has no more lives to lose.
        """
        if self.lives == 0:
            print('The cat has no more lives to lose')
            self.is_alive = False
            return
        self.lives -= 1


## 2.2

class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        # not necessary, you don't need it since nothing new
        super().__init__(name, owner, lives)
    
    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        super().talk()
        super().talk()
    
    def __repr__(self):
        """The interpreter-readable representation of a NoisyCat
        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoisyCat('Muffin', 'Catherine')
        """
        return "NoisyCat('{}', '{}')".format(self.name, self.owner)
