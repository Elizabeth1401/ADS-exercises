# 🔍 Searching Algorithms

Searching = finding a target value inside a collection (array, list, tree, graph, etc.).

---

## 1. Linear Search (O(n))
- **Idea:** check each element one by one until found.
- **Best case:** O(1) (first element is the target).
- **Worst case:** O(n) (last element or not found).
- **Use case:** unsorted data.

## 2. Binary Search (O(log n))
- **Idea:** repeatedly halve the search space
- **Requirement:** array must be **sorted**.
- **Best case:** O(1) (middle element is target).
- **Worst case:** O(log n).

### Python Example
```python
#Linear Search
def linear_search(arr, target):
    # Loop through each element
    for i in range(len(arr)):
        if arr[i] == target:  # Check if match
            return i          # Return index if found
    return -1                 # -1 if not found

print(linear_search([3, 5, 7, 9], 7))  # Output: 2

# (Iterative)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2   # Find middle index
        if arr[mid] == target:      # Target found
            return mid
        elif arr[mid] < target:     # Target is in right half
            left = mid + 1
        else:                       # Target is in left half
            right = mid - 1
    
    return -1  # Not found

print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3

#Binary Search (Recursive)
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1   # Base case: not found
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

print(binary_search_recursive([1, 3, 5, 7, 9], 9, 0, 4))  # Output: 4




