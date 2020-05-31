from PyQt5.QtCore import pyqtSlot


class CalculatorBrain:
    """ A class to manage the calculator logic. """

    def __init__(self, calculator):
        self.calculator = calculator
        self.display_value, self.first_number, self.second_number = 0, 0, 0
        self._operator = ""

    @pyqtSlot()
    def button_tapped(self, btn_id):
        """ Process the button pressed. """

        if type(btn_id) == dict:

            # Operator button pressed.
            if 'operator' in btn_id.keys():
                self._operator_pressed(btn_id)

            # Miscellaneous button pressed. ("%", ".", "plus/minus")
            if 'misc' in btn_id.keys():
                self._misc_pressed(btn_id)

        # Number button pressed.
        if type(btn_id) == int:
            self._number_pressed(btn_id)

        # Update the display.
        self._update_lcd()

    def _number_pressed(self, btn_id):
        """ get the int value from a number button pressed event and update display. """

        print(f"button {btn_id} pressed")
        if self.display_value == 0:
            self.display_value = btn_id
        else:
            self.display_value = f"{self.display_value}{btn_id}"

    def _operator_pressed(self, btn_id):
        """ get the operator from an operator button pressed event. """

        # Division pressed.
        if btn_id['operator'] == u"\u00F7":
            self._operator = "//"
            print("Division")

        # Multiplication pressed.
        elif btn_id['operator'] == u"\u00D7":
            self._operator = "*"
            print("Multiplication")

        # Subtraction pressed.
        elif btn_id['operator'] == "-":
            self._operator = "-"
            print("Subtraction")

        # Addition pressed.
        elif btn_id['operator'] == "+":
            self._operator = "+"
            print("Addition")

        # Equals pressed.
        else:
            print("Equals")
            self._equals_pressed()

    def _equals_pressed(self):
        """ Equals pressed evaluate expression. """
        # TODO

    def _evaluate(self):
        """ evaluate the current string and return answer. """
        #TODO

    def _misc_pressed(self, btn_id):
        """ Misc buttons pressed (C, decimal, plus/minus, percent). """

        # Reset button pressed.
        if btn_id['misc'] == 'C':
            print("Reset button")
            self._full_reset()

        # Plus/Minus button pressed.
        if btn_id['misc'] == u"\u00B1":
            print("Plus/Minus button")

        # Percent button pressed.
        if btn_id['misc'] == "%":
            print("Percent button")

        # Decimal button pressed.
        if btn_id['misc'] == ".":
            print("Decimal button")

    def _update_lcd(self):
        """
        Update the LCD display with new value. If out out of range, avoid OverFlowError crash
        and set display to "Er"

        Value must be in range -2147483648 to 2147483647
        """
        try:
            self.calculator.lcd.display(self.display_value)
        except OverflowError:
            # Overflow error, out of range.
            self.calculator.lcd.display("Er")

    def _full_reset(self):
        """ Reset calculator """
        self.display_value, self.first_number, self.second_number = 0, 0, 0
        self._operator = ""
