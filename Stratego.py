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

