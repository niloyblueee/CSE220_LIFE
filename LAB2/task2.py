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
def lengthOf(head):
    count = 0 
    pointer = head
    while pointer :
       count+=1
       pointer = pointer.next
    return count

def indexAt(head, idx):
    pointer = head
    n = 0
    if idx == 0 :
       return head
    else:
        while pointer:
            if n == idx :
                return pointer
            else:
               n+=1
               pointer = pointer.next


def word_Decoder(head):
    
    dummy = Node(None)
    length = lengthOf(head)
    index = []
    x = 13 % length

    for i in range(1, length):
        if x*i > length:
            break
        else:
           index.append(x*i)

    pointer = dummy

    while index!=[]:
       pointer.next = indexAt(head,index[-1])
       pointer = pointer.next 
       index.pop()
       pointer.next = None

    return dummy      
       
       
    


#Driver Code
print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head) #This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→C→A→T

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head) #This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→N