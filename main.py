from cal import Calculator


# Start program
while True:

    # Program naming
    print("-" * 20 + "Calculator" + "-" * 20)

    # UI program
    try:
        num1 = float(input("Insert number 1st: "))
        num2 = float(input("Insert number 2nd: "))
        operator = input("Insert operator: ")

    except:
        print("Reject! Check the data input. Only int and float")
        continue

    #TODO improvise if number input wrong data type?
    if isinstance(num1, float) and isinstance(num2, float):
        app = Calculator(num1, num2, operator)
        print(app.calculate())

    # ask the user to continue the program or not
    confirmation = input("continue? press [y] to continue: ")
    print("-" * 50)

    if confirmation == "y":
        continue
    else:
        print("-" * 23 + "exit" + "-" * 23)
        break

