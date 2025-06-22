from linked_list_node import SingleLLNode as Node

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

class LinkedList:
    """
    Singly linked list supporting append, prepend, insert, pop, and traversal.

    Attributes:
        head (Node): First node in the list.
        tail (Node): Last node in the list.
        length (int): Number of nodes in the list.

    Methods:
        append(value): Add value to end of list.
        prepend(value): Add value to start of list.
        insert(index, value): Insert value at given index.
        find_length(): Return number of nodes.
        pop(): Remove and return last node.
        traverse_list(): Print all node values.
    """
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        """
        Add a new node with the given value to the end of the list.

        Args:
            value: Value to store in the new node.

        Returns:
            bool: True if operation is successful.
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1
        return True

    def prepend(self, value):
        """
        Add a new node with the given value to the start of the list.

        Args:
            value: Value to store in the new node.

        Returns:
            bool: True if operation is successful.
        """
        node = Node(value)
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
        self.head = node
        self.length += 1
        return True

    def insert(self, index, value):
        """
        Insert a new node with the given value at the specified index.

        Args:
            index (int): Position to insert at (0-based).
            value: Value to store in the new node.

        Raises:
            IndexError: If index is out of bounds.

        Returns:
            bool: True if operation is successful.
        """
        length = self.find_length()
        if index > length + 1:
            raise IndexError("Index out of bounds")
        elif index == 0:
            return self.prepend(value)
        elif index == length + 1:
            return self.append(value)
        i = 0
        temp = self.head
        node = Node(value)
        while i != index - 1:
            temp = temp.next
            i += 1
        node.next = temp.next
        temp.next = node
        self.length += 1
        return True

    def find_length(self):
        """
        Return the number of nodes in the list.

        Returns:
            int: Number of nodes.
        """
        return self.length

    def pop(self):
        """
        Remove and return the last node from the list.

        Returns:
            Node or None: The removed node, or None if list is empty.
        """
        if self.head is None:
            return None
        pop_node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        print(f"Pop node {pop_node.value}")
        self.length -= 1
        return pop_node

    def traverse_list(self):
        """
        Print all node values in the list, separated by spaces.
        """
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
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
