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

def getPrev(head):
    prev = None
    curr = head
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def idGenerator(head1, head2, head3):
    dummy = Node(None)
    dummy.next = getPrev(head1)
    pointer = dummy
    while pointer.next:
        pointer = pointer.next 

    curr2 , curr3 = head2 , head3
    while curr2 and curr3:
        
        if curr2.elem + curr3.elem >= 10 :
            
            pointer.next = Node((curr2.elem + curr3.elem)%10)
        
        else:    

            pointer.next = Node(curr2.elem + curr3.elem)

        curr2, curr3 = curr2.next , curr3.next
        pointer = pointer.next
    dummy = dummy.next
    return dummy    

print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2


print('==============Test Case 2=============')
head1 = createList(np.array([0,3,9,1]))
head2 = createList(np.array([3,6,5,7]))
head3 = createList(np.array([2,4,3,8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5