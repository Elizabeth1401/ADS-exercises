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

## Task 5
Implement a function thet uses binary search on a sorted list of ints,
to find out how many times an int occurs in the list:
count_occurrences([1,2,2,3,4],2) Returns 3
count_occurrences([1,3,5,7],4) Returns 0

---

- We do two specialized binary searches:

- - Left bound: keep searching left while we can still see x at mid.

- - Right bound: keep searching right while we can still see x at mid.

- Base case: interval becomes empty (low > high) → return -1.

- Time complexity: each search is O(log n); two searches → O(log n) overall.

- Why sorted is required: binary search only works when the search space is ordered.