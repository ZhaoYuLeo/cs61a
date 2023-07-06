def av(eng, er):
    er = lambda: eng
    def eng(er):
        eng = 2
        return lambda eng: eng + thor
    return er()

thor = 3
stark = lambda x: lambda y: 4
av(stark, lambda: 5)(6)(7)

"""
Global frame
av      -> func av(eng, er) [parent=Global]
thor    3
stark   -> func λ(x) <line=9> [parent=Global]
        -> func λ <line=10> [parent=Global]

f1: av [parent=Global]
eng     -> points to λ(x) <line=9> in global frame and changes -> func eng(er) [parent=f1]
er      -> points to λ <line=10> in global frame and changes -> func λ <line=2> [parent=f1]
Return Value    -> points to func eng(er) in f1 frame

f2: λ <line=2> [parent=f1]
Return Value    -> points to func eng(er) in f1 frame

f3: eng [parent=f1]
er      6
eng     2
Return Value    -> func λ(eng) <line=5> [parent=f3]

f4: λ <line=5> [parent=f3]
eng     7
Return Value    10
"""
