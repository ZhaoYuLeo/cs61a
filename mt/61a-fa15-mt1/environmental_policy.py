def the(donald):
    return donald + 5

def clin(ton):
    def the(race):
        return donald + 6
    def ton(ga):
        donald = ga - 1
        return the(4) - 3
    return ton

donald, duck = 2, clin(the)
duck = duck(8)


"""
Global frame
the     -> func the(donald) [parent=Global]
clin    -> func clin(ton) [parent=Global]
donald  2
duck    -> points to func ton in f1 frame changed to 5

f1: clin [parent=Global]
ton     -> func ton(ga) [parent=f1] # attention, ton is in front of the
the     -> func the(race) [parent=f1]
Return Value -> points to the func ton in f1 frame

f2: ton [parent=f1] # attention, intrinsic name of function, is ton not duck
ga      8
donald  7
Return Value 5

f3: the [parent=f1]
race    4
Return Value 8
"""


def inside(out):
    anger = lambda fear: fear(disgust)
    fear = lambda disgust: anger(out)
    disgust = 3
    fear(5)

fear, disgust = 2, 4
inside(lambda fear: fear + disgust)


"""
Global frame
inside  -> func inside(out) [parent=Global]
fear    2
disgust 4
        -> func λ(fear) <line=46> [parent=Global]

f1: inside [parent=Global]
out     -> points to the λ(fear) <line=46> in global frame
anger   -> func λ(fear) <line=40> [parent=f1]
fear    -> func λ(disgust) <line=41> [parent=f1]
disgust 3 
Return Value: None 

f2: λ(disgust) <line=41> [parent=f1]
disgust 5
Return Value: 7 

f3: λ(fear) <line=40> [parent=f1]
fear    -> points to the λ(fear) <line=46> in global frame
Return Value: 7

f4: λ(fear) <line=46> [parent=Global]
fear    3 #attention, we found the acutal parameter disgust in f1 frame which is 3 before we called
Return Value: 7
"""


def a():
    print(twist)
twist = 3
a()
twist = 9
(lambda twist: a())(123)
