#In one farm there are 28 cows and 101 chickens. 
# Create variables for cows and chickens .
# Create variables for leg of cows and chickens
# Then calculate total animal legs that are in 
# this farm using python code. 

cows = 28
chickens = 101

legs_of_a_cow = 4
legs_of_a_chicken = 2

total_chicken_legs = legs_of_a_chicken * chickens
total_cow_legs     = legs_of_a_cow * cows

total_legs = total_chicken_legs + total_cow_legs

print(total_legs)