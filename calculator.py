from PyQt5.QtWidgets import QApplication, QGridLayout
from calculator_gui import CalculatorGui

from calculator_window import CalculatorWindow


class Calculator:
    """ A general class to manage the calculator app. """

    def __init__(self):
        self.app = QApplication([])
        self.app.setStyle('Fusion')
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.window = CalculatorWindow()
        CalculatorGui(self.window, self.layout)
        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec_()


if __name__ == "__main__":
    calc = Calculator()
