#Let's ask user to enter a word 
# Then print that word

print("Please enter a word")
word = input()
print("The word that user entered is",word)

print("The data type of the variable word is",type(word))

# Let's ask user to enter a number

print("please enter any number")
num = input()
print(num) # -> 23
print(type(num)) # -> <class 'str'>

# We understand that input() will always return the values as string. 
# What should we do when we need other data types such as int, float? 

# How can we convert string into an integer variable? 

print("please enter only numbers not starting with 0")
num1 = int(input())
#if user enters anything other than number code will generate
#invalid literal error. 
print("Casted result of input function is",num1)
print("Casted data type of input function is",type(num1))