# += /= *= **= %= //=

# var+=10 # var = var + 10 


#Lines above will generate an error because variable name var 
# is not defined yet

num = 11

num+=2

print(num) # 13

num/=2 # -> num = num / 2
print(num) # 6.5

num*=2
print(num) # 13

num//=4
print(num) # 3

num%=10 # num = num % 10

print(num) # 3

# exponentiation is used to find power of numbers. 
number = 2 ** 3 # 2 * 2 * 2
print(number) # 8


num**=2 # num = num**2   num = 3 ** 2 -> 3 * 3

print(num) # 9




print(11/2)