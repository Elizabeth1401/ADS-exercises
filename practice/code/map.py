# create dictionary (map)
student = {"name": "Alice", "age": 21}
print(student) #{'name': 'Alice', 'age': 21}

# add/ update
student["grade"] = "A" #add new key
student["age"] = 22 #update existing key
print(student) # {'name': 'Alice', 'age': 22, 'grade': 'A;}

# access
print(student["name"]) #Alice
print(student.get("major", "Not found")) #safe lookup

#remove
del student ["grade"]
print(student) #{'name': 'Alice', 'age': 22}

# membership
print("name" in student) #True
print("grade" in student) #False

#iterate
for key, value in student.items():
    print(key, ":", value)
#Output
#name: Alice
#age: 22

#practical example: word frequency
text = "apple banana apple orange banana apple"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) +1
print(freq) #{'apple': 3, 'banana': 2, 'orange': 1}