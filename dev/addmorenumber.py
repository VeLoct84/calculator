#! calculator/dev/addmorenumber.py
"""
User will key in unlimited number and return grand total as result.
To get the grand total, user will key in number '0' and the program
will return result and terminated.
"""


class Total:

    # create empty list
    stacklist = []

    def __init__(self):
        pass

    def add_number(self, number):
        # create empty list
        self.number = number

        self.stacklist.append(self.number)
        return self.stacklist


#############################################
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
        print(50 * "-")
        break
