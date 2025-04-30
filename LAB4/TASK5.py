class Node:
    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next

class Stack:
    def __init__(self):
        self.__top = None

    def push(self, elem):
        nn = Node(elem, self.__top)
        self.__top = nn

    def pop(self):
        if self.__top == None:
            # print('Stack Underflow')
            return None
        e = self.__top
        self.__top = self.__top.next
        return e.elem

    def peek(self):
        if self.__top == None:
            # print('Stack Underflow')
            return None
        return self.__top.elem

    def isEmpty(self):
        return self.__top == None

def print_stack(st):  #fixed it was not working in VSCODE
    if st.isEmpty():
        print("Stack is empty")
        return
    
    # Temporary stack to hold elements
    temp_stack = Stack()
    
    # Print all elements in the stack
    while not st.isEmpty():
        elem = st.pop()
        print('|', elem, end=' ')
        if elem < 10:
            print(' |')
        else:
            print('|')
        temp_stack.push(elem)
    
    # Restore the original stack
    while not temp_stack.isEmpty():
        st.push(temp_stack.pop())

def remove_block(stack, n):
    tempStack = Stack()

    iter = 0
    for _ in range(n):
        tempStack.push(stack.pop())
        iter += 1
    tempStack.pop()

    for _ in range(iter - 1):
        stack.push(tempStack.pop())

# Test 01
print('Test 01')
st = Stack()
st.push(4)
st.push(19)
st.push(23)
st.push(17)
st.push(5)
print('Stack:')
print_stack(st)
print('------')
remove_block(st, 2)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

# Test 02
print('Test 02')
st = Stack()
st.push(73)
st.push(85)
st.push(15)
st.push(41)
print('Stack:')
print_stack(st)
print('------')
remove_block(st, 3)
print('After Removal')
print_stack(st)
print('------')