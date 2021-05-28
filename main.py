from cal import Calculator


# Program name
print("Calculator")

# Start program
while True:

    # user input
    num1 = input("Insert number 1st: ")
    num2 = input("Insert number 2nd: ")
    operator = input("Insert operator: ")

    app = Calculator(num1, num2, operator)
    print(app.calculate())

    # ask the user to continue the program or not
    confirmation = input("continue? press [y] to continue: ")
    print("-" * 50)

    if confirmation == "y":
        continue
    else:
        break

