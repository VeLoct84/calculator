from cal import Calculator


# Start program
while True:

    # Program naming
    print("-" * 20 + "Calculator" + "-" * 20)

    # UI program
    try:
        num1 = float(input("Insert number 1st: "))
        operator = input("Insert operator: ")
        num2 = float(input("Insert number 2nd: "))

        app = Calculator(num1, num2, operator)
        print(app.calculate())

    except:
        print("Reject! Check the data input. Only int and float")
        continue


    # ask the user to continue the program or not
    confirmation = input("continue? press [y] to continue: ")
    print("-" * 50)

    if confirmation == "y":
        continue
    else:
        print("-" * 23 + "exit" + "-" * 23)
        break

#TODO
    # unlimited add number (~/calculator/dev/addmorenumber.py)
    # enhance CLI UI to better view
