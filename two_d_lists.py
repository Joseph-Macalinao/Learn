'''
[
    123
    456
    789
]
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#to get 1 item, start with list (matrix), then go the line using index-base[0] (for top row), then [] for the index
#in that row
#matrix[0][1] will print 2

#print(matrix[1][1])

#changing value for an element in the list
matrix[1][1] = 45
print(matrix[1][1])
#45
for row in matrix:
    for number in row:
        print(number)