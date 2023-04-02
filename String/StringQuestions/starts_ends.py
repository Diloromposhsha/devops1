s1 = "AI is future!!"
s2 = "future!!"

print(s1.endswith("future")) # False

print(s1.endswith(s2)) # -> True

print(type(s1.endswith(s2))) # <class 'bool'>

# startswith method will only return true if the string starts with
# given parameter
s1 = "AI is future!!"

print(s1.startswith("Another string")) # False

print(s1.startswith("A")) # True

print(s1.startswith("AI is fut")) # True

print(s1.startswith("ai")) # False
print(s1.endswith("FUTURE!!")) #False
# Both starts and endswith method are case sensitive. 


