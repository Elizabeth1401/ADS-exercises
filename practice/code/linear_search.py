def linear_search(arr, target):
    """
    Linear search algorithm
    Time Complexity: O(n)
    """
    for i in range(len(arr)):    # Loop over all elements
        if arr[i] == target:     # Check if element matches
            return i             # Return index if found
    return -1                    # Return -1 if not found

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print(linear_search(arr, 30))  # Output: 2
    print(linear_search(arr, 100)) # Output: -1