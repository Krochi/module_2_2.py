while (True):
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    third = int(input("Enter third number: "))

    if first == second and first == third and second == third:
        print(2)

    elif first == second or first == third or second == third:
        print(1)

    else:
        print(0)
        break