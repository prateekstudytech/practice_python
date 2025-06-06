"""
linked_list.py

A simple implementation of a singly linked list in Python.

Classes:
    Node: Represents a node in the linked list.
    LinkedList: Implements methods to manipulate the linked list.

Usage:
    - Append, prepend, insert, and pop elements from the list.
    - Traverse the list and find its length.

Example:
    ll = LinkedList()
    ll.append(10)
    ll.prepend(5)
    ll.insert(1, 7)
    ll.pop()
    ll.traverse_list()
    print(ll.find_length())
"""

class Node:
    """
    Represents a node in a singly linked list.

    Attributes:
        value: The data stored in the node.
        next (Node or None): Reference to the next node in the list, or None if this is the last node.

    Args:
        value: The value to be stored in the node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    A singly linked list implementation supporting basic operations such as append, prepend, insert, pop, and traversal.
    Attributes:
        head (Node): The first node in the linked list.
        tail (Node): The last node in the linked list.
    Methods:
        __init__():
            Initializes an empty linked list with head and tail set to None.
        append(value):
            Adds a new node with the specified value to the end of the list.
        prepend(value):
            Adds a new node with the specified value to the beginning of the list.
        insert(index, value):
            Inserts a new node with the specified value at the given index in the list.
            Raises IndexError if the index is out of bounds.
        find_length():
            Returns the number of nodes in the linked list.
        pop():
            Removes and returns the last node from the list. Returns None if the list is empty.
        traverse_list():
            Prints the values of all nodes in the list in order.
    """
    def __init__(self):
        """
        Initializes a new empty linked list with head and tail set to None.
        """
        self.head = None
        self.tail = None
    
    def append(self, value):
        """
        Appends a new node with the given value to the end of the linked list.

        Args:
            value: The value to be stored in the new node.

        Side Effects:
            Modifies the linked list by adding a new node at the end.
            Updates the tail reference to the new node.
        """
        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
    
    def prepend(self, value):
        """
        Inserts a new node with the specified value at the beginning of the linked list.

        If the list is empty, both head and tail will point to the new node.
        Otherwise, the new node becomes the new head, and its next pointer references the previous head.

        Args:
            value: The value to store in the new node.
        """
        node = Node(value)
        if self.head == None:
            self.tail = node
        else:
            node.next = self.head
        self.head = node
    
    def insert(self, index, value):
        """
        Inserts a new node with the specified value at the given index in the linked list.

        Parameters:
            index (int): The position at which to insert the new node. Indexing starts at 0.
            value (Any): The value to be stored in the new node.

        Raises:
            IndexError: If the index is greater than the length of the linked list plus one.

        Notes:
            - If index is 0, the value is prepended to the list.
            - If index is equal to the length of the list plus one, the value is appended to the end.
            - Otherwise, the value is inserted at the specified position.
        """
        length = self.find_length()
        if index > length+1:
            raise IndexError
        elif index == 0:
            self.prepend(value)
        elif index == length+1:
            self.append(value)
        i = 0
        temp = self.head
        node = Node(value)
        while i != index - 1:
            temp = temp.next
            i += 1
        node.next = temp.next
        temp.next = node

    def find_length(self):
        """
        Calculates and returns the number of nodes in the linked list.

        Returns:
            int: The total number of nodes in the linked list. Returns 0 if the list is empty.
        """
        if self.head == None:
            return 0
        elif self.head == self.tail:
            return 1
        temp = self.head
        i = 1
        while temp.next != None:
            temp = temp.next
            i += 1
        return i

    def pop(self):
        """
        Removes and returns the last node from the linked list.

        If the list is empty, returns None. If the list contains only one node,
        removes it and sets both head and tail to None. Otherwise, traverses the list
        to find the node before the tail, updates the tail, and removes the last node.

        Returns:
            Node or None: The removed node if the list is not empty, otherwise None.
        """
        if self.head == None:
            return None
        pop_node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next    
        self.tail = temp
        temp.next = None
        print(f"Pop node {pop_node.value}")
        return pop_node

    def traverse_list(self):
        """
        Traverses the linked list from the head node to the end, printing the value of each node.

        If the list is empty (i.e., head is None), the method returns None and does not print anything.
        Otherwise, it prints the values of all nodes in the list, separated by spaces, followed by a newline.
        """
        if self.head == None:
            return None
        temp = self.head
        while temp != None:
            print(temp.value, end = " ")
            temp = temp.next
        print("")

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(40)
    ll.append(50)
    ll.traverse_list()
    ll.pop()
    ll.traverse_list()
    ll.insert(2, 100)
    ll.traverse_list()
    print(ll.find_length())
