import numpy as np
from base import BaseList


class DLList(BaseList):
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):  # Initializes all the variables
        self.n = 0
        self.d = DLList.Node(None)
        self.d.prev = self.d
        self.d.next = self.d

    def get_node(self, i: int) -> Node:  # if the integer is less than the n/2 then it will go to next
        if i < self.n / 2:  # This function is to get the node when you call it in the get, set, remove, and add functions
            p = self.d.next
            for x in range(i):
                p = p.next
        else:
            p = self.d
            for x in range(self.n - i):
                p = p.prev
        return p

    def get(self, i: int):  # If the integer is less than 0 or more than what's in self then it will raise an Index Error
        if i < 0 or i >= self.n: raise IndexError()
        return self.get_node(i).x

    def set(self, i: int, x):  # This will set the index entered, the number that was given second
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def _remove(self, w: Node):  # This will remove the element at that index in the list
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    def remove(self, i: int):  # If there was nothing in the list then it will print Nothing to remove
        if i < 0 or i >= self.n:
            print("ERROR")
        else:
            self._remove(self.get_node(i))

    def add_before(self, w: Node, x):  # This inserts the node in the middle of the list
        u = DLList.Node(x)  # It takes node u and insert it before node w
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n = self.n + 1
        return u

    def add(self, i: int, x):  # This will add the integer to position x and add it to the beginning of the list
        self.add_before(self.get_node(i), x)

    def __iter__(self):  # this initializes some of the functions
        u = self.d.next
        while u != self.d:
            yield u.x
            u = u.next

    def size(self) -> int:  # Returns the size of the list as an integer
        return self.n

    def append(self, x: np.object):  # This will append the element to the list
        self.add(self.n, x)

    def isPalindrome(self) -> bool:  # This will check if the list is a Palindrome
        mid = int(len(self) / 2)  # It will return True if it is, and False if it isn't
        for i in range(mid):
            if self[i] != self[len(self) - i - 1]:
                return False
        return True

    def __str__(self):  # This is the print statement that will print what is in the list
        s = "["
        u = self.d.next
        while u is not self.d:
            s += "%r" % u.x
            u = u.next
            if u.next is not None:  # I couldn't get rid of the last comment that prints at the end of the list
                s += ","
        return s + "]"

    def __next__(self):
        if self.iterator != self.d:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x


dl = DLList()
dl.remove(0)  # print error message or raise exception
dl.add(0, 5)
print(dl)  # print [5]
dl.add(0, 1)
print(dl)  # print [1,5]
dl.add(1, 3)
print(dl)  # print [1,3,5]
dl.add(2, 6)
print(dl)  # print [1,3,6,5]
dl.remove(2)
print(dl)  # print [1,3,5]
dl.add(1, 2)
print(dl)  # print [1,2,3,5]
dl.add(3, 4)
print(dl)  # print [1,2,3,4,5]
dl.append(6)
print(dl)  # print [1,2,3,4,5,6]
dl.set(5, 1)
print(dl)  # print [1,2,3,4,5,1]
dl.remove(3)
print(dl)  # print [1,2,3,5,1]
print(dl.isPalindrome())  # print False
dl.set(1, 5)
print(dl)  # print [1,5,3,5,1]
print(dl.isPalindrome())  # print True
