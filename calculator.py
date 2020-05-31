from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget
from calculator_gui import CalculatorGui


class Calculator:
    """ A general class to manage the calculator app. """

    def __init__(self):
        self.app = QApplication([])
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.window = QWidget()
        self.window.setFixedSize(320, 520)
        CalculatorGui(self.window, self.layout)
        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec_()


if __name__ == "__main__":
    calc = Calculator()
