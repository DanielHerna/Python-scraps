try:
    a = int(input("Add a numerator"))
    b = int(input("Add a divisor"))

    print(f"The division is {a/b}")
except ZeroDivisionError as e:
    print("You cannot divide by zero")
    print("Error: ", e)
except ValueError as e:
    print("Please enter only numbers")
    print("Error: ", e)
    