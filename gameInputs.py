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
        self._up = 'w'
        self._down = 's'
        self._left = 'a'
        self._right = 'd'
        self._map = 'm'
        self._menu = 'e'
        self._journal = 'f'
        self._leftclick = 'c'
        self._rightclick = 'x'
        self._esc = 'esc'
        self._one = '1'
        self._two = '2'
        self._three = '3'
        self._four = '4'
        self._five = '5'
        self._six ='6'
        self._seven = '7'
        self._eight = '8'
        self._nine = '9'
        self._zero = '0'
        self._minus = '-'
        self._equals = '='

    """ Stardew Valley Commands """
    def moveup(self):
        pdi.keyDown(self._up)
        pdi.keyUp(self._up)

    def movedown(self):
        pdi.keyDown(self._down)
        pdi.keyUp(self._down)

    def moveleft(self):
        pdi.keyDown(self._left)
        pdi.keyUp(self._left)

    def moveright(self):
        pdi.keyDown(self._right)
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

