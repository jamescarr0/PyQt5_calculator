from PyQt5.QtWidgets import QPushButton


class CalculatorButton(QPushButton):
    """ A class to manage the size and styling of the calculator button widget. """

    def __init__(self, button_text):
        super().__init__(button_text)
        self.setMinimumSize(70, 70)
