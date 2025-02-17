import fhm_unittest as unittest
import numpy as np
#Run this cell

class Node:
    def __init__(self,elem,next = None):
        self.elem,self.next = elem,next

def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1,len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = newNode
    return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()


def sum_dist(head, arr):
  #TO DO
    sum = 0
    flag = True
    for i in  arr:
        curr = head
        flag = True
        for _ in range(i):
            if curr.next:
                curr = curr.next  
            else:
               flag = False 
               break
               
        sum += curr.elem if  flag  else 0     
       

    return sum



         

#[DO NOT MODIFY THE TESTER CODES BELOW]
#[THERE WILL BE 50% PENALTY IF IT'S MODIFIED]
print('==============Test Case 1=============')
LL1 = createList(np.array([10,16,-5,9,3,4]))
dist = np.array([2,0,5,2,8])
returned_value = sum_dist(LL1, dist)
print(f'Sum of Nodes: {returned_value}') #This should print Sum of Nodes: 4
unittest.output_test(returned_value, 4)
print()