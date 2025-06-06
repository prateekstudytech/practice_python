import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_append(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        values = self._get_values()
        self.assertEqual(values, [1, 2, 3])

    def test_prepend(self):
        self.ll.append(2)
        self.ll.prepend(1)
        values = self._get_values()
        self.assertEqual(values, [1, 2])

    def test_insert(self):
        self.ll.append(1)
        self.ll.append(3)
        self.ll.insert(1, 2)
        values = self._get_values()
        self.assertEqual(values, [1, 2, 3])

    def test_pop(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        pop_node = self.ll.pop()
        self.assertEqual(pop_node.value, 3)
        values = self._get_values()
        self.assertEqual(values, [1, 2])

    def test_find_length(self):
        self.assertEqual(self.ll.find_length(), 0)
        self.ll.append(1)
        self.assertEqual(self.ll.find_length(), 1)
        self.ll.append(2)
        self.assertEqual(self.ll.find_length(), 2)

    def test_insert_out_of_bounds(self):
        self.ll.append(1)
        with self.assertRaises(IndexError):
            self.ll.insert(5, 10)

    def _get_values(self):
        values = []
        temp = self.ll.head
        while temp:
            values.append(temp.value)
            temp = temp.next
        return values

if __name__ == "__main__":
    unittest.main()
