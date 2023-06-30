def peace(today):
    harmony = love+2
    return harmony + today(love+1)

def joy(peace):
    peace, love = peace+2, peace+1
    return love // harmony

love, harmony = 3, 2
peace(joy)

"""
Global frame
peace   func peace(today) [parent=Global]
joy     func joy(peace) [parent=Global]
love    3
harmony 2

f1: peace [parent=Global]
today   point to joy in global frame
harmony 5
Return Value 7

f2: joy [parent=Global]
peace   6
love    5
Return Value 2 #important, harmony == 2, where joy defined.
"""
