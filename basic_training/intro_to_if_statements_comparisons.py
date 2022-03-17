
# Creating a function to identify the biggest number
def max_number(number1, number2, number3):
    # Is number one bigger than number 2 & 3?
    if number1 >= number2 and number1 >= number3:
        return number1
    # Is number two bigger than number 1 & 3?
    elif number2 >= number1 and number2 >= number3:
        return number2
    # If the 2 statements above are not true, then return number 3
    else:
        return number3

print(max_number(10, 2, 3))

# Equal too: ==
# Not equal: != 