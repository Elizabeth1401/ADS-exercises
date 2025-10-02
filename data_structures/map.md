# Map 

- A **map** (in Python called a **dictionary** *dict*) is a collection of **key-value pairs**
- **Keys** must be unique and **hashable** (numbers, strings, tuples, etc.)
- **Values** can be of any type and are not required to be unique
- Internally, *dict* uses **hashing for fast access


**Properties:**

- Keys are unique -> if you insert the same key again, the value gets **updated**
- Iterating over a dictionary goes through keys by default

## Operations & Complexity:

| Operation              | Description                                | Average Time |
| ---------------------- | ------------------------------------------ | ------------ |
| `d[k] = v`             | Insert or update a key-value pair          | O(1)         |
| `d[k]`                 | Access value by key                        | O(1)         |
| `d.get(k, default)`    | Safe access (returns `default` if missing) | O(1)         |
| `del d[k]`             | Delete a key-value pair                    | O(1)         |
| `k in d`               | Membership test for key                    | O(1)         |
| `len(d)`               | Number of key-value pairs                  | O(1)         |
| Iteration (`.items()`) | Iterate over all key-value pairs           | O(n)         |
