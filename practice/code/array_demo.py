# Array demo using Python's list as dynamic array
arr = [10, 20, 30, 40]

print("Access index 2:", arr[2]) # O(1)
arr[1] = 25 # update O(1)
print("Updated array:", arr)

#Insert in middle (O(n))
arr.insert(2, 99)
print("After insert:", arr)

#Delete from middle (O(n))
arr.pop(2)
print("After pop:", arr)