class Calculator:
    """
    Input two number and calculate the result
    """

    def __init__(self, num1, num2, operator):
        # ask user to input num1,num2 and operator
        """
        num1 --> int, float
        num2 --> int, float
        operator --> "+,-,*,/"
        """
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    # Select which operator to use the calculation
    def calculate(self):

        """
        converting operator string and return the value num1 and num2
        """
        x = self.num1
        y = self.num2

        # convert the string operator
        if self.operator == "+":
            result = x + y
        if self.operator == "-":
            result = x - y
        if self.operator == "*":
            result = x * y
        if self.operator == "/":
            result = x / y

        return f"{x} {self.operator} {y} = {result}"
