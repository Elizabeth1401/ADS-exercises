# 🔁 Recursion

Recursion = when a function **calls itself** until it reaches a **base case**.

---

## 📌 Key Concepts

1. **Base Case** – the condition where recursion stops.  
2. **Recursive Case** – the part where the function calls itself.  
3. **Stack** – each recursive call is put on the call stack until base case is reached.

---
| Problem        | Recurrence Relation       | Complexity |
| -------------- | ------------------------- | ---------- |
| Factorial      | T(n) = T(n-1) + O(1)      | O(n)       |
| Fibonacci      | T(n) = T(n-1)+T(n-2)+O(1) | O(2^n)     |
| Sum of Array   | T(n) = T(n-1) + O(1)      | O(n)       |
| Tower of Hanoi | T(n) = 2T(n-1) + O(1)     | O(2^n)     |
