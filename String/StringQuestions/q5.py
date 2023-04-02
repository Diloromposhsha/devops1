# Ask user to give two string values and 
# print True 
# if the second string starts with 
# last two charachters 
# of the first string OR print True 
# if the first string starts with
# first two charachters of the second string.

# 'example'

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
# Last two chs of the s1
last_two_s1 = s1[-2:]

condition1 = s2.startswith(last_two_s1)

#first two charachters of the second string.
first_two_s2 = s2[:2]

condition2 = s1.startswith(first_two_s2)

end_result = condition1 or condition2

print(end_result)