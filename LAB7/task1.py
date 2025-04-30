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


def LCA(root, x, y):
    if root is None:
        return None
    
    if x <= root.elem and y >= root.elem:
        return root.elem
    
    elif x >= root.elem and y <= root.elem:
        return root.elem 
    
    else:
        if x < root.elem and y < root.elem:
            return LCA(root.left,  x, y)

        else:

            return LCA(root.right, x, y)


#DRIVER CODE

arr = [None, 15, 10, 25, 8, 12, 20, 30, 6, 9, None, None, 18, 22]
root = tree_construction(arr)


print(LCA(root, 6, 12))
print(LCA(root, 20, 6))
print(LCA(root, 18, 22))
print(LCA(root, 20, 25))
print(LCA(root, 10, 12)) 

#Write by yourself from the given tree (Create parent node and its corresponding left and right children nodes)
#check all the sample inputs given
#You can take help by seeing the driver code of Lab-6