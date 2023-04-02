# Veera wants lose 10 pounds in one month. 
# There are multiple conditions to lose 10 pounds in a month 
# Veera needs to walk 10000 steps daily  OR needs to run at least
#  4 miles a day.  and Addition to these , Veera needs eat less 
#  than 1500 calories daily. 
#  We should create a program to calculate if Veera can 
#  loose weight or not.

daily_calory = 1700 
running_distance = 3
walking_steps = 12000

is_calory  = daily_calory < 1500
is_running = running_distance >= 4
is_steps   = walking_steps >= 10000

can_loose_weight = (is_steps or is_running) and is_calory



print("The Veera can loose weight",can_loose_weight)

#  Relate and operator with multiplication and relate or with addition.
# and operator has more precedence than or operator. Therefore,
# and operator will always be executed before or operator. 
# Unless parenthesis used for changing the order. 