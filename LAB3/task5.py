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

#Task 05: Game Arena

def play_game(arena):
    rows = len(arena)
    cols = len(arena[0]) 
    count = 0
    for i in range(rows):
        for j in range(cols):
            if arena[i][j]!=0 and arena[i][j] % 50 == 0:

                if i > 0 and arena[i-1][j] == 2:  
                    count += 1

                if i < rows - 1 and arena[i+1][j] == 2:  
                    count += 1

                if j > 0 and arena[i][j-1] == 2: 
                    count += 1

                if j < cols - 1 and arena[i][j+1] == 2:  

                    count += 1

    
    count*=2

    print(f"Points Gained: {count}")

    if count <= 10:
       print("Your Team is Out")
    else:
       print("Your team has survived the game.")


#DO NOT CHANGE THE CODE BELOW
arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 6. Your team is out.
print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 14. Your team has survived the game.