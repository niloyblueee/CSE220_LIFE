class MaxHeap:
    def __init__(self, cap, arr=None):
        self.__cap = cap
        self.__arr = [None] * (cap + 1)
        self.__size = 0

        if arr:
            for val in arr:
                self.insert(val)

    def insert(self, element):
        if self.__size >= self.__cap:
            print("Heap is full")
            return

        self.__size += 1
        self.__arr[self.__size] = element
        self.swim(self.__size)

    def delete(self, element):
        if self.__size == 0:
            print("MAKE A HEAP")
            return

        goner_idx = self.__arr.index(element)
        self.__arr[goner_idx], self.__arr[self.__size] = self.__arr[self.__size], self.__arr[goner_idx]
        self.__arr[self.__size] = None
        self.__size -= 1
        self.sink(goner_idx)

    def sink(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1
        temp_idx = idx

        if left_idx < self.__size and self.__arr[left_idx] is not None:
            if self.__arr[temp_idx] < self.__arr[left_idx]:
                temp_idx = left_idx

        if right_idx < self.__size and self.__arr[right_idx] is not None:
            if self.__arr[temp_idx] <= self.__arr[right_idx]:
                temp_idx = right_idx

        if temp_idx != idx:
            self.__arr[idx], self.__arr[temp_idx] = self.__arr[temp_idx], self.__arr[idx]
            self.sink(temp_idx)

    def swim(self, child_idx):
        parent_idx = child_idx // 2

        if parent_idx == 0:
            return

        if self.__arr[parent_idx] is not None and self.__arr[child_idx] is not None and self.__arr[parent_idx] < self.__arr[child_idx]:
            self.__arr[parent_idx], self.__arr[child_idx] = self.__arr[child_idx], self.__arr[parent_idx]
            self.swim(parent_idx)

    def extractMax(self):
        max_val = self.__arr[1]
        self.delete(max_val)
        return max_val


    def sort(self):
        result = []
        original_size = self.__size
        original_arr = self.__arr[:]

        while self.__size > 0:
            result.append(self.extractMax())

        self.__arr = original_arr
        self.__size = original_size

        return result

    def display(self):
        print("Heap:", self.__arr[1:self.__size + 1])


if __name__ == "__main__":
    heap = MaxHeap(10)

    # Inserting elements
    for val in [5, 3, 8, 1, 4]:
        heap.insert(val)
        heap.display()

    # Extract maximum
    print("\nExtracted max:", heap.extractMax())
    heap.display()

    # Delete a specific element
    heap.delete(4)
    print("\nAfter deleting 4:")
    heap.display()

    # Extract max again
    print("\nExtracted max:", heap.extractMax())
    heap.display()

    # Sort the heap
    print("\nSorted elements:", heap.sort())
    heap.display()

