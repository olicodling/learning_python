# Definging a boolean variable
is_male = False
is_tall = True

# If is_male is true then do some stuff
#if is_male:
#    print("you are a male")

# if is_male or is_tall are true then do some stuf
#if is_male or is_tall:
#    print("You are either a male or are tall")
#else:
#    print("you are not a male and you're not tall")


# Is this person a male or are they tall?
if is_male and is_tall:
    print("You're either a male or are tall")
# Is this person a man and not tall?    
elif is_male and not(is_tall):
    print("You're a short male")
# Is this person not a man and is tall?
elif not(is_male) and is_tall:
    print("You're a tall non-male")
# This person is neither a man nor tall
else:
    print("you're not a male and you're not tall")

