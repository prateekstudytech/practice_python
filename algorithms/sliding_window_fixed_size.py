def closeDuplicates(nums: list[int], k: int) -> bool:
    """
    Checks if the array contains any duplicates within a window of size k. 
    Returns False if k is less than or equal to 0.

    Args:
        nums (list[int]): The list of integers to check.
        k (int): The maximum index distance between duplicate values.

    Returns:
        bool: True if there are any duplicates within k indices of each other, False otherwise.

    Example:
        closeDuplicates([1, 2, 3, 1], 3) -> False
        closeDuplicates([1, 2, 3, 4], 2) -> False
        closeDuplicates([1, 0, 1, 1], 2) -> True
    """
    left = 0  # Left pointer of the sliding window
    window = set()  # Set to store unique elements in the current window

    for right in range(len(nums)):
        # If window size exceeds k, remove the leftmost element
        if right - left >= k:
            window.discard(nums[left])
            left += 1
        # If current element is already in the window, duplicate found
        if nums[right] in window:
            return True
        # Add current element to the window
        print(f"Adding {nums[right]} to the window")
        window.add(nums[right])
        print(f"Current window: {window}")
    
    # No duplicates found within k distance
    return False

# Example usage:
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    k = 3
    print(closeDuplicates(nums, k))  # Output: False

    # nums = [1, 0, 1, 1]
    # k = 2
    # print(closeDuplicates(nums, k))  # Output: True

    # nums = [1, 2, 3, 4]
    # k = 2
    # print(closeDuplicates(nums, k))  # Output: False
