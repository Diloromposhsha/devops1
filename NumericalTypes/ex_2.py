
# The three digit number created below
num = 347
# Create a python code to find product of digits from that number.
# The code created should work
#  even the value of the variable num changes

# 2 % 10 -> 2
# 15 % 10 -> 5
# 103 % 10 -> 3
# 143 % 10 -> 3
# 97 % 10 -> 7
# When we find remainder with 10 we always get last digit 
# from that number
# To be able to find last digit of variable num
last_digit = num % 10

# 17 // 10 -> 1
# 100 // 10 -> 10
#150 // 10 -> 15
# 237 // 10 -> 23

# To get rid of the last digit from the number I should use floor 
# division by 10 

fist_two_digits = num // 10
#34
middle_digit = fist_two_digits%10
#4
first_digit = fist_two_digits // 10
#3

print(first_digit*middle_digit*last_digit)