num = 19

# 
print(type(num)) # <class 'int'>

# After the division operator
new_var = num / 3 # 7

print(type(new_var)) #class 'float'

# Since the result of division(/) operator is not guarenteed to be 
# whole number, python will always assign result of / operator 
# with a float number.
#-------------------------------------

result_floor = num // 3
print(type(result_floor)) # int type

#-------------------------------------

result_intFloat = 3.0 + 5

print(type(result_intFloat))

# Any arithmetic operator between float and a integer will result in 
# float type.


#-------------------------------------
c = 3+0j

print(type(c)) # <class 'complex'>

#-------------------------------------

ex = "A text"

print(type(ex)) # <class 'str'>