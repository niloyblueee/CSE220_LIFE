class BTNode:
    def __init__(self, elem):
        self.elem = elem
        self.right = None
        self.left = None

def MainSum(root):
    if root == None:
        return 0
    
    else:
        sum = root.elem + MainSum(root.left) + MainSum(root.right)
        return sum

def subtract_summation(root):
    return MainSum(root.left) - MainSum(root.right)



#Driver Code
root = BTNode(71)
#Write other nodes by yourself from the given tree of Doc File
root.left = BTNode(27)
root.left.left = BTNode(80)
root.left.left.left = BTNode(87)

root.left.right = BTNode(75)
root.left.left.right = BTNode(56)

root.right = BTNode(62)
root.right.right = BTNode(3)
root.right.right.right = BTNode(89)

root.right.left = BTNode(41)
root.right.right.left = BTNode(19)




print(subtract_summation(root)) #This should print 111