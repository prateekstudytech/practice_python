class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
    
class BST:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value: int):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True
        
        current_node = self.root
        while True:
            if value == current_node.value:
                return False
            elif value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
    
    def contains(self, value: int):
        if self.root == None:
            return False
        
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        
        return False
    
    def bfs_traversal(self):
        if self.root == None:
            return []
        queue = []
        result = []
        queue.append(self.root)

        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return result
    
    def dfs_pre_order(self):
        current_node = self.root
        result = []

        def traversal(current_node):
            result.append(current_node.value)
            if current_node.left:
                traversal(current_node.left)
            if current_node.right:
                traversal(current_node.right)
        
        traversal(self.root)
        return result
    
    def dfs_post_order(self):
        current_node = self.root
        result = []

        def traversal(current_node):
            if current_node.left:
                traversal(current_node.left)
            if current_node.right:
                traversal(current_node.right)
            result.append(current_node.value)
        
        traversal(self.root)
        return result

    def dfs_in_order(self):
        current_node = self.root
        result = []

        def traversal(current_node):
            if current_node.left:
                traversal(current_node.left)
            result.append(current_node.value)
            if current_node.right:
                traversal(current_node.right)
        
        traversal(self.root)
        return result
    
    def is_valid_bst(self):
        if self.root == None:
            return False
        results = dfs_in_order(self.root)
        for i in range(1:len(results)):
            if len(results) >= 2:
                if results[i-1] > results[i]:
                    return False
        return True


if __name__ == '__main__':
    my_tree = BST()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.dfs_in_order())
    
    # print("BST is valid:")
    # print(my_tree.is_valid_bst())

