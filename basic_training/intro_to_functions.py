# A function is a collection of code which performs a specific task
# code can be added to a function, then functions can be called again in the future

# All the code that comes after the below line will be within a function.
# For the code to be included within the function, it needs to be indented.
def say_hello():
    print("Hello there!")

def say_goodbye():
    print("Goodbye!")

# To run the function, we need to call the function. Type the name of the function and then ()
say_hello()
say_goodbye()


# Can specify that when a function is used, some parameters must be passed. The below requires name and age
def say_hello_again(name, age):
    print("Hello there " + name +", you are " + age)


# Calling the function and providing the required parameters.
say_hello_again("Oliver", "28")
say_hello_again("Greta", "23")