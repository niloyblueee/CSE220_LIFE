import numpy as np

def mostWater(height):
    #len(array) - index == length of rectangle
    max = 0
    for index in range(len(height)):
        length_of_rectangle = 1
        
        for element in range (index+1, len(height)):
            
            if height[index] < height[element]:
                if max < (height[index] * length_of_rectangle):
                   max = height[index] * length_of_rectangle  

            else:
                if max < (height[element] * length_of_rectangle):
                    max = height[element] * length_of_rectangle   
                
            length_of_rectangle += 1             
    print(max)        

height = np.array([1,8,6,2,5,4,8,3,7])
print(f'Given Array: {height}')

print(f'\nExpected Output: 49')
print(f'Your Output: ',end='')
mostWater(height)