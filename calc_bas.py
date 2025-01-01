from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

first_number = float(input("Type the first number. "))

result = 0
calculator_run = True

while calculator_run:
    print(" +\n", "-\n", "*\n", "/\n")
    mathematical_operator = input("Type the mathematical operator. ")
    second_number = float(input("Type the second number. "))

    if mathematical_operator in operations:
        result = operations[mathematical_operator](first_number, second_number)
        print(f"The result is: {result}")

        continue_calculating = input("Do you want to continue calculating? ").lower()
        if continue_calculating == "yes":
            first_number = result
        elif continue_calculating == "no":
            first_number = float(input("Type the first number. "))
    else:
        print("Please type a valid calculation")