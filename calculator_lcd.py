from PyQt5.QtWidgets import QLCDNumber
from PyQt5 import QtGui


class CalculatorLcd(QLCDNumber):
    """ A class to manage the size and styling of the calculator display widget. """

    def __init__(self):
        super().__init__()
        self._set_styling()

    def _set_styling(self):
        """ Style the LCD display. """
        self.setNumDigits(11)
        foreground = QtGui.QColor(0, 0, 0)
        background = QtGui.QColor(176, 223, 229)
        self.setAutoFillBackground(True)
        palette = self.palette()

        # foreground color
        palette.setColor(palette.WindowText, foreground)
        # background color
        palette.setColor(palette.Background, background)

        self.setPalette(palette)
