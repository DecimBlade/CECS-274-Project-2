class Node:
    def __init__(self, data):  # Initializes the variables
        self.data = data
        self.next = None


class CreateList:

    def __init__(self):  # Initializes the variables
        self.head = 0
        self.tail = 0

    def add(self, data):  # This add function will add the data into the list
        node = Node(data)  # This takes in 2 parameters
        if self.head == 0:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.next = self.head
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head

    # This function will print the nodes of circular linked list from the head
    def print(self):  # This takes in self and makes the print statement
        temp = self.head
        print("List: { ", end="")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("}")

    # This function will count the nodes of circular linked list
    def countNodes(self):  # This function counts the number of nodes in the list and will return the number of nodes in a print statement
        numberofnodes = 0
        temp = self.head
        while True:
            numberofnodes += 1
            temp = temp.next
            if temp == self.head:
                break
        print("Number of nodes:", numberofnodes)


class CircularLinkedList:
    cl = CreateList()
    # Adds data to the list
    cl.add(4)
    cl.add(5)
    cl.add(7)
    cl.add(8)
    cl.add(12)
    cl.add(56)
    cl.add(85)
    cl.add(41)
    # Displays all the nodes present in the list
    cl.print()
    cl.countNodes()
