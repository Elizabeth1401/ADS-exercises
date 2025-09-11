def sum_array(arr, n):
    """
    Sum array using recursion
    Base case: empty array (n=0) → 0
    Recursive case: sum(n) = arr[n-1] + sum(n-1)
    Time Complexity: O(n)
    """
    if n == 0:
        return 0
    return arr[n-1] + sum_array(arr, n-1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(sum_array(arr, len(arr)))  # Output: 10
