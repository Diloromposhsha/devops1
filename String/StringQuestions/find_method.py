# In other words, find method is exact opposite of accesing elements in
# string. 
#    012345
a = "Python"

print(a[2]) # t

# What if you have the letter itself but want to find index number
# of that letter? 
print(a.find('t')) # 2

# find method will give us first index number of given parameter.

#     0123
s2 = "java"

print(s2.find("va")) # 2

# the code above will print 2 because given sequence of chars
# start from index number 2. 

print(s2.find("str")) # -1
# When given sequence of chars or char does not exist in str,
# find method will return -1. 
#     0123456789
s3 = "Encapsulation is good for data hiding."
#I want to find the index number of letter a? 
print(s3.find("a")) # -> 3
# Even the character is repeating through out the string it will 
# return first index number of that character. 

# rfind() method. 
# rfind() method is exact same logic  as find method, but 
# instead of giving first index of a char, it gives last index of 
# given character. 

# To be able to find last index of letter 'a'
print(s3.rfind('a')) # 29


#       01234
name = "Peter"

# First index for letter e is 1
# last index for letter e is 3

print(name.find('e')) # 1
print(name.rfind('e')) # 3
