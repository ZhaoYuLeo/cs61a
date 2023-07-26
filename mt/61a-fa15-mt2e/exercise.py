def f(it):
    return [bit, it[0]()]

def b(it):
    def steps():
        nonlocal it
        it = bit.pop()
    return [steps, 3]

fit = [[1]] + [2]
bit = b(fit)
fit.append(f(bit))

"""
Global frame
f       -> func f(it) [parent=Global]
b       -> func b(it) [parent=Global]
bit     -> points to the list created in f1

             [1]                    [1]
fit     ->  [ ↑ , 2]  changed into [ ↑, 2, ↓] in f2: f
                                          Return value in f2: f
f1: b [parent=Global]
it      -> points to fit changed into 3 in f3: steps
steps   -> func steps [parent=f1]       ←┓   
Return Value    -> [↑, 3] changed into [ | ] in f3: steps

f2: f [parent=Global]
it     -> points to bit which points to the Return list in f1
                   bit
Return Value    -> [↑,  None]

f3: steps [parent=1]
it     -> 3 # but 'it' isn't defined here, you should delete this line
Return Value    None
"""


w = [2, 2]
z = [2, 2, w]
x = z[w[0]]
y = list(x)
x.append([w.pop()])
y, x = z[2], y
w[0] = z.pop()

"""
Global frame
          ┏-┓  
          ↓ | [2]
w       -> [|, ↑] 
          ↑
y       ->┚ 
x       -> [2, 2]
z       -> [2, 2]
"""
