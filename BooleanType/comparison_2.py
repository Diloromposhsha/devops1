# >, <,!=, ==, <=, >=

#Create a boolean variable
bool1 = True
bool2 = False

# In the line below since the text is in quotes it is a string variable.
# String variable and bool variable give false when compared.
print(bool1 == "True") #False

print(bool2 != "False")   # True


#----------------------
print((True+6)==(False+7)) # True

#Unsupported Opperand(Type Error)
#print(bool1+" is the value ")

# Error

print("bool2 + is the value")
#bool2 + is the value



print(bool1==bool2) # False

  #Error

bool2==bool1
print(bool2) # False

bool2=bool1
print(bool2) # True