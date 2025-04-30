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

def tree_construction(arr, i = 1):
    if i>=len(arr) or arr[i] == None:
        return None
    p = BTNode(arr[i])
    p.left = tree_construction(arr, 2*i)
    p.right = tree_construction(arr, 2*i+1)
    return p

def smallest_level(root, level = {}, i = 0):
    if root == None:
        return 
    
    else:
        if i not in level :
            level[i] = root.elem

        else:
            if level[i] > root.elem:
                level[i] = root.elem 
        root.left = smallest_level(root.left, level, i +  1)
        root.right = smallest_level(root.right , level , i + 1)

        return level
#DRIVER CODE
root = tree_construction([None, 4,9,2,3,-5,None,7])
print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  3 9 5 4 2 7
print()
print('Level Wise Smallest Value: ', end = ' ')
print(smallest_level(root)) #Level Wise Smallest Value:  {0: 4, 1: 2, 2: -5}