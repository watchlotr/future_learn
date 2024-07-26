#A programme serving as a basic TODO list

todo_list = [] #Creating a list that is empty
next_task = input("Please input a task to add to your TODO list! To stop writing enter nothing: ")
#Defining the variable which will be a part of the while loop's statement

while next_task != "":
    todo_list.append(next_task) #When the user inputs something into the textbox, it will be added to the list
    next_task = input("Please input a task to add to your TODO list! ") #User prompted to write again

print("Here is your TODO list:")
for i in todo_list: #List only printed after the loop ends.
    print(i)