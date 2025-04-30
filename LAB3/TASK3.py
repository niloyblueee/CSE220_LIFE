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
# Task 03: Row Rotation Policy of BRACU Classroom



def row_rotation(exam_week, seat_status):
    col = len(seat_status[0])
    row = len(seat_status)

    for _ in range( exam_week -1 ):  
        dummy = np.zeros((row, col), dtype=object)  
        
        for i in range(row - 1, 0, -1):
            dummy[i] = seat_status[i - 1]  

        dummy[0] = seat_status[row-1]
        seat_status = np.array(dummy) 
    
    final_idx = 1
    for i in seat_status:
        
        if "AA" in i:
        
            break
        
        else:
            final_idx +=1 if (final_idx + 1) <=row else  1

    return(f" {final_idx} \n{seat_status}")


#DO NOT CHANGE THE CODE BELOW
seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3
print_matrix(seat_status)
print()

row_number=row_rotation(exam_week, seat_status) #This should print modified seat status after rotation and return the row number
print(f'Your friend AA will be on row {row_number}') #This should print Your friend AA will be on row 2