# Ask user to input anything
user_input = input("Type anything: ")

# Remove all the spaces from input
user_input = user_input.replace(" ","")
print(user_input)

# if user_input is odd print True, else False
if len(user_input) % 2 == 0:
    print(False)
else: print(True)
