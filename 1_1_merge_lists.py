class Node:
    # constructor
    def __init__(self, data=None, next=None):  # This initializes the variables in the Node class
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):  # This initializes the variables in the LinkedList class
        self.head = None

    def insert(self, data):
        newnode = Node(data)  # Uses the class Node and puts it with data.
        if self.head is None:
            self.head = newnode  # This will insert the first node into the list
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newnode

    def merge(List_1, List_2):  # Takes in 2 lists as the parameters
        newlist = LinkedList()
        fakenode = Node(0)
        tail = fakenode
        firsthead = List_1.head  # Start a variable to get the first index of each list into the new variable
        secondhead = List_2.head
        while True:  # This is going to make both of the lists append to each other and sort in order
            if firsthead is None:
                tail.next = secondhead
                break
            if secondhead is None:
                tail.next = firsthead
                break
            if firsthead.data <= secondhead.data:
                tail.next = firsthead
                firsthead = firsthead.next
            else:
                tail.next = secondhead
                secondhead = secondhead.next
            tail = tail.next
        newlist.head = fakenode.next
        return newlist

    def printLL(self):  # This is the print function that will print the list
        current = self.head
        print("This is the Linked List: {", end=" ")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("}")


# Test merge() function
# Linked List of L
L = LinkedList()  # Creates the List of L
L.insert(3)
L.insert(6)
L.insert(9)
L.insert(14)
L.insert(17)
# Linked List of M
M = LinkedList()  # Creates the List of M
M.insert(2)
M.insert(8)
M.insert(15)
M.insert(19)
M.insert(22)
# Merge Function
LM = L.merge(M)
LM.printLL()
