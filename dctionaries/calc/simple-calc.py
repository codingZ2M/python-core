################### Namespaces: Local vs. Global Scope ####################
'''
You have a Television, who can access its internal circuits and do some repairs?
    ... TV Technician.
But anybody can control the color, brightness, contrast of the TV.. right?
'''

from calc.art import icon

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {    # Global Scope
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(icon)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True     # Local Scope

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False

calculator()
