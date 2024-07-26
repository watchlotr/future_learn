def my_function(): #Defining my own function
    return"Hello world" #The associated code
print(my_function()) #Calling my function

#Note, snake case (e.g., snake_case) used for variables and functions
#whereas PascalCase (e.g., SnakeCase) used for class names

print("Using -return- function enables my_function to hold a value, which is a string.")
print("Anything after -return- would be ignored, so it needs to be at the end of the function")
print("Need to use -print- when calling the function to recall the value of my_function")

def my_function2():
    print("Hello world 2")
my_function2()
#This gives and output, but is bad practice. The function holds no value.