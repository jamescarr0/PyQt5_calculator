from functools import partial

from calculator_brain import CalculatorBrain
from calculator_button import CalculatorButton
from calculator_lcd import CalculatorLcd


class CalculatorGui:
    """ A class to manage the calculator GUI. """

    def __init__(self, window, layout):
        """ Initialise constructor attributes """
        self.calculator_brain = CalculatorBrain(self)
        self.window = window
        self.layout = layout
        self._create_lcd()
        self._create_number_buttons()
        self._create_operator_buttons()
        self._create_misc_buttons()

    def _create_lcd(self):
        """ Create the calculator lcd display. """
        self.lcd = CalculatorLcd()
        # Span the display across multiple cells.
        # addWidget(Widget, row, column, rowspan, colspan)
        self.layout.addWidget(self.lcd, 0, 1, 1, 4)

    def _create_number_buttons(self):
        """ Create and label the calculator int buttons. """
        button_label = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        zero_label = 0

        index = 0
        for row in range(2, 5):
            for btn in range(1, 4):
                button = CalculatorButton(str(button_label[index]))
                button.clicked.connect(partial(self.calculator_brain.button_tapped, button_label[index]))
                self.layout.addWidget(button, row, btn)
                index += 1

        # Create the 0 button and span multiple cells.
        z_button = CalculatorButton(str(zero_label))
        z_button.clicked.connect(partial(self.calculator_brain.button_tapped, zero_label))
        self.layout.addWidget(z_button, 5, 1, 1, 2)

    def _create_operator_buttons(self):
        """ Create the operator buttons. """
        operators = [u"\u00F7", u"\u00D7", "-", "+", "="]
        for row in range(1, 6):
            button = CalculatorButton(operators[row - 1])
            context = {"operator": operators[row - 1]}
            button.clicked.connect(partial(self.calculator_brain.button_tapped, context))
            self.layout.addWidget(button, row, 4)

    def _create_misc_buttons(self):
        """ Create misc operator buttons. """
        button_dict = {
            # Button Label: Button Position.
            ".": "5, 3",
            "C": "1, 1",
            u"\u00B1": "1, 2",
            "%": "1, 3"
        }
        for button, position in button_dict.items():
            button = CalculatorButton(button)
            context = {"misc": button.text()}
            button.clicked.connect(partial(self.calculator_brain.button_tapped, context))
            self.layout.addWidget(button, *eval(position))
