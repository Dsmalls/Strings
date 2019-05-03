# Creating a string and converting into an Acronym
# Wide Area Network...WAN

orig_string = input("Convert to Acronym : ")

orig_string = orig_string.upper()

list_of_words = orig_string.split()

for word in list_of_words:
    print(word[0], end="")

print()


