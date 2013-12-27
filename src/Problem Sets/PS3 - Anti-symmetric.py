# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(square):
    row_comp = []
    col_comp = []
    i = 0
    if len(square) == 0:
        anti_symmetric = True
    else:
        anti_symmetric = len(square) == len(square[0]) 
        while anti_symmetric and i < len(square[0]):
            row_comp = square[i]
            for j in range(0, len(square[0])):
                col_comp.append(-square[j][i])
            anti_symmetric = anti_symmetric and (row_comp == col_comp)
            col_comp = []
            i += 1
    return anti_symmetric


# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
