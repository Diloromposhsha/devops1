num1 = -100
num2 = 0
print(bool(num1)) # variable num1 will be converted to boolean
                  # therefore it will take the value True.

print(bool(num2))# We'll get the false because when 0 converted to 
                 # boolean we get False. 

s = ""
print("The boolean value of the empty string is",bool(s))

list = []
print("The boolean value of the empty list is",bool(list))

tuple =()
print("The boolean value of the empty tuple is",bool(tuple))


# Q1: What will be the output?
print(bool("False"))  # True
# When string is not empty,
# regardless of the string value bool function will give True