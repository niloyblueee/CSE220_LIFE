class MinHeap:
    def __init__(self, cap, arr=None):
        self.__cap = cap
        self.__arr = [None] * (cap + 1)  
        self.__size = 0

        if arr:
            for val in arr:
                self.insert(val)


    def insert(self,element):
        if self.__size >= self.__cap:
            print("Heap is full")
            
        self.__size += 1
        self.__arr[self.__size] = element
        self.swim(self.__size)


    def delete (self,element):
        if self.__size == 0 :
            print("MAKE A HEAP")
        Goner_idx = self.__arr.index(element)
        self.__arr[Goner_idx], self.__arr[self.__size] = self.__arr[self.__size] , self.__arr[Goner_idx]
        self.__arr[self.__size] = None
        self.__size -= 1
        self.sink(Goner_idx)


    def sink(self,Goner_idx):
        
        left_idx = Goner_idx*2
        right_idx = Goner_idx*2 + 1
        temp_idx = Goner_idx 

        if left_idx <  len(self.__arr) and self.__arr[left_idx] is not None:
            
            if self.__arr[temp_idx] > self.__arr[left_idx]:
                temp_idx = left_idx

        if right_idx <  len(self.__arr) and self.__arr[right_idx] is not None:

            if self.__arr[temp_idx] >= self.__arr[right_idx]:
                temp_idx = right_idx
        
        if temp_idx != Goner_idx:
            self.__arr[Goner_idx], self.__arr[temp_idx] = self.__arr[temp_idx] , self.__arr[Goner_idx]
            self.sink(temp_idx)
    

    def swim(self,child_idx):
        parent_idx = child_idx  // 2
        
        if parent_idx == 0 :
            return

        if self.__arr[parent_idx] is not None and self.__arr[child_idx] is not None and self.__arr[parent_idx] > self.__arr[child_idx]:
            self.__arr[parent_idx], self.__arr[child_idx] = self.__arr[child_idx], self.__arr[parent_idx]
            self.swim(parent_idx)

    def sort(self):
        result = []
        original_size = self.__size
        original_arr = self.__arr

        while self.__size > 0:
            result.append(self.extractMin())

        self.__arr = original_arr
        self.__size = original_size

        return result

    def extractMin(self):
        min = self.__arr[1]
        self.delete(min)
        return   min
    
    def display(self):
        print("Heap:", self.__arr[1:self.__size + 2 ])

    def ProcessTime(self, element):
        temp = self.extractMin()
        print(f"Extracted {temp} \n")
        print("after extraction")
        self.display()

        self.insert(temp + element)
        print(f"After Insertion:") 
        self.display()
        print()
        
if __name__ == "__main__":
    m = 4
    arr = [0]*m
    heap = MinHeap(m, arr)
    heap.ProcessTime(2)
    heap.ProcessTime(4)
    heap.ProcessTime(7)
    heap.ProcessTime(1)
    heap.ProcessTime(6)