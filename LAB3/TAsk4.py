import fhm_unittest as unittest
import numpy as np

def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))
#====================================================================================================================================================================================================================





#Task 04: Matrix Compression

def compress_matrix(mat):
   
    rows = len(mat)
    cols = len(mat[0]) 
    Res_rows = rows // 2
    Res_cols = cols // 2
    Res_matrix = np.zeros((Res_cols,Res_rows),dtype=object)
    
    for i in range(0, rows, 2):
        for j in range(0, cols, 2):
            Res_matrix[i//2][j//2] = mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]
    
    return (Res_matrix)

#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
print("...............")
returned_array=compress_matrix(matrix)
print_matrix(returned_array)
#This should print

#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------