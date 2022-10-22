import pydirectinput as pdi

# slow down the keyboard inputs, so that Stardew Valley receives the input.
pdi.PAUSE =.159

# FAILSAFE allows the host to turn off pyauotgui
# by moving the mouse to the top left of the monitor very quickly
pdi.FAILSAFE = True

""" This class implements the model for Stardew Valley Commands
    it also declares and intializes the class with the strings associated with the keyboard commands"""
class StardewValleyCommands():

    def __init__(self):
        self._up = 'w'          # if you keep your hand up
        self._down = 's'        # if you keep your hand down
        self._left = 'a'        # if you keep your hand on the left
        self._right = 'd'       # if you keep your hand on the right
        self._map = 'm'         
        self._menu = 'e'
        self._journal = 'f'
        self._leftclick = 'c'
        self._rightclick = 'x'
        self._esc = 'esc'
        self._one = '1'         # hold up 1 finger
        self._two = '2'         # hold up 2 fingers
        self._three = '3'       # hold up 3 fingers
        self._four = '4'        # hold up 4 fingers
        self._five = '5'        # hold up 5 fingers
        self._six ='6'          # hold up 6 fingers
        self._seven = '7'       # hold up 7 fingers
        self._eight = '8'       # hold up 8 fingers
        self._nine = '9'        # hold up 9 fingers
        self._zero = '0'        # hold up 10 fingers
        self._minus = '-'
        self._equals = '='

    """ Stardew Valley Commands """
    def moveUp(self):
        pdi.keyDown(self._up)
        pdi.keyUp(self._up)

    def holdUp(self):
        pdi.keyDown(self._up)
    
    def stopMovingUp(self):
        pdi.keyUp(self._up)

    def moveDown(self):
        pdi.keyDown(self._down)
        pdi.keyUp(self._down)

    def holdDown(self):
        pdi.keyDown(self._down)
    
    def stopMovingDown(self):
        pdi.keyUp(self._down)

    def moveLeft(self):
        pdi.keyDown(self._left)
        pdi.keyUp(self._left)

    def holdLeft(self):
        pdi.keyDown(self._left)
    
    def stopMovingLeft(self):
        pdi.keyUp(self._left)

    def moveRight(self):
        pdi.keyDown(self._right)
        pdi.keyUp(self._right)

    def holdRight(self):
        pdi.keyDown(self._right)
    
    def stopMovingRight(self):
        pdi.keyUp(self._right)

    def openmap(self):
        pdi.keyDown(self._map)
        pdi.keyUp(self._map)

    def openmenu(self):
        pdi.keyDown(self._menu)
        pdi.keyUp(self._menu)

    def openjournal(self):
        pdi.keyDown(self._journal)
        pdi.keyUp(self._journal)

    def leftclick(self):
        pdi.click()

    def rightclick(self):
        pdi.keyDown(self._rightclick)
        pdi.keyUp(self._rightclick)

    def escape(self):
        pdi.keyDown(self._esc)
        pdi.keyUp(self._esc)

    def tool_1(self):
        pdi.keyDown(self._one)
        pdi.keyUp(self._one)

    def tool_2(self):
        pdi.keyDown(self._two)
        pdi.keyUp(self._two)

    def tool_3(self):
        pdi.keyDown(self._three)
        pdi.keyUp(self._three)

    def tool_4(self):
        pdi.keyDown(self._four)
        pdi.keyUp(self._four)

    def tool_5(self):
        pdi.keyDown(self._five)
        pdi.keyUp(self._five)

    def tool_6(self):
        pdi.keyDown(self._six)
        pdi.keyUp(self._six)

    def tool_7(self):
        pdi.keyDown(self._seven)
        pdi.keyUp(self._seven)

    def tool_8(self):
        pdi.keyDown(self._eight)
        pdi.keyUp(self._eight)

    def tool_9(self):
        pdi.keyDown(self._nine)
        pdi.keyUp(self._nine)

    def tool_10(self):
        pdi.keyDown(self._zero)
        pdi.keyUp(self._zero)

    def tool_11(self):
        pdi.keyDown(self._minus)
        pdi.keyUp(self._minus)

    def tool_12(self):
        pdi.keyDown(self._equals)
        pdi.keyUp(self._equals)

