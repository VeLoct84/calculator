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


class Total:
    """
    User will key in unlimited number and return grand total as result.
    To get the grand total, user will key in number '0' and the program
    will return result and terminated.
    """

    # create empty list
    stacklist = []

    def __init__(self):
        pass

    def add_number(self, number):
        # create empty list
        self.number = number
        
        self.stacklist.append(self.number)
        return self.stacklist

