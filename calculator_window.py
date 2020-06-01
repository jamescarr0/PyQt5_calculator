from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

from calculator_brain import CalculatorBrain
from calculator_gui import CalculatorGui


class CalculatorWindow(QWidget):
    """ A class to manage the application window and key pressed events. """

    def __init__(self):
        """ Constructor. """
        super().__init__()
        self.setWindowTitle("PyQT5 Calculator")
        self.setFixedSize(320, 460)

    def keyPressEvent(self, event):
        """ Get the key pressed. """
        buttons = range(0, 10)
        for button in buttons:
            if event.key() == eval(f'Qt.Key_{button}'):
                self._key_pressed(button)

    def _key_pressed(self, button):
        """ Print keypressed to console. """
        print(f"button {button} tapped")
