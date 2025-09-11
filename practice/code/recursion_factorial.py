def factorial(n):
    """
    Factorial using recursion
    Base case: factorial(0) = 1
    Recursive case: factorial(n) = n * factorial(n-1)
    Time Complexity: O(n)
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(5))  # Output: 120