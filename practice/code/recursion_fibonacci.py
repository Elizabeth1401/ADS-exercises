def fib(n):
    """
    Fibonacci using recursion
    Base case: fib(0) = 0, fib(1) = 1
    Recursive case: fib(n) = fib(n-1) + fib(n-2)
    Time Complexity: O(2^n) - very slow!
    """
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print(fib(6))  # Output: 8