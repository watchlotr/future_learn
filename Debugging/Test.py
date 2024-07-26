## FUNCTIONS

# Addition
def add(a1, a2):
    return f"{a1} + {a2} = {a1 + a2}"

# Subtraction
def subtract(s1, s2):
    return f"{s1} - {s2} = {s1 - s2}"

# Multiplication
def multiply(m1, m2):
    return f"{m1} * {m2} = {m1 * m2}"

# Division
def divide(d1, d2):
    try:
        result = d1 / d2
        return f"{d1} / {d2} = {result}"
    except ZeroDivisionError:
        return "Cannot divide by 0, please start the operation again."

# Getting two numbers from user
def get_two_numbers(prompt1="Please enter the first number: ",
                    prompt2="Please enter the second number: "):
    while True:
        try:
            n1 = float(input(prompt1))
            n2 = float(input(prompt2))
            return n1, n2
        except ValueError:
            print("Please enter a numerical value.")

# Mapping functions to menu options
operation_functions = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide)
}

## The actual calculator
def calculator():
    while True:
        option = input('''Please select the operation you want to use:
                        1: Addition
                        2: Subtraction
                        3: Multiplication
                        4: Division
                        5: EXIT programme
                       ''')

        if option in operation_functions:
            n1, n2 = get_two_numbers() if option != "4" else get_two_numbers("Please enter the numerator: ", "Please enter the denominator: ")
            print(operation_functions[option][1](n1, n2))
        elif option == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Please enter a valid option (1-5).")

calculator()
