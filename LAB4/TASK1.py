import fhm_unittest as unittest
import numpy as np
class Node_pair:
  def __init__(self, key, value, next = None):
    self.key, self.value, self.next = key, value, next


class Hashtable:
  def __init__(self, size):
    self.ht = [None]*size


  def insert(self, s):
    if self.search_hashtable(s) == 'Found':
      print(s,'Already Inserted. Cannot reinsert.')
      print('===============================')
      return
    hashed_index = self.__hash_function(s[0])
    pair = Node_pair(s[0], s[1])
    if self.ht[hashed_index] == None:
      self.ht[hashed_index] = pair
    else:
      pair.next = self.ht[hashed_index]
      self.ht[hashed_index] = pair


  def create_from_array(self, arr):
    for i in arr:
      self.insert(i)

  def print_hashtable(self):
    idx = 0
    for i in self.ht:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'(key: {head.key}, value: {head.value})', end = '-->')
        head = head.next
      print('None')
      print()
      idx += 1


  #Do it by yourself
  def __hash_function(self, key):
    #TO DO
    # has to be moded with 5 as length is 5 in the driver code
    keyM = key
    if len(keyM)%2 == 0:
    
        store = 0    
        for i in range(0,len(keyM),2):
            store += int(str(ord( keyM[i])) + str(ord(keyM[i+1] )))

        return store%len(self.ht)
    
    else:
        store = 0 
        keyM+="N"
        for i in range(0,len(keyM),2):

            store += int(str(ord( keyM[i])) + str(ord(keyM[i+1] )))

        return store%len(self.ht)


  #Do it by yourself
  def search_hashtable(self, s):
    #TO DO 
    if self.ht[self.__hash_function(s[0])] == None:
        
        return "Not Found"

    else:
          temp = self.ht[self.__hash_function(s[0])]
#

          while temp:

              if temp.key == s[0] and temp.value == s[1]:
                return "Found"
              
              else:
                 temp = temp.next
          return "Not Found"
          
#Driver Code
arr = [('Colt', 360), ('Cordelius', 730), ('Shelly', 300), ('Doug', 1200), ('Emz', 520), ('Bo', 580)]
ht = Hashtable(5)
ht.create_from_array(arr)
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Doug', 1200))
unittest.output_test(result, 'Found')
print(f'(Doug, 1200) {result}')

print('======================')
ht.insert(('Doug', 1200))
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Edgar', 320))
unittest.output_test(result, 'Not Found')
print(f'(Edgar, 320) {result}')

print('======================')
ht.insert(('Edgar', 320))
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Edgar', 320))
unittest.output_test(result, 'Found')
print(f'(Edgar, 320) {result}')