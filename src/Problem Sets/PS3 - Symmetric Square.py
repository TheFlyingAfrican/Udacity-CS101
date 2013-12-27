# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(square):
    row_comp = []
    col_comp = []
    i = 0
    if len(square) == 0:
        symmetric = True
    else:
        symmetric = len(square) == len(square[0]) 
        while symmetric and i < len(square[0]):
            row_comp = square[i]
            for j in range(0, len(square[0])):
                col_comp.append(square[j][i])
            symmetric = symmetric and (row_comp == col_comp)
            col_comp = []
            i += 1
    return symmetric
    
 
print symmetric([[]])
print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False