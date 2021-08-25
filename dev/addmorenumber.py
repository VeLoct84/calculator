#TODO check while syntax
while:
    """
    Adding more numbers and result
    """
    try:
        num = []
        data = input("Insert number:\n")
        cont = input("add more number? [y/n]")
        if cont == "y":
            num.append(data)
        else:
            continue

    # function to total all the numbers
    def addition():
        zero = 0
        for num in addnum:
            zero += num
        return zero

    print(addition())
