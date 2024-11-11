# List 
# - Mutable 
# - Ordered 
# - contain items of any data type
# -  Defined using square brackets [], with elements separated by commas.





# 1. append()   (to add at the end)
a = [2,5,"kuanl",50.89]
a.append(77)
print(a)

# 2. insert() (insert item in the list using index value)
a = [2,5,"kuanl",50.89]
a.insert(1, "rahul")
print(a)

# 3. pop() remove item using index
a = [2,5,"kuanl",50.89]
a.pop(1)
print(a)

# 4. remove()  (directly remove value )
a = [2,5,"kunal",50.89]
a.remove("kunal")
print(a)

# 5. sort() sort the list 
s = [2,90,54,22,67]
s.sort()
print(s)

# 6. reverse()  reverse the list 
r = [2,90,54,22,67]
r.reverse()
print(r)

# 7. len() gives you the length 
r = [2,90,54,22,67]
print(len(r))

# 8. sum() 
s = [1, 2, 3]
print(sum(s))  

# 9. min() max()
m = [1, 2, 3]
print(min(m))  # Output: 1
print(max(m))  # Output: 3

# 10. join()  (Combines list elements into a single string with a specified separator.)
j = ["a", "b", "c"]
print('-'.join(j))   # o/p: a-b-c

# 11. copy() 
l = [2,7,4,6]
newl = l.copy()
print(newl)

# 12. count()   (count occurances of the item in list)
c = [2,5,2,4,2,8]
print(c.count(2))

# 13. clear()  (removes all items from the list)
c = [2,5,2,4,2,8]
c.clear()
print(c)