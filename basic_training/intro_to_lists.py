# Storing a list of friends, each entry is indexed. Greta = 1, Nathan =2.
friends = ["Greta", "Nathan", "Tom", "Matt", "Adolf"]
lucky_numbrs = [4, 8, 15, 16, 23, 42]

print(friends)

# Print all elements after 1
print(friends[1:])

# Print a range of elements from the list, from 1 up to 3 but not including 3
print(friends[0:2])

# Append a list to the end of another lise
#friends.extend(lucky_numbrs)
#print(friends)

# Append an intem to the end of a list
friends.append("Geroge")
print(friends)

# Inset a value into a list
friends.insert(1, "Obama")
print(friends)

# Remove an element from a list
friends.remove("Obama")
print(friends)

# Count the elements within a list
print(friends.count("Obama"))

# Sort the friend list
friends.sort()
print(friends)

# Sort the lucky number list
lucky_numbrs.sort()
print(lucky_numbrs)

# Copy a list and make a new one
friends2 = friends.copy()
print(friends2)