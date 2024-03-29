class Plant:
    k = 1
    kind = "green"

    def __init__(self):
        self.k = Plant.k
        Plant.k = self.k + 1
        if self.k > 3:
            Plant.name = lambda t: "tree"
            Plant.k = 6

    def name(self):
        return kind

    def __repr__(self):
        s = self.name() + " "
        return s + str(self.k)


class Flower(Plant):
    kind = "pretty"

    def __repr__(self):
        s = self.smell() + " "
        return s + Plant.__repr__(self)

    def smell(self):
        return "bad"

class Rose(Flower):
    def name(self):
        return "rose"

    def smell(self):
        return "nice"

class Garden:
    def __init__(self, kind):
        self.name = kind
        self.smell = kind().smell

    def smell(self):
        return self.name.kind

f1 = Flower()
f2 = Flower()


"""
>>> [2, 3]
[2, 3]
>>> f1.name()
'pretty' # Wrong: NameError: name 'kind' is not defined
>>> f1.k
1
>>> Plant().k
3
>>> Rose.k
4
>>> Plant()
tree 4
>>> Rose()
nice rose 6
>>> Garden(Flower).smell()
'bad' # Attention: smell function of the new object was changed into Flower().smell
>>> Garden(Flower).name()
bad tree 6 # Attention: name is class Flower. name() is print out Flower()
"""
