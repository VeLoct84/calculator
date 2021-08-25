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
    # unlimited add number
    # enhance CLI UI to better view
