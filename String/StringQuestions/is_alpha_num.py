#

# isalpha will return True only when all string consist of letters. 

s = "Techtorial"
print(s.isalpha()) # True

s = "Techtorial Academy"
print(s.isalpha()) # False

s = ""
print(s.isalpha()) # False

# isnumeric will return True only when all string consists of numbers.

s = '0987654323456'
print(s.isnumeric()) # True

s = "3.5"
print(s.isnumeric()) # False because . is not a numerical character.

s = ""
print(s.isnumeric()) # False 


# isalnum method returns true when string only consists of letters and
# numbers. 

s = "a1d5ajds"
print(s.isalnum()) # True

s = "Python"
print(s.isalnum()) # True

s="1234"
print(s.isalnum()) # True

s=''
print(s.isalnum()) # False

s= '1 a'
print(s.isalnum()) # False because space is not a number nor is a letter.

s= '1!a'
print(s.isalnum()) # False because ! is not a number nor is a letter.