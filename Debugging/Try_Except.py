#Use Try and Except blocks when you think there's a particular chunk of code that won't run.
#You may be able to pick out that that segment is the issue when code fails to run.

try:
    #Code segment
    print(n) #Doesn't run because not in ""
except: #Runs if try code doesn't.
    print("didn't work") #Could have the Except block as a backup solution!

try:
    print(n)
except:
    print("didn't work 2")
finally: #This Finally block will run regardless of whether the Try/Except block runs
    print("this message will always show!")



#The RAISE keyword is used to highlight when a *particular condition* isn't satisfied
def RaiseFunc(number):
    if number == 0: #Condition for error
        raise ValueError("Number must not equal 0") #I have specified the (built in) exception class name
    return number

try:
    print(RaiseFunc(0)) #If the argument was equal to anything else, this block would run
except ValueError as e: #If the number == 0, this exception block will be run with the specified
    #raise block code as written in the function
    #"as" simply provides an object for the exception - good for when you having multiple exceptions
    print(e)



# EG Imagine a Banking App
while True: # Enables me to test until I give a valid input
    transfer = input("How much money would you like to transfer to Keneisha?")

    try:
        transfer_amount = float(transfer)
        if transfer_amount > 0 :
            print(f"You have transferred ${transfer} to Keneisha!")
            break # Code stops if a valid input is given
        else:
            print("Please enter a positive value")
    except ValueError:
        print("Invalid input. Please enter a numerical value")
