# Arrays

- Fixed-size contiguous memory block.
- Random access by index → O(1).
- Insert/delete at arbitrary index → O(n) (shift needed).
- Great for fast lookups, bad for frequent resizing.

| Operation         | Time Complexity |
|-------------------|-----------------|
| Access (a[i])     | O(1)            |
| Update (a[i]=x)   | O(1)            |
| Insert/Delete end | O(1) amortized  |
| Insert/Delete mid | O(n)            |
