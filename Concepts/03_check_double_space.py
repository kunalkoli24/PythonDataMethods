# name = "python is easy language"
# print(name.find("  ")) 
# in this we dont have double space, so it will return -1 rather if double space is found then return the index of it
# a = "python is easy  language"
# print(a.find("  ")) # as string consists of spacing,will return index value as 14


# print(name.find("easy")) # also find any word existing in the string and will give its index position



# To replace double space by single 

b = "python is easy  language"
print(b.replace("  "," "))