class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    # FIFO queue implementation using a singly linked list for storage.

    def __init__(self):
        # Create an empty queue.
        self.head = None
        self.tail = None
        self.size = 0  # number of queue elements

    def is_empty(self):  # This will return True if there is nothing in the queue
        if self.head is None:
            return True
        else:  # This will return False if there is something in the queue
            return False

    def len(self):
        # Return the number of elements in the queue.
        return self.size

    def first(self):
        # Return (but do not remove) the element at the front of the queue
        if self.head is None:
            return None
        print(self.head.data)  # This will print the first item in the list

    def dequeue(self):
        # Remove and return the first element of the queue (i.e., FIFO).
        if self.is_empty():  # This will check if the queue is empty and returns a Boolean variable
            print("Queue is empty")  # If the queue is empty
            return None
        else:
            temp = self.head.data  # If they detect something is in the queue then they would remove the first item in the queue and return that
            self.head = self.head.next
            self.head.prev = None
            print(temp)
            return temp

    def enqueue(self, data):  # This will take the queue and put a number to the back of the queue
        # Add an element to the back of queue
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def rotate(self):  # This function will take the head and put that element into the tail of the queue
        self.tail.next = self.head
        self.tail = self.head
        self.head = self.head.next

    def print(self):  # This will print what is in the Queue
        output = self.head
        s = "Current Queue: {"
        while output.next:
            if output.next == self.head:
                break
            s += str(output.data) + ", "
            output = output.next
        s += str(output.data) + "}"
        print(s)


queue = LinkedQueue()
queue.dequeue()  # print error message or throw exception
queue.enqueue(6)  # queue = 6
queue.print()
queue.enqueue(2)  # queue = 6->2
queue.print()
queue.enqueue(7)  # queue = 6->2->7
queue.print()
queue.dequeue()  # print 6 and queue = 2->7
queue.print()
queue.first()  # print 2 and queue = 2->7
queue.print()
queue.enqueue(1)  # queue = 2->7->1
queue.print()
queue.rotate()  # queue = 7->1->2
queue.print()
queue.enqueue(5)  # queue = 7->1->2->5
queue.print()

