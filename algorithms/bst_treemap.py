from typing import List

class TreeNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        def dfs(root, key, val):
            if root is None:
                return TreeNode(key, val)
            if key < root.key:
                root.left = dfs(root.left, key, val)
            elif key > root.key:
                root.right = dfs(root.right, key, val)
            else:
                root.val = val  # Update value if key exists
            return root
        self.root = dfs(self.root, key, val)
        return


    def get(self, key: int) -> int:
        if not self.root:
            return -1
        current = self.root
        def dfs(node, key):
            if not node:
                return -1
            if key < node.key:
                return dfs(node.left, key)
            elif key > node.key:
                return dfs(node.right, key)
            else:
                return node.val
        value = dfs(current, key)
        return value


    def getMin(self) -> int:
        if not self.root:
            return -1
        node = self.root
        while node and node.left:
            node = node.left
        return node.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        node = self.root
        while node and node.right:
            node = node.right
        return node.val


    def remove(self, key: int) -> None:
        pass


    def getInorderKeys(self) -> List[int]:
        pass

if __name__ == "__main__":
    tm = TreeMap()
    tm.insert(10, 100)
    print(tm.get(10)) # Output: 100
    tm.insert(5, 50)
    print(tm.get(5))  # Output: 50
    tm.insert(15, 150)
    print(tm.get(10))  # Output: 100
    print(tm.getMin())  # Output: 50
    print(tm.getMax())  # Output: 150
    print(tm.get(20))  # Output: -1 (not found)
