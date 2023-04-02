
# All numerical types in Python are immutable, which means
# they won't  change their value unless reassigned.

num = 7

print(num) # 7
print(type(num)) # <class 'int'>

print(num/3) #2.3

print(num) # What will be the value that num holds?
# 7
print(type(num)) # <class 'int'>

num = 10 

print("After reassignment")
print(num)
print(type(num))

#Let's reassign the variable num with a different type
print("After assigning with a different data type")
num = 10.0
print(num) # 10.0
print(type(num)) # float

num = "A text"
print(num) 
print(type(num))

# In Python the variables can change their values as well 
# as their data types after reassignment. 

# Let's make this variable num a numerical type. 

num = 10 

num+=3    #num = num + 3
print(num) 
print(type(num))