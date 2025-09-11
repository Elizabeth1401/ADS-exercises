# O(1): Constant time
def get_first(arr):
    # Accessing an array element by index is constant time
    # Doesn't matter if arr has 10 or 10 million elements
    return arr[0]


# O(n): Linear time
def linear_search(arr, target):
    # Check each element one by one
    for i in range(len(arr)):  # Loop runs n times
        if arr[i] == target:   # Compare each element
            return i           # Return index if found
    return -1                  # Return -1 if not found


#O(log n): Logarithmic
def binary_search(arr, target):
    # Binary Search only works on a sorted array
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Pick middle element
        if arr[mid] == target:
            return mid              # Found target
        elif arr[mid] < target:
            left = mid + 1          # Search right half
        else:
            right = mid - 1         # Search left half
    return -1                       # Not found


#O(n log n): Merge Sort
def merge_sort(arr):
    # Base case: if array has 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Sort left half
    right = merge_sort(arr[mid:])  # Sort right half
    
    # Merge sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from both halves and pick smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left or right
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


#O(2^n): Recursive Fibonacci
def fib(n):
    # Base case: first two Fibonacci numbers
    if n <= 1:
        return n
    
    # Recursive calls: each call splits into 2 new calls
    # This makes the complexity O(2^n)
    return fib(n-1) + fib(n-2)

#O(n^2): Quadratic Time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):             # Outer loop runs n times
        for j in range(n - i - 1): # Inner loop runs ~n times
            if arr[j] > arr[j+1]:  # Compare adjacent elements
                # Swap if elements are out of order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#O(n!): Factorial Time
import itertools

def generate_permutations(arr):
    # itertools.permutations generates all possible orderings
    # For n elements → n! permutations
    return list(itertools.permutations(arr))

# Example
print(generate_permutations([1, 2, 3]))
# Output: [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]

