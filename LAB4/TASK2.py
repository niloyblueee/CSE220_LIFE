class Node:
    def __init__(self, value=None, next = None):
      self.value = value
      self.next = next

class HashTable:
    def __init__(self, length):
      n = Node()
      self.ht = [n] * length
      self.length = length

    def show(self):
      count = 0
      for i in self.ht:
        temp = i
        print(count, end=" ")
        while temp!=None:
         print (temp.value, end="-->")
         temp = temp.next
        count += 1
        print()


  #Do it by yourself
    def __hash_function(self, key):
      #mod by 3
      sum = 0
      if len(key)%2 == 0:
        for i in range(0,len(key),2):
          sum+= ord(key[i])

      else:
        for i in range(1,len(key),2):
          sum+= ord(key[i])

      return sum%len(self.ht)


  #Do it by yourself
    def insert(self, key, value):
      Tuple_pair = (key , value)
      Tuple_pair = tuple(Tuple_pair)
      Tuple_Node = Node(value=Tuple_pair)
      Hash_idx = self.__hash_function(key)
      
      if self.ht[Hash_idx].value is None:
       
        self.ht[Hash_idx] =  Tuple_Node 

      else:
        
        prev = self.ht[Hash_idx]
        current = self.ht[Hash_idx].next
        while prev:
          
          if prev.value[1] < value:

            Tuple_Node.next = prev
            self.ht[Hash_idx] = Tuple_Node
            return

          elif current is None:
            
            prev.next = Tuple_Node
            return 
        
          elif current.value[1] < value:
            prev.next = Tuple_Node
            Tuple_Node.next = current
            return

          else:
            prev = prev.next
            current= current.next



#Driver Code
ht = HashTable(3)


ht.insert("apple", 20)
ht.insert("coconut", 90)
ht.insert("cherry", 50)
ht.show()
print("------------")
ht.insert("banana", 30)
ht.insert("pineapple", 50)
ht.show()

# Driver Code Output:
# 0 ('coconut', 90)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->