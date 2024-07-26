print("Lists are one way of structuring data and enable you to run loops")
print("Lists are 'mutable', meaning they can be adapted")

#CREATING a simple list
myList = ["Zelda", "Mario", "DK"] #[] used to define lists
print(myList)

#LISTING individual items using the index
print(myList[0]) #Index values startsfrom 0
print(myList[1])
print(myList[2])

#Also can retrieve items from the END of a list using negative numbers
bigList = ["Apple", "Banana", "Orange", "Lemon", "Kiwi", "Pineapple"]
print(bigList[-1]) #The last item
print(bigList[2], bigList[-2])

#Also retieve across a RANGE of indices
print(bigList[0:4], "Note that this is excluding the fourth, Kiwi - i.e., from 0-3")


#Find out HOW MANY items are in a list
print(len(bigList)) #Using the "len()" function - i.e., "length"

#Find out how many UNIQUE items are in a list
dupeList = ["Zelda", "Mario", "DK", "Zelda", "Pit", "Kirby"]
print(len(set(dupeList))) #The set() function rejects duplicates.


#ADDING and REMOVING items from a list
print(bigList)
bigList.remove("Banana") #REMOVING
print(bigList)
bigList.append("NEW") #ADDING
print(bigList)

#CHANGING an item in a list
bigList[0] = "CHANGE"
print(bigList) #"Apple" has been changed to "CHANGED"

#MERGING lists
print(myList)
mergeList = myList + bigList
print(mergeList) #This added bigList to the end of myList

print("Other functions for list include: clear(); copy(); count(); sort()")

