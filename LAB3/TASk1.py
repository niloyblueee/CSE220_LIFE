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

# Task 01: Zigzag Walk

def walk_zigzag(floor):
    rowo = len(floor)
    if rowo % 2 == 0:
        for col in range (0, len(floor[0])):
            if col %2 == 0 :
                for row in range (0, len(floor), 2):
                    print(floor[row][col], end= " ")
            
            else:
                for row in range (len(floor)-1, -1, -2):
                    print(floor[row][col], end= " ")
            print()
    else:
        for col in range (0, len(floor[0])):
            if col %2 == 0 :
                for row in range (0, len(floor), 2):
                    print(floor[row][col], end= " ")
            
            else:
                for row in range (len(floor)-2, -1, -2):
                    print(floor[row][col], end= " ")
            print()


#DO NOT CHANGE THE CODE BELOW
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0'],
                  ['1' , '4' , '2' , '8' , '6']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9 1
# 1 2
# 4 7 2
# 4 9
# 1 8 6
print('################')
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9
# 1 2
# 4 7
# 4 9
# 1 8
