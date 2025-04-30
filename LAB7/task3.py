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


def sum_of_leaves(root, sum):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return root.elem

    else:
        sum = sum_of_leaves(root.left, sum ) + sum_of_leaves(root.right, sum)
        return sum

#DRIVER CODE
#Write by yourself from the given tree
arr = [None, 30 , 10 ,40 , 3 , 15, 35, 55, 2, None, None, None , None, 36, None, None]
root = tree_construction(arr)

print(sum_of_leaves(root, 0))