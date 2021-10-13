#! calculator/dev/addmorenumber.py
"""
User will key in unlimited number and return grand total as result.
To get the grand total, user will key in number '0' and the program
will return result and terminated.
"""

number = []

def add_number(numbers):
    number.append(numbers)
    return number

print("press [0] to see the result")

while True:
    # user insert number
    data = int(input("Insert number:\n"))
    add_number(data)
    
    # showing data entry
    print(number)

    # ask user what next
    if data == 0:
        total = sum(number)
        print(f"Grand Total: {total}")
        print(50 * "-")
        break
