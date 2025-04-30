class BTNode:
    def __init__(self, elem):
        self.elem = elem
        self.right = None
        self.left = None

def sumOdd(root, idx):
  if root == None:
    return 0
  
  elif idx % 2 != 0 :
    return root.elem + sumOdd(root.left, idx + 1 ) + sumOdd(root.right, idx + 1 )
    
  else:

    return sumOdd(root.left, idx + 1 ) + sumOdd(root.right, idx + 1 )
   

def sumEven(root, idx):
  if root == None:
    return 0
  
  elif idx % 2 == 0 :

    return root.elem + sumEven(root.left, idx + 1 ) + sumEven(root.right, idx + 1 )
    
  else:

    return sumEven(root.left, idx + 1 ) + sumEven(root.right, idx + 1 )
  
   

def level_sum(root):
   return   sumEven(root, 1) - sumOdd(root,1) 

#DRIVER CODE
root = BTNode(1)
n2 = BTNode(2)
n3 = BTNode(3)
n4 = BTNode(4)
n5 = BTNode(5)
n6 = BTNode(6)
n7 = BTNode(7)
n8 = BTNode(8)
root.left = n2
root.right = n3

n2.left = n4
n3.left = n5
n3.right = n6

n5.left = n7
n5.right = n8


print(level_sum(root)) #This should print 4