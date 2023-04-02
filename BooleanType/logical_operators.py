
b1 = True
b2 = False

print(b1 and b2)   # False

print(b1 and True) # True

print(b2 and b2)   # 


# I want to see if I can go eat today.
# I have given parameters which are money, if i have time

have_time =  False
have_money = True

can_i_go = have_time and have_money

print("Value of variable can_i_go is",can_i_go) #True

# I need to exercise every day. To be able to exercise 
# every day I have to check 2 parameters which are if I have gym card
# or gym equipment at home. In both times I can exercise daily

have_gym_eq =   False
have_gym_card = True

can_I_exercise = have_gym_eq or have_gym_card

print("Value of variable can_I_exercise is",can_I_exercise)
# True


# not operator
# makes boolean value take the opposite value in an equation.


b2 = True

print(b2 and not False)
#WHat shouyld be the output? 
#True

print(not b2 and True)
print("The value of b2 is",b2)
#What shouyld be the output? 
# 1: False
# 2: The value b2 is True
#Note: b2 didn't change its value because boolean is an immutable
# type, which means value will be protected unless reassigned.



