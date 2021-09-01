# checklist.py
shopping_list = {}

# function - to user add into dict
def add_item(item_name, quantity):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else:
        shopping_list[item_name] = quantity


# user input
while True:
    item = input("item to buy: \n")
    number = int(input("how many item? \n"))
    add_item(item, number)

    # ask user if want to add more or none
    cont = input("add more item? (y/n)")

    if cont == "y":
        print(shopping_list)
        continue
    else:
        print("Checklist: ")
        for item_name, quantity in shopping_list.items():
            print(f"{quantity}x - {item_name} ")
        break
