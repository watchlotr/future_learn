#Using arguments
def func_arg(name): #The argument is "name"
    return f"Welcome, {name}!" #the f needs to be here - basically does concatenation
#A different way of saying -- return "Welcome, " + name + "!" -- which can get complicated for longer strings
print(func_arg("Rudi")) #Setting "name" to "Rudi"

print("You must provide all the arguments when you call the function")


#Positional and keyword arguments
#ALWAYS any positional arguments first, followed by keyword arguments
#Positional arguments have a position and need to be defined, but keywords are predefined.
def pos_key1(game, adj1, adj2):
    return f"{game} is a {adj1} game because the main character is {adj2}"
print(pos_key1("Zelda", "bad", "stupid"))
#These are all positional arguments - they need to be defined.

def pos_key2(game, adj1 = "good", adj2 = "funny"):
    return f"{game} is a {adj1} game because the main character is {adj2}"
print(pos_key2("Zelda"))
#Here "adj1" and "adj2" are keyword arguments, which don't need to be defined when I call the function.
#But I can change their values still

print(pos_key2("Zelda", adj1 = "bad", adj2 = "smelly"))
#But they must be listed AFTER the positional keywords - unless I say "arg = ''"


#Multiple values can be returned when calling a function
def numbers(start):
    a = start + 1 #{} only seem to be used in a string
    b = start + 2
    c = start + 3
    return a, b, c
print(numbers(start =  5))

#Another step
def numbers(start):
    a = start + 1
    b = start + 2
    c = start + 3
    return a, b, c
x, y, z = numbers(start = 5) #This line assigns values stored in a, b, c to x, y, z
print(x, y, z)