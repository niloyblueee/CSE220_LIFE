import fhm_unittest as unittest
import numpy as np

#DO NOT CHANGE THE CODE BELOW
#You must run this cell to print matrix and for the driver code to work
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

#Task 02: Decryption Process

def decrypt_matrix(matrix):
    sumArr = np.zeros(len(matrix[0])-1)
    
    

    for col in range (0, len(matrix[0])):
        if col%2 == 0:
            sum1 = 0
            for row in range (0, len(matrix)):
               sum1 += matrix[row][col]
            if not col == 0 :
                sumArr[col-1] = sum1 - sum2  
        else:
            sum2 = 0
            for row in range (0, len(matrix)):
                sum2 += matrix[row][col]

            sumArr[col - 1 ] = sum2 - sum1
    return sumArr
#DO NOT CHANGE THE CODE BELOW
matrix=np.array([[1,3,1],
                [6,4,2],
                [5,1,7],
                [9,3,3],
                [8,5,4]
                ])

returned_array=decrypt_matrix(matrix)
print(returned_array)
#This should print [-13, 1]