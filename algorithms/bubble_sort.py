# Write program to implement bubble sort algorithm

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted so no need to sort them again
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [3, 4, 6, 2, 1]
    print(bubble_sort(arr))
