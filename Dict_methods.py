# Dictionary
# - mutable
# - collection of key-value pairs
# - unordered but can be ordered in Python 3.7+ (insertion order is maintained).
# - Defined using curly braces {}
# - e.g {'name': 'Alice', 'age': 25}).
# - "Keys must be unique" but value can be repeated
# - {} denotes empty dict 

# - Methods

# 1. items() (Returns a view object with a list of dictionary’s key-value tuple pairs.)
d= {
    "Kunal": 95,
    "Param": 93,
    "Pushkar": 94,
    "Surve": 92
}
print(d.items())

# 2. keys() (return all keys from dict)
k= {
    "Kunal": 95,
    "Param": 93,
    "Pushkar": 94,
    "Surve": 92
}
print(k.keys())

# 3. values() (return all values from dict)
v= {
    "Kunal": 95,
    "Param": 93,
    "Pushkar": 94,
    "Surve": 92
}
print(v.values())

# 4. update() 
# Update the dict and also add another pair if not exist in the dict 
u= {
    "Kunal": 95,
    "Param": 93,
    "Pushkar":94
}
u.update({"Pushkar":90}) # update the marksa of pushkar .
u.update({"Pushkar":90, "Surve":89}) # update marksa of pushkar as-well-as insert the pair of surve in to the dict
print(u)

# 5. get() (Retrieves the value for a specified key)
g= {
    "Kunal": 95,
    "Param": 93,
    "Pushkar":94
}
print(g.get("Kunal"))

# BUT if:-

# print(g.get("Kunal2"))    o/p: None
# If you use this syntax (.get() ), this will give you none, if key is not present in the dict 

# print(g["Kunal2"])    o/p: KeyError: 'Kunal2'
# If you  use this syntax,this will give you error if key is not present in the dict 

# 6. pop()  (will remove/delete specific item)
p= {
    "Kunal": 95,
    "Param": 93,
    "Pushkar":94
}
p.pop("Pushkar")
print(p)

# 7. popitem()   (will remove last inserted pair as a tuple)
pi= {
    "Kunal": 95,
    "Param": 93,
    "Pushkar": 94,
    "Surve": 92       # will get removed
}
pi.popitem()
print(pi)

# 8. clear()  (clear all elements form the dict)
clr= {
    "Kunal": 95,
    "Param": 93,
    "Pushkar": 94,
    "Surve": 92       # will get removed
}
clr.clear()
print(clr)

# 9. copy() (returns a shallow of dict)
cpy= {
    "Kunal": 95,
    "Param": 93,
    "Pushkar":94
}
newcpy = cpy.copy()
print("original: ",cpy)
print("copy: ",newcpy)