class BTNode:
    def __init__(self, elem):
        self.elem = elem
        self.right = None
        self.left = None

def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.elem, end = ' ')
    inorder(root.right)

def swap_child(root, level, M):
    if root == None:
        return 
    
    if level == M:
        return root
    
    else:
        temp = root.left
        root.left = root.right
        root.right = temp
        
        root.left = swap_child(root.left, level + 1, M)
        root.right = swap_child(root.right, level + 1, M)
        return root

        


#Driver Code
root =BTNode('A')
#Write other nodes by yourself from the given tree of Doc File
root.left = BTNode('B')
root.right = BTNode('C')

root.left.left = BTNode('D')
root.left.right = BTNode('E')
root.right.right = BTNode('F')

root.left.left.left = BTNode('G')
root.left.left.right = BTNode('H')

root.left.right.left = BTNode('I')
root.right.right.left = BTNode('J')

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()

root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
inorder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H