input_age = int(input('How old are you?'))
if input_age < 18: #Issue was that input_age is initially a string (user input). Therefore, I converted the
    #input into an integer. This was a RUNTIME error.
   print("You're too young")
else:
   print('You are old enough')