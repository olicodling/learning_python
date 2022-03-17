# Return statements are used to obtain information from a function. 
# The return function returns data from a function.



def cube(number):
    number*number*number

def cubey(number):
    return number*number*number

# This will return nothing as we haven't used the return statement
print(cube(3))
# This will return the answer we're looking for 
print(cubey(3))

#Storing the value from the function as a variable & printing it
result = (cubey(3))
print(result)