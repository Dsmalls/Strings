#===============String Methods===================
rand_string = "   this is an important string    "

# Deletes white or black space
rand_string = rand_string.lstrip() # deletes white space on left
rand_string = rand_string.rstrip() # deletes white space in right

# Capitalize first letter
print(rand_string.capitalize())

# Capitalize all the letters
print(rand_string.upper())

# lowercase all letters
print(rand_string.lower())

# Turning a list into a string and separating the items
a_list = ["Tons", "of", "long, random", "words"]
print(" ".join(a_list))

# String into a list
a_list_2 = rand_string.split()
for j in a_list_2:
    print(j)

# Count how many times a string occurs
print("How many is :", rand_string.count("is"))
print("====================================================")

letter_z = "z"
num_3 = "3"
a_space = " "

# Returning true if chars are letters or nums
# Whitespace is false
print("Is z a letter or number :", letter_z.isalnum())

print("Is z a letter :", letter_z.isalpha())

print("Is 3 a number :", num_3.isdigit())

print("Is z a lowercase :", letter_z.islower())

print("Is space a space :", a_space.isspace())
