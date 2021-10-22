from cal import Calculator, Total


# Start program
while True:

    # Program naming
    print("-" * 20 + "Calculator" + "-" * 20)

    # ask the user to continue the program or not
    selection = input(
        """Please select function:
        (a) calculate two only
        (b) unlimited total number
        (q) terminate program
        Your answer: """
    )
    print("-" * 50)

    if selection == "a":
        try:
            num1 = float(input("Insert number 1st: "))
            operator = input("Insert operator: ")
            num2 = float(input("Insert number 2nd: "))

            app = Calculator(num1, num2, operator)
            print(app.calculate())

        except:
            print("Reject! Check the data input. Only int and float")
            continue

    elif selection == "b":
        print("press [0] to see the result")

        while True:
            # user insert number
            data = int(input("Insert number:\n"))
            n = Total()
            list_num = n.add_number(data)

            # showing data entry
            print(list_num)

            # ask user what next
            if data == 0:
                total = sum(list_num)
                print(f"Grand Total: {total}")
                print("-" * 23 + "exit" + "-" * 23)
                break

    else:
        print("Program terminate")
        break

# TODO
# check function "b" selection
# enhance CLI UI to better view
