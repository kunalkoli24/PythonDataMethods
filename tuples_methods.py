# Tuple 
# - immutable
# - Ordered 
# - can hold elements of different data types.
# - Defined using parentheses ()

# Methods of tuple

# 1. Count ()  ( Count the occurance in tuple)
t = (1, 2, 2, 3)
print(t.count(2))  # Output: 2

# 2. index() returns index of first occurance of item in tuple.
t = (1, 2, 3, 2)
print(t.index(2))  # Output: 1

# 3. max()
t = (1, 5, 3)
print(max(t))  # Output: 5

# 4. min()
t = (1, 5, 3)
print(min(t))  # Output: 1

# 5. sum()
t = (1, 2, 3)
print(sum(t))  # Output: 6

# 6. any()
# Returns True if any element in the tuple is True.
t = (0, 1, 0)
print(any(t))  # Output: True

# 7. all()
# Returns True if all elements in the tuple are True.
t = (1, 2, 3)
print(all(t))  # Output: True

# 8. len()
t = (1, 2, 3)
print(len(t)) # Output: 3

# 9. sorted()
t = (3, 1, 2)
print(sorted(t))  # Output: [1, 2, 3]

# 10. tuple()  #Converts an iterable (like a list or string) into a tuple.
lst = [1, 2, 3]
print(tuple(lst)) # Output: (1, 2, 3)

# 11. nested tuple
t = ((1, 2), (3, 4), (5, 6))

# other useful operations
# - Concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2  # Output: (1, 2, 3, 4)
print(t3)  # or print(t1 + t2)

# - Repetition  (Repeats a tuple a specified number of times.)
t = (1, 2)
t * 3  # Output: (1, 2, 1, 2, 1, 2)
# print(t*3) to display

# - Membership   (Checks if an element exists within a tuple.)
t = (1, 2, 3)
print(2 in t)       # Output: True
print(4 not in t )  # Output: True
print(4 in t )  # Output: false
print(3 not in t )  # Output: false

# Advance tuple technique

# Tuple Packing  (Packing refers to assigning multiple values into a single tuple variable.)

# Packing multiple values into a tuple
packed_tuple = 1, 2, 3, 4
print(packed_tuple)  # Output: (1, 2, 3, 4)

# Alternative syntax with parentheses
packed_tuple = (1, 2, 3, 4)
print(packed_tuple)  # Output: (1, 2, 3, 4)


# Tuple Un-Packing (Unpacking refers to extracting values from a tuple into separate variables.)
tpl=(1,2,3,4)
a,b,c,d =tpl
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)

# Using the * Operator with Unpacking
tpl=(1,2,3,4,5,6)
a,*b,c=tpl
print("a:",a)
print("b:",b)
print("c:",c)