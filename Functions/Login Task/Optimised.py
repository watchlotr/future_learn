username = "Rudi"
password = "Keneisha"

def usercheck():
    user = input("Please enter your username: ")
    return user == username #Using the comparison operator ==, returning True or False
user = usercheck()

def pwcheck():
    pw = input("Please enter your password: ")
    return pw == password
pw = pwcheck()

if user and pw: #The AND keyword always checks for true - so "if user and pw are both true".
    print("Welcome", username)
else:
    print("Username or password incorrect")