# Big-O Exercises

#1 Single loop  What's the time complexity?
def sum_to_n(n):
    # Loop runs exactly n times -> linear work
    s = 0
    for i in range(n): # O(n) iterations
        s += i         # O(1) per iteration
    return s           # Total: O(n)

#2 Two nested loops
def count_pairs(n):
    # Two full nested loops: n * n iterations 
    c = 0
    for i in range(n):      # n
        for j in range(n):  # n for each i
            c += 1          # O(1)
    return c                # Total: O(n * n) = O(n^2)

#3 Inner loop depends on i
def triangular(n):
    # Inner loop runs i+1 times; total = 1+2+...+n = n(n+1)/2
    c = 0
    for i in range(n):           # n rows
        for j in range(i + 1):   # grows with i arerage n/2
            c += 1
    return c                     # Total: Θ(n^2)

#4 Halving loop
def halve_until_zero(n):
    # Each iteration halves n -> number of iterations = floor(log2 n) + 1
    steps = 0
    while n > 0:    # runs -> log2(n) times
        n //= 2.    # halve n
        steps += 1
    return steps    # Total: Θ(log n)

#5 Doubling loop
def powers_below(n):
    # k grows as 1,2,4,8,... up to < n -> log2(n) iterations
    k = 1
    cnt = 0
    while k < n:   # log2(n) iterations
        k *= 2     # double k
        cnt += 1
    return cnt     # Total: Θ(log n)

#6 Two independent inputs Let n = len(a), m = len(b)
def cross_check(a, b):
    # Outer scans a (n items); for each, inner scans b (m items)
    # Total comparisons = n * m
    hits = 0
    for x in a:           # n iterations
        for y in b:       # m iterations each
            if x == y:    # O(1) check
                hits += 1
    return hits           # Total: Θ(n * m)

#7 Nested + halving inner
def n_times_log_m(n, m):
    # For each of the n iterations, inner while halves x until 0
    # Inner work per outer loop = log2(m) 
    total = 0
    for _ in range(n):  # n times
        x = m
        while x > 0:    # log2(m) iterations
            x //= 2
            total += 1
    return total        # Total: Θ(n * log m)

#8 Early break trims a nested loop
def upper_triangle(n):
    # We only count j >= i (upper triangle including diagonal)
    # Number of ops = n + (n-1) + ... + 1 = n(n+1)/2 → Θ(n^2)
    ops = 0
    for i in range(n):
        for j in range(n):
            if j < i:            # break out of inner early
                continue
            ops += 1
    return ops

#9 Hash set membership
def count_unique(arr):
    # Each add is average O(1) due to hashing
    # Total ≈ O(n); worst-case pathological hashing is O(n^2), but uncommon
    seen = set()
    for x in arr:     # n items
        seen.add(x)   # average O(1)
    return len(seen)  # Total: Θ(n) average

#10 Divide & Conquer (Merge Sort) What's T(n) and Big-O?
def merge_sort(a):
    # Recurrence: split into 2 subproblems of size n/2 (2T(n/2))
    # plus linear-time merge (O(n)).
    # By Master Theorem (a=2, b=2, f(n)=n ⇒ n^log_b(a) = n):
    # T(n) = Θ(n log n)
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def merge(L, R):
    i = j = 0
    out = []
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            out.append(L[i]); i += 1
        else:
            out.append(R[j]); j += 1
    out.extend(L[i:]); out.extend(R[j:])
    return out
