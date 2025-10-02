# SET

- A **set** is an **unordered collection of unique elements**
- Dublicates are **automatically removed**
- Sets are implemented using **hash tables**, so most operations very efficient (O(1) average time)
- **Important properties:**
- - No dublicate elements
- - Elements must be **hashable** (e.g., numbers, strings, tuples - but not lists or dicts)
- - The order of elements is **not guaranteed**

----------------------

## Operations & Complexity:

| Operation                    | Description                                 | Average Time           |      |
| ---------------------------- | ------------------------------------------- | ---------------------- | ---- |
| `add(x)`                     | Add element `x`                             | O(1)                   |      |
| `remove(x)` / `discard(x)`   | Remove element (error if not found vs safe) | O(1)                   |      |
| `in`                         | Check membership                            | O(1)                   |      |
| `len(s)`                     | Get number of elements                      | O(1)                   |      |
| `union` (`                   | `)                                          | Elements in either set | O(n) |
| `intersection` (`&`)         | Elements in both sets                       | O(min(n,m))            |      |
| `difference` (`-`)           | Elements in one but not the other           | O(n)                   |      |
| `symmetric_difference` (`^`) | Elements in one set OR the other, not both  | O(n)                   |      |
