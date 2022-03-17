# Creating an array containing some strings
friends = ["Max", "Tom", "Gaz", "Dom", "Lucie"]


# Print each string within the array
for friend in friends:    
    print (friend)

# Prints all numbers within the range listed, doesn't include last number in range
for index in range(100):
    print(index)

for index in range(len(friends)):
    print(friends[index])
    
    
# On the first iteration, print something. On all subsequent iterations, print something else.
for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")