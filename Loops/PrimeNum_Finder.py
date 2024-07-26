numbers = list(range(1, 151)) #Creating a list from 1-100 (second number is not inclusive)
prime = [] #Creating an empty list

for i in numbers:
    tf = True
    if i == 1: #Because 1 is not a prime number, skip it
        continue
    if i == 2: #Because 2 is a prime number, I made an exception here
        prime.append(i)
        continue
    for j in numbers: #Initiating a second loop
        if i != j and j != 1: #i.e., divisor is NOT same as numerator and is NOT 1
            if i % j == 0: #i.e., NOT a prime number
                    tf = False
                    break #This breaks the loop completely - if False, no need to continue
    if tf == True: #Only true if number is prime
        prime.append(i)
print(prime)