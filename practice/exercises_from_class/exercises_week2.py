"""
Easy Exercise1:
Implement a function that finds the sum,average, min and max 
for the numbers in an unsorted list
Expand it by finding the frequency of all the numbers
"""

def sumAverageMinMax (myList):
    mySum = 0 # accumulator for sum
    min_val = myList[0] # assume first element is min
    max_val = myList[0] # assume first element is max

    for x in myList: # loop throught all elements
     mySum = mySum + x # adds each element to the running sum

     if x < min_val: # update min if smaller found
     min_val = x

     if x > max_val: # update max if larger found 
     max_val = x

 average = mySum / len(myList) # compute average
 return mySum, min_val, max_val, average

"""
Time Complexity Analysis
- Loop visits every element once -> O(n)
- Updates inside the loop are constant time -> O(1)
- Overall: O(n) + O(1) = O(n)
"""

"""
-------------------------------
Exercise 2:
Implement a function that finds the frequency 
of all numbers in a sorted list
"""

def frequencyPrint( myList):
    index = 0
    number = myList[0] # current number we are counting
    freq = 0  # frequency counter

    while index < len(myList): # loop until we reach the end of the list
        if myList[index] == number:
            # Same number -> increase count
            freq = freq + 1
        else:
            # New number starts -> print previous frequency
            print("Found {} of {}".format( freq, myList[index-1]))
            freq = 1
            number = myList[index]
        index = index + 1
    # Print frequency of the last number
    print("Found {} of {}".format(freq, myList[index-1])) 

"""
Time Complexity Analysis
- The function loop once through the list
- Each element is compared only once
- Therefore, time complexity = O(n)
"""

"""
--------------------------
Exercise 3:
Implement a recursive function that returns 
the sum of all digits in a positive integer.
"""

def sum_digits(content):
    content_str = str(content) # Convert number to string
    content_len = len(content_str) #Count digits

    #Base case: only 1 digit
    if content_len == 1:
        return constant
    
    else:
        # Recursive case: split into two halves
        middle = constant_len // 2
        left = content_str[0:middle] # first half of digits
        right = content_str[middle:constant_len] # second half of degits

        # Recursive calls on both halves
        return (sum_digits(int(left))) + sum_digits(int(right))
print(sum_digits(222)) # Output: 6

"""
Time Complexity
- Let d = number of digits
- Each recursive call splits the number into halves
- The total number of recursive calls is proportional to d
- Time Complexity = O(d).
"""

"""
-------------------------
Exercise 4:
Implement a recursive function that 
returns all unique vowels in a string.
"""
def is_vowel(letter): # helper function, checks if a character is vowel
    vowels = {"a","e","i","o","u"}
    return letter in vowels

def recursive_vowels(content, vowels = None):
    if vowels is None:
        vowels = set() # use a set so each vowel is stored once only(unique)
    constant_len = len(constant)

    # Base case: single character
    # If the string has only one character, check if it's a vowel and return it
    if content_len == 1:
        content_lower = constant.lower()
        if is_vowel(content_lower): # if character is a vowel
            vowels.add(content_lower) # add to set
        return vowels
    
    else:
        # Recursive case: split into two halves
        middle = constant_len // 2
        recursive_vowels(constant[0:middle], vowels) # left half
        recursive_vowels(constant[middle:constant_len], vowels) # right half
        return vowels
print(recursive_vowels("coffee store")) #Output: {'o','e'}

"""
Time complexity 
- Each recursive call slices the string
- Slicing costs O(n)
- The recursion tree has O(log n) levels
- Total complexity: O(n log n)
"""

"""
------------------------
Exercise 5:
Implement a function thet uses binary search on a sorted list of ints,
to find out how many times an int occurs in the list:
count_occurrences([1,2,2,3,4],2) Returns 3
count_occurrences([1,3,5,7],4) Returns 0
"""
def binary_search_bound(a, x, low = 0, high = None, want = "left"):
    """
    Return the index of the leftmost/rigtmost occurrence of x in sorted list a.
    If x is not present, return -1.

    want = "left" -> first(lowest) index where a[i] == x
    want = "right" -> last(highest) index where a[i] == x
    """

    if high is None:
        high = len(a) - 1
    
    if low > high: # Base case: empty interval
        return -1 
    
    mid = (low + high) // 2

    if a[mid] == x:
        # I found x, but I might not be at the boundary yet.
        if want == "left":
            #Try to push boundary to the left
            left_idx = binary_search_bound(a, x, low, mid - 1, "left")
            return left_idx if left_idx != -1 else mid
        else: # want == "right"
        #Try to push boundary to the right
        right_idx = binary_search_bound(a, x, mid +1, high, "right")
        return right_idx if right_idx!= -1 else mid 
    elif a[mid] < x:
        return binary_search_bound(a, x, mid +1, high, want)
    else:
        return binary_search_bound(a, x, low, mid -1, want)

def count_occurrences(a, x):
    """
    Count how many times x appears in sorted list a
    """
    left = binary_search_bound(a, x, want = "left")
    if left == -1: #Not found at all
       return 0
    right = binary_search_bound(a, x, want= "right")
    return right - left + 1
