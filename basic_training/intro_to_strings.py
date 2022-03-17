# Printing a string
print("this is an example of a string.")

# Printing some of the string on a new line using \n
print("this is an example of a\nstring.")

# Printing a quotation mark within a string
print("this is an example of a\"string.")

# Storing a string as a phrase
phrase = "Storing a string as a PHRASE"
#  Index  0123456789          
print(phrase)

# Concatination
print(phrase + " and adding another string to it") 

## Functions with strings##

# Printing a string all in lowercase
print(phrase.lower())

# Printing a string all in uppercase
print(phrase.upper())

# Checking wheter a string is all in uppercase, returns a boolean
print(phrase.isupper())

# Functions can be used one after the other.
# Convering the string to uppercase & checking it's upper, returns a boolean
print(phrase.upper().isupper())

# Identifying the number of chars in a string, returns integer
print(len(phrase))

# Find the first character and return it, strings are indexed starting with 0
print(phrase[0])

# Identify the index of a string within the string, search for a
print(phrase.index("a"))

# Replacing words within a string with something else, replacing string with new string
print(phrase.replace("string", "new string"))

