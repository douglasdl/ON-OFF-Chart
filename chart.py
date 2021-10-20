segments = [' ', '_', '|', '‾']
chart = list(" _ _ _ _ _ _ _ _ _ _ _ _ _ _")

def setON(switch):
    global chart
    if switch == 1:
        chart[switch] = "‾"
        chart[switch-1] = "|"
        chart[switch+1] = "|"
    elif switch == 2:
        chart[switch + 3] = "‾"
    elif switch == 3:
        chart[switch + 6] = "‾"
    elif switch == 4:
        chart[switch + 9] = "‾"
    elif switch == 5:
        chart[switch + 12] = "‾"
    elif switch == 6:
        chart[switch + 15] = "‾"
    elif switch == 7:
        chart[switch + 18] = "‾"

def setOFF(switch):
    pass

def printChart():
    #print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    #print("")
    #print("|‾|_|‾|_|‾|_|‾|_|‾|_|‾|_|‾|_")
    pass

setON(1)
#setON(2)
#setON(3)
#setON(4)
#setON(5)
#setON(6)
#etON(7)
print("".join(chart))    