random_word = input("Enter a random word: ")
number_of_letter = input("Enter number of letter that word consists ")

if int(number_of_letter) == len(random_word): 
    print(True)
else: 
    print(False)

index_letter = input("Enter a letter that you want to find an index ")
print(random_word.index(index_letter))