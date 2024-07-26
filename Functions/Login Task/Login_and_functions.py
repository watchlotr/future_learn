username = "Rudi"
password = "Keneisha"

#username function
def usercheck():
    user = input("Please enter your username: ")
    if user == "Rudi": #I didn't use "if username == username" because I don't know if it would always
        #be TRUE because it just equals itself
        return True
    else:
        return False
user = usercheck()
#print(usercheck()) #EDIT 1: This actually calls AND outputs
#print(user) #EDIT 2: This made it so that in the last chunk, code didn't immediately terminate when user == FALSE
#But still the issue that the value of user (TRUE/FALSE) would still print

#Password function
def pwcheck():
    pw = input("Please enter your password: ")
    if pw == "Keneisha":
        return True
    else:
        return False
pw = pwcheck() #EDIT 4: When the username/password modules are run alone, I am prompted to input.
#So probably the last module isn't the one prompting me

if user == True and pw == True: #EDIT 3: Seems that by having user/pw instead of the function enables me
    #to call the function still, without the issue of early terminaion
    print("Welcome", username)
else:
    print("Username or password incorrect")


#If I want to use either checking functions again, just call the function!!!

