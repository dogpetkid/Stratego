##Stratego written by Dogpetkid

##Imports
import os
from Choose import *
import graphics
try: import winsound
except: pass
try: ##Import the multiplayer additions
    from clienttest import *
    from servertest import *
    multi = True
except:
    multi = False

##Mess alert
print("If you see this... you might have a box that just pops on your screen later in the game (AND IT CAN GET ANNOYING).")
os.system('cls' if os.name == 'nt' else 'clear')

##Commenting system:

##Single Pound (#) = Comment out code
##Single Pound-Dollar (#$) = Go back and fix
##Double Pounds (##) = Comment
##Double Pound-At (##@) = Chess/Code Comment
##Triple Pound (###) = Code Probe/Tracer
##(Not all cases follow this system but most do for convenience)

##Dictionary:

##None

##To do:

##Start pieces

class piece():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        board.board[x,y] = self
        if self.piece() == "bombB" or self.piece() == "flagF":
            self.move = False
        else:
            self.move = True
    
    def piece(self):
        return(type(self).__name__)

class marshal1(piece):
    pass

class general2(piece):
    pass

class colonel3(piece):
    pass

class major4(piece):
    pass

class captain5(piece):
    pass

class lieutenant6(piece):
    pass

class sergeant7(piece):
    pass

class miner8(piece):
    ##Can beat bombs
    pass

class scout9(piece):
    ##Can go as far in a row as possible
    pass

class spyS(piece):
    ##Can beat Marshal (1)
    pass

class bombB(piece):
    pass

class flagF(piece):
    pass


class board:
    board = []
    for x in range(10):
        row = []
        for y in range(10):
            row.append("")
        board.append(row)
