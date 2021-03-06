from PyQt5.QtCore import pyqtSlot


class CalculatorBrain:
    """ A class to manage the calculator logic. """

    def __init__(self, calculator):
        self.calculator = calculator
        self.display_value, self.first_number, self.second_number = 0, 0, 0
        self._operator = ""
        self.equals_pressed = False

    @pyqtSlot()
    def button_tapped(self, btn_id):
        """ Process the button pressed. """

        if self.equals_pressed:
            self.first_number = self.display_value
            self._zero_display()
            self._update_lcd()
            self.equals_pressed = False

        if self.display_value == "Er":
            self._full_reset()

        if type(btn_id) == dict:
            # Operator button pressed.
            if 'operator' in btn_id.keys():
                self._operator_pressed(btn_id)

            # Miscellaneous button pressed. ("%", ".", "plus/minus")
            elif 'misc' in btn_id.keys():
                self._misc_pressed(btn_id)

        # Number button pressed.
        elif type(btn_id) == int:
            self._number_pressed(btn_id)

        # Update the display.
        self._update_lcd()

    def _number_pressed(self, btn_id):
        """
        Number button pressed.
        --- range (0 - 9)
        """

        if self.display_value == 0:
            self.display_value = btn_id
        else:
            self.display_value = f"{self.display_value}{btn_id}"

    def _operator_pressed(self, btn_id):
        """
        Operator button pressed.
        --- ( /, *, +, - )
        """

        # Store the current display.
        self._store_numbers()

        # Division pressed.
        if btn_id['operator'] == u"\u00F7":
            self._operator = "/"
        # Multiplication pressed.
        elif btn_id['operator'] == u"\u00D7":
            self._operator = "*"
        # Subtraction pressed.
        elif btn_id['operator'] == "-":
            self._operator = "-"
        # Addition pressed.
        elif btn_id['operator'] == "+":
            self._operator = "+"
        # Equals pressed.
        else:
            self._perform_calculation()

    def _misc_pressed(self, btn_id):
        """
        Misc buttons pressed
        --- (C, decimal, plus/minus, percent).
        """

        # Reset button pressed.
        if btn_id['misc'] == 'C':
            # Reset all attributes.
            self._full_reset()

        # Plus/Minus button pressed.
        if btn_id['misc'] == u"\u00B1":
            # Toggle sign display (+/-).
            self.display_value = -int(self.display_value)

        # Percent button pressed.
        if btn_id['misc'] == "%":
            # Perform percent logic.
            self._percent_button_logic()

        # Decimal button pressed.
        if btn_id['misc'] == ".":
            # Add decimal point to display.
            if "." not in str(self.display_value):
                display_string = str(self.display_value) + "."
                self.display_value = str(display_string)

    def _percent_button_logic(self):
        """ Perform logic and calculate when the percent button is tapped. """

        if not self.first_number and not self._operator:
            self.display_value = float(self.display_value) / 100.00

        elif self.first_number and self._operator:
            self.second_number = self.display_value
            eval_string = f"{self.first_number}{self._operator}({self.first_number}*{self.second_number}/100)"
            print(f"Sum to evaluate: {eval_string}")
            self.display_value = eval(eval_string)
            self.equals_pressed = True

    def _store_numbers(self):
        """ Assign the current number to its correct position. """
        if not self.first_number and not self._operator:
            self.first_number = self.display_value
            self._zero_display()
        else:
            self.second_number = self.display_value

    def _perform_calculation(self):
        """ Equals pressed.
        evaluate expression.
        """
        print(f"Sum to evaluate = {self.first_number}{self._operator}{self.second_number}")
        try:
            answer = eval(f"{self.first_number}{self._operator}{self.second_number}")
        except ZeroDivisionError:
            print("Zero division error")
            answer = "Er"

        print(f"\t={answer}")
        self.display_value = answer
        self._prepare_for_input(answer)

    def _prepare_for_input(self, answer):
        """ Prepare calculator for input after evaluating sum. """
        self.first_number, self.second_number, self._operator = answer, 0, ""
        self.equals_pressed = True

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
        """ Reset all calculator attributes. """
        self.display_value, self.first_number, self.second_number, self._operator = 0, 0, 0, ""
        self.equals_pressed = False

    def _zero_display(self):
        """ Zero the display. """
        self.display_value = 0
