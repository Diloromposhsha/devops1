# Using the input function ask the user to enter one sentence with three words
user_input = input("Enter one sentence with three words: ")

# Print the index number of each word's last character
# Print the sum of each index number that you found

prv_word_ind = 0
totals = 0
for item in user_input.split(" "):
     last_chr_ind = item.rindex(item[-1]) # using rindex() function instead of index() function, rindex() pick the real last index
     print(f"{last_chr_ind + prv_word_ind} is index number for {item[-1]}")
     totals = last_chr_ind + prv_word_ind + totals
     prv_word_ind = len(item) + prv_word_ind + 1

print(f"The sum is: {totals}")


# split(" ") = Importance of Human >> ["Importance", "of", "Human"] - (list of strings) - 3 items