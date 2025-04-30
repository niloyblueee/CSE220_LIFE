# YOU MUST RUN THIS CELL
import fhm_unittest as unittest
# BUT DO NOT modify the CODE in this cell
class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  def __init__(self):
    self.__top = None

  def push(self,elem):
    nn = Node(elem,self.__top)
    self.__top = nn

  def pop(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    e = self.__top
    self.__top = self.__top.next
    return e.elem

  def peek(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    return self.__top.elem

  def isEmpty(self):
    return self.__top == None
  
def diamond_count(stack,string):
    stackLeft = Stack()
    DumRight  = Node(None,None)
    
    iter = 0
    for i in string:
      iter +=1
      stack.push(i)

    RCount = 0
    LCount = 0
    for _ in range(iter):
      
      if stack.peek() == ">" :
        DumRight.next = stack.pop()
  
        RCount+= 1

      elif  stack.peek() == "<":
        stackLeft.push(stack.pop())
        LCount +=1

      else:
        stack.pop()

    if LCount < RCount :

      return LCount
    
    else:

      return RCount






print('Test 01')
stack = Stack()
string = '<..><.<..>> '
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')


print('Test 02')
stack = Stack()
string = '<<<..<......<<<<....>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 1
unittest.output_test(returned_value, 1)
print('-----------------------------------------')


print('Test 03')
stack = Stack()
string = '>>><...<<..>>...>...>>>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
unittest.output_test(returned_value, 3)
print('-----------------------------------------')