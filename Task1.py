import fhm_unittest as unittest
import numpy as np

def mergeSortedArray(arr1, arr2):
    x = (len(arr1)+len(arr2))
    mainArr = np.zeros(x,dtype=int)
    idx1 = 0
    idx2 = 0
    idx3 = 0
    while idx1 < len(arr1) and idx2 < len(arr2):

      if arr1[idx1] < arr2[idx2] :
      
        mainArr[idx3] = arr1[idx1]
        idx1 += 1
      else:
        mainArr[idx3] = arr2[idx2]
        idx2 +=1
      idx3 += 1  

    if idx1 < len(arr1) :
      for i in arr1[idx1: ]:
        mainArr[idx3] = i
        idx3 += 1   

    else:
      for i in arr2[idx2: ]:
        mainArr[idx3] = i
        idx3 += 1   

    
    return mainArr                                                  

                     #remove this line when you're done with the method

a1 = np.array([1, 2, 3])
print(f'Sorted Array 1: {a1}')
a2 = np.array([2, 5, 6])
print(f'Sorted Array 2: {a2}')
returned_value = mergeSortedArray(a1, a2)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 2, 3, 5, 6]
unittest.output_test(returned_value, np.array([1, 2, 2, 3, 5, 6]))

print('\n==================================\n')

a3 = np.array([1, 3, 5, 11])
print(f'Sorted Array 3: {a3}')
a4 = np.array([2, 7, 8])
print(f'Sorted Array 4: {a4}')
returned_value = mergeSortedArray(a3, a4)
print(f'Merged Sorted Array: {returned_value}\n') # This should print [1, 2, 3, 5, 7, 8, 11]
unittest.output_test(returned_value, np.array([1, 2, 3, 5, 7, 8, 11]))