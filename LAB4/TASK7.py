# YOU MUST RUN THIS CELL
# BUT DO NOT modify the CODE in this cell
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# YOU MUST RUN THIS CELL
# BUT DO NOT modify the CODE in this cell
class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, elem):
        new_node = Node(elem)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        removed_elem = self.front.elem
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_elem

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.front.elem

    def is_empty(self):
        return self.front is None

    def display_queue(self):
        print("Queue (front to rear):", end=" ")
        current = self.front
        while current:
            print(f"{current.elem} ->", end=" ")
            current = current.next
        print("NULL")

class CallQueue:
    def __init__(self):
        self.vip_queue = LinkedListQueue()
        self.regular_queue = LinkedListQueue()

    def enqueue_call(self, customer_id, is_vip):
        #To Do
        if is_vip:
            self.vip_queue.enqueue(customer_id)
            print(f"Customer {customer_id} added to VIP queue.")
            print()

        else:
            self.regular_queue.enqueue(customer_id)
            print(f"Customer {customer_id} added to Regular queue.")
            print()

    def dequeue_call(self):

        if self.vip_queue.is_empty() and self.regular_queue.is_empty() == False:

            print(f"Processing Regular Customer {self.regular_queue.dequeue()}.")
            print()

        elif self.vip_queue.is_empty() and self.regular_queue.is_empty() :
            print("No calls in the queue.")
            print()

        else:
            print(f"Processing VIP Customer {self.vip_queue.dequeue()}.")
            print()

    def display_queue(self):
        
        print("VIP Queue:")
        self.vip_queue.display_queue()
        print()

        print("Regular Queue:")
        self.regular_queue.display_queue()


# YOU MUST RUN THIS CELL TO TEST YOUR CODE
# If you modify the method calls the outputs will be changed as well
call_center = CallQueue()
# Enqueueing customers
call_center.enqueue_call(101, False)  # Regular customer
call_center.enqueue_call(201, True)   # VIP customer
call_center.enqueue_call(102, False)  # Regular customer
call_center.enqueue_call(202, True)   # VIP customer
call_center.enqueue_call(103, False)  # Regular customer

call_center.display_queue()

# Processing calls
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()
call_center.dequeue_call()  # No more calls

call_center.display_queue()

#   ::Expected Ouput::

# Customer 101 added to Regular queue.
# Customer 201 added to VIP queue.
# Customer 102 added to Regular queue.
# Customer 202 added to VIP queue.
# Customer 103 added to Regular queue.

# VIP Queue:
# Queue (front to rear): 201 -> 202 -> NULL
# Regular Queue:
# Queue (front to rear): 101 -> 102 -> 103 -> NULL

# Processing VIP Customer 201.
# Processing VIP Customer 202.
# Processing Regular Customer 101.
# Processing Regular Customer 102.
# Processing Regular Customer 103.
# No calls in the queue.

# VIP Queue:
# Queue (front to rear): NULL
# Regular Queue:
# Queue (front to rear): NULL