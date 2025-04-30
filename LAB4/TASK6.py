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

def conditional_reverse(stack):
    Out_Stack = Stack()

    while stack.peek() != None:
        if stack.peek() != Out_Stack.peek():
            Out_Stack.push(stack.pop())

        else:
            stack.pop()    
    return Out_Stack


print('Test 01')
st=Stack()
st.push(10)
st.push(10)
st.push(20)
st.push(20)
st.push(30)
st.push(10)
st.push(50)
print('Stack:')
print_stack(st)
print('------')
reversed_stack=conditional_reverse(st)
print('Conditional Reversed Stack:')
if reversed_stack==None:
    print("Incomplete Task")
else:
    print_stack(reversed_stack) # This stack contains 50, 10, 30, 20, 10 in this order whereas top element should be 10
print('------')