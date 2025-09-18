#Python's built-in list (dynamic array)

lst = []
lst.append(10)
lst.append(20)
lst.append(30)

print(lst) #[10,20,30]
print(lst[1]) # 20 (O(1) access)

lst.insert(1, 99) #O(n) insert
print(lst)

lst.remove(99) #O(n) remove
print(lst)