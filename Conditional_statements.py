print("Conditional statements are all about decision making. If one statement is TRUE, do the associated steps; if FALSE, do some other steps")
#if(): #Stating the first condition
#elif(): #Then subsequent conditions...short for "else IF"
#elif(): #Can have multiple
#else: () #If nothing is TRUE, then carry out this function instead

#Using if and else
password = input("Please enter your password: ")
if password == "1234":
    print("Password correct - Welcome!")
else:
    print("Password incorrect - try again")

#Introducing elif
game = input("What is the best game franchise? ")
if game == "Zelda":
    print("Damn right")
elif game == "Mario":
    print("It's certainly up there!")
else: #Note that else always has the colon after it, whereas the other statements have it after the condition
    print("Are you serious?")


#Adding the logical operator "and"
username = input("Please enter your username: ")
password = input("Please enter your password: ")
if username == "Rudi" and password == "Field":
    print("Successful - welcome Rudi Field!")
else:
    print("Either username or password is incorrect")

#Adding the logical operator "or"
fruit = input("Please name a fruit: ")
if fruit == "apple" or fruit == "mango" or fruit == "orange":
    print("That's a good fruit!")
else:
    print("You could've done better...")