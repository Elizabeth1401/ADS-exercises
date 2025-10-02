# creating sets
fruits = {"apple", "banana", "cherry", "apple"} # dublicates removed
print(fruits) #{'apple', 'banana', 'cherry'}

numbers = set([1, 2, 3, 2, 1])
print(numbers) # {1, 2, 3}

# add and remove
fruits.add("orange")
print(fruits) # {'apple', 'banana', 'cherry', 'orange'}

fruits.discard("banana") # safe remove
print(fruits) #{'apple', 'cherry', 'orange'}

# membership test
print("apple" in fruits) #True
print("banana" in fruits) #False

#set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) #union -> {1, 2, 3, 4, 5}
print(a & b) #intersection -> {3}
print(a - b) #difference -> {1, 2}
print(a ^ b) #symmetric difference -> {1, 2, 4, 5}