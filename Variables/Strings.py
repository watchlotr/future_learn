#Strings
string1 = "This is a string"
print(string1)
string2 = 'This is also a string'
print(string2)

string3 = '''This is a string
with multi-line
breaks
''' #It uses 3 quotes
print(string3)

select_char = "I will select specific characters from a string"
print(select_char[0], select_char[5], select_char[6], select_char[8]) #Selecting "I", "l", " ", "e"
#Index count begins from 0.

#modify_string = "I cannot modify an existing string"
#modify_string[5] = "O"
#Trying to change a single character led to an error

conc1 = "I am concatenating"
conc2 = "strings to form one string"
print(conc1 + conc2)
print(conc1 + " " + conc2) #This adds a space between strings