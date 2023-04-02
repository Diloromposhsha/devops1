ingredients = input("Input 3 ingredients: \n")
num = input("Input any number: \n")

"""
## Need To Learn below ##
# num = int(num)
# item_new = []
# for item in ingredients.split(" "):
#     item_new.append(item.replace(item[0],str(num),1))
#     num = num + 1
# print(' '.join(item_new))
"""

print(ingredients.replace("M",num).replace("P",str(int(num)+1)).replace("S",str(int(num)+2)))
