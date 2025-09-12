# Tasks Explanation

## Task 1

Implement a function that finds the sum, average, minimum, and maximum of numbers in an unsorted list.

---

**If asked:**

"What does this function do and what’s its complexity?"

**I say:**

- It computes the **sum, average, minimum, and maximum** of all numbers in the list.

- It uses a **single loop** over the list → each element is processed once.

- Therefore, the time complexity is **O(n)**.

## Task 2

Implement a function that finds the frequency of all numbers in a sorted list.

---

**If asked:**

“What does this function do and what’s its complexity?”

**I say:**

- The function counts how many times each number appears in a sorted list.

- It prints frequencies as soon as it finds a new number.

- It uses a **single loop** that processes each element once.

- So the time complexity is **O(n)**.

## Task 3

Implement a recursive function that returns the sum of all digits in a positive integer.

---

- The function uses recursion to sum digits.

- **Base case:** when only one digit is left → return that digit.

- **Recursive case:** split number into left and right halves, sum recursively.

- **Complexity:** Each digit is visited once, so time complexity is O(d) where d = number of digits.

## Task 4

Implement a recursive function that returns all unique vowels in a string.

---

This function recursively extracts all unique vowels from a string.

- **Base case:** when string length = 1, check if it’s a vowel.

- **Recursive case:** split string into halves, process both recursively.

- **Complexity:** O(n log n) due to slicing overhead, or O(n) if indexes are used.