from typing import List

class Node:

    def __init__(self, val: int) -> None:
        self.val = val
        self.next_node = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        if self.head == None:
            return -1
        i = 0
        curr_node = self.head
        while i < index and curr_node:
            curr_node = curr_node.next_node
            i += 1
        return curr_node if i == index and curr_node else -1


    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next_node = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.insertHead(val)
            return
        new_node = Node(val)
        prev_node = None
        curr_node = self.head
        while curr_node:
            prev_node = curr_node
            curr_node = curr_node.next_node
        prev_node.next_node = new_node
        return

    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        i = 0
        prev_node = None
        curr_node = self.head
        while i < index and curr_node:
            prev_node = curr_node
            curr_node = curr_node.next_node
            i += 1
        if i == index and curr_node:
            prev_node.next_node = curr_node.next_node
            curr_node.next_node = None
            return True
        return False
        

    def getValues(self) -> List[int]:
        result = []
        curr_node = self.head
        while curr_node:
            result.append(curr_node.val)
            curr_node = curr_node.next_node
        return result

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertHead(1)
    ll.insertTail(2)
    ll.insertTail(3)
    print(ll.getValues())  # Output: [1, 2, 3]
    ll.remove(1)
    print(ll.getValues())  # Output: [1, 3]
    print(ll.get(0))       # Output: Node with value 1
    print(ll.get(1))       # Output: Node with value 3
    print(ll.get(2))       # Output: -1
