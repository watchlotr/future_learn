#Can assign user inputs to a variable
print("It's all about the input() function")

username = input("Please enter your username: ") #You can have the text prompt within the input() function
print("Welcome", username)
#Any input taken will be stored as a string

#CAVEAT - if the input is a number, it will still be string.
number = input("Please input any number: ")
print(type(number))
print("Changing the input into an integer ", type(int(number))) #The int() function is doing the conversion