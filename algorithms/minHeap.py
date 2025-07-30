from typing import List

class MinHeap:
    
    def __init__(self):
        self.heap = [0]
    
    def _bubble_up(self, index):
        while index//2 > 0 and self.heap[index] < self.heap[index//2]:
            self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
            index = index//2
        return
    
    def _bubble_down(self, index):
        while index*2 < len(self.heap):
            if ((index*2+1 < len(self.heap)) and 
                self.heap[index*2 + 1] < self.heap[index]):
                self.heap[index], self.heap[index*2 + 1] = self.heap[index*2 + 1], self.heap[index]
                index = index*2 + 1
            elif self.heap[index*2] < self.heap[index]:
                self.heap[index], self.heap[index*2] = self.heap[index*2], self.heap[index]
                index = index*2
            else:
                break


    def push(self, val: int) -> None:
        self.heap.append(val)
        if len(self.heap) <= 1:
            return
        self._bubble_up(len(self.heap) - 1)
        return


    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        val = self.heap[1]
        self.heap[1] = self.heap[-1]
        self._bubble_down(1)
        self.heap.pop()
        return val


    def top(self) -> int:
        if len(self.heap) <= 1:
            return -1
        return self.heap[1]


    def heapify(self, nums: List[int]) -> None:
        self.heap = [0]
        for num in nums:
            self.push(num)
        return
        