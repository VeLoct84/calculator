# addmorenumber.py
number = []

def add_number(numbers):
    for num in numbers:
        number.append(num)
    return number


while True:
    # user insert number
    data = input("Insert number:\n")

    # ask user what next
    cont = input("add more number? [y/n]")
    if cont == "y":
        print(add_number(data))
    else:
        print("Program terminated!")
        break

#TODO to sum all number in number[]
#ERR the number keyin split inside the list
    #for example when user input 110 it return [1,1,0]
    #expectation is [110]
