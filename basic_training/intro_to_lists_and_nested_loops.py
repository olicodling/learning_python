# Creating a nested list, a list containing lists.
# It contains a grid with 4 rows, 3 columns.

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Accessing the number's within the grid above using the index of
# the first the row & then the column.
print(number_grid[0][0])

for row in number_grid:
    for col in row:
        print(col)
