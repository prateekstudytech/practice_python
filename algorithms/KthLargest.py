# Find Kth largest element in a stream of integers using a min-heap
import heapq
from typing import List

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(nums)
    
    def add(self, val: int) -> int:
        heapq.heapify(self.nums.append(val))
        for i in range(len(self.nums) - self.k):
            self.nums.pop()
        return self.nums[0]
