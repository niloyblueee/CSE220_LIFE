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


def find_Path(root, key):

    if root is None:
        return "NO PATH FOUND"

    if root.elem == key:
        return [root.elem]

    else:

        if key < root.elem:
            if not find_Path(root.left, key) == "NO PATH FOUND":
                return [root.elem] + find_Path(root.left, key)
            
            else:
                return "NO PATH FOUND"


        else:
            if not find_Path(root.right, key) == "NO PATH FOUND":
                return [root.elem] + find_Path(root.right, key)
            
            else:
                return "NO PATH FOUND"
            
            
#DRIVER CODE
arr = [None, 30, 10, 40, 3, 15, 35, 55]
root = tree_construction(arr)
#Write by yourself from the given tree


print(find_Path(root,15))
#This should print [30,10,15]

print(find_Path(root,50))
#This should print No Path Found