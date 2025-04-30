import fhm_unittest as unittest
import numpy as np

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


#==============================================================================================================

def alternate_merge(head1, head2):
  #TO DO
    curr1 = head1
    curr2 = head2

    while curr1.next and curr2.next:
        temp1, temp2 = curr1.next, curr2.next
        curr1.next = curr2
        curr2.next =temp1
        curr1, curr2 = temp1, temp2

    if curr1.next:
        temp = curr1.next
        curr1.next = curr2
        curr2.next = temp
        
    else:
        curr1.next = curr2 

    return (head1)

print('==============Test Case 1=============')
head1 = createList(np.array([1,2,6,8,11]))
head2 = createList(np.array([5,7,3,9,4]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    1 --> 5 --> 2 --> 7 --> 6 --> 3 --> 8 --> 9 --> 11 --> 4


print('==============Test Case 2=============')
head1 = createList(np.array([5, 3, 2, -4]))
head2 = createList(np.array([-4, -6, 1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    5 → -4 -> 3 → -6 -> 2 -> 1 -> -4


print('==============Test Case 3=============')
head1 = createList(np.array([4, 2, -2, -4]))
head2 = createList(np.array([8, 6, 5, -3]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print   4-> 8 → 2-> 6 → -2 → 5 → -4 -> -3
