class Calculator:
    """
    Input two number and calculate the result
    """
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    # Select which operator to use the calculation
    def calculate(self):

        x = float(self.num1)
        y = float(self.num2)

        if self.operator == "+":
            result = x + y
        if self.operator == "-":
            result = x - y
        if self.operator == "*":
            result = x * y
        if self.operator == "/":
            result = x / y

        return f"{x} {self.operator} {y} = {result}"
