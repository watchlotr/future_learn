print("Repeats for as long as a condition remains true") #i.e., won't stop until a condition is met
#Useful for when you want to repeat code without knowing the number of repetitions ahead of time.

#while test_condition:
    #statement(s)
print("The test condition is a boolean statement")
print("The loop stops when the statement is FALSE")

#Example
count = 0 #First declaring a variable
while count < 5: #Terminates when count = 5
    print(count)
    count = count + 1 #can be shorthand written as coun+=1