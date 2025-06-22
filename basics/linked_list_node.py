class SingleLLNode:
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
