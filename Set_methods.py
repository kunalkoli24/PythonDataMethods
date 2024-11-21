# Sets
# - mutable
# - unordered
# - collection of unique items 
# - Defined using curly braces {}
# - in set we denote empty set as s= set()

# - Methods

# 1. len()
l= {1,2,3,4}
print(len(l))

# 2. add() (Adds a single element to the set. If the element is already in the set, nothing happens.)
a= {1,2,3,4}
a.add(5)
print(a)

# 3. update()  (Adds multiple elements to the set from an iterable)
u = {1,2,3}
u.update([4,5,6])
print(u)

# 4. remove()
r = {1,2,3,4,5}
r.remove(5)
print(r)

# 5. clear()
clr= {1,2,3,4,5}
clr.clear()
print(clr)

# 6. union()  (Returns a new set that contains all unique elements from both sets.)
s1 = [1,2,3]
s2 = [4,5,6]
u = set(s1).union(set(s2))
print(u)

# 7. intersection()  (Returns a new set containing elements common to both sets.)
s3 = [1,2,3,6]
s4 = [3,5,2,6]
i=set(s3).intersection(set(s4))
print(i)

# 8. issubset()  (all elements of one set are contained within another set.)
s5 = [1,2]
s6 = [1,2,3]
subst = set(s5).issubset(set(s6))
print(subst)  # returns true, all elements must be present not only single.

# 9. issuperset()  (method checks if a set contains all elements of another set.)
s7 = [1,2]
s8 = [1,2,3]
supst = set(s7).issuperset(set(s8))
print(supst) 

# 10. isdisjoint()  (checks if  sets have no elements in common.)
set9 = {1, 2, 3}
set10 = {4, 5, 6}
set11 = {3, 4, 5}

print(set9.isdisjoint(set10))  # Output: True, because set9 and set10 have no elements in common

print(set10.isdisjoint(set11))  # Output: False, because set10 and set11 both contain the element 4

print(set9.isdisjoint(set11))  # Output: False, because set9 and set11 both contain the element 3
