## FUNCTIONS

# Addition
def add(a1, a2):
    return f"{a1} + {a2} = {a1+a2}"

# Subtraction
def subtract(s1, s2):
    return f"{s1} - {s2} = {s1-s2}"

# Multiplication
def multiply(m1, m2):
    return f"{m1} * {m2} = {m1*m2}"

def divide(d1, d2):
    try:
        return f"{d1} / {d2} = {d1 / d2}"
    except ZeroDivisionError: # Handling division by 0
        return "Cannot divide by 0. Please reselect the operation you would like to carry out."


# Getting two numbers from user
def get_two_numbers(prompt1 = "Please enter the first number: ",
                    prompt2 = "Please enter the second number: "):
    while True:
        try:
            n1 = float(input(prompt1))
            n2 = float(input(prompt2))
            return n1, n2
        except ValueError: # Handling non-numerical inputs into operations
            print("Please enter a numerical value.")


## The actual calculator
def calculator():
    while True:
        option = input('''Please select the operation you want to use:
                        1: Addition
                        2: Subtraction
                        3: Multiplication
                        4: Division
                        5: EXIT programme
                       ''') #This is the menu, giving the user multiple options

        if option in ["1", "2", "3"]:
            n1, n2 = get_two_numbers()
            if option == "1":
                print(add(n1, n2))
            elif option == "2":
                print(subtract(n1, n2))
            elif option == "3":
                print(multiply(n1, n2))
        elif option == "4":
            n1, n2 = get_two_numbers("Please enter the numerator: ",
                                     "Please enter the denominator: ") # Prompts specific to division
            print(divide(n1, n2))
        elif option == "5": # A prompt to exit the programme
            break
        else:
            print("Please enter a valid option (1-5).") # Looping until a valid input is received
calculator()
