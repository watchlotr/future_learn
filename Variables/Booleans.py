#Objects of the boolean data type are only either "TRUE" or "FALSE".
boolean1 = True
print(type(boolean1))
boolean2 = False
print(type(boolean2))
print(boolean1, boolean2)

#UUsing "and" and "or" keywords
print(boolean1 and boolean2) #Asking whether both booleans are TRUE or not
print(boolean1 or boolean2) #whether either is TRUE

print("If I changed boolean2 to be TRUE, then using the -and- keyword would give TRUE, as both are now TRUE")