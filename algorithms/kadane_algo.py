# Kadane's Algorithm to find the maximum subarray sum
def kadane_algorithm(nums):
    """
    Implements Kadane's Algorithm to find the maximum subarray sum.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The maximum subarray sum.
    """
    if not nums:
        return 0

    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

# Return the left and right index of the max subarray sum,
# assuming there's exactly one result (no ties).
# Sliding window variation of Kadane's: O(n)
def kadane_with_indices(nums):
    """
    Implements a variation of Kadane's Algorithm to find the maximum subarray sum
    along with its starting and ending indices.

    Args:
        nums (list): A list of integers.

    Returns:
        tuple: A tuple containing the maximum subarray sum and its starting and ending indices.
    """
    if not nums:
        return 0, -1, -1

    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R 

    return [maxL, maxR]

# Example usage:
if __name__ == "__main__":
    example_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = kadane_algorithm(example_array)
    print(f"The maximum subarray sum is: {result}")
    start_index, end_index = kadane_with_indices(example_array)
    print(f"The maximum subarray sum is: {result}, starting at index {start_index} and ending at index {end_index}")
