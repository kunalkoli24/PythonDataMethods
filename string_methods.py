# Strings

# 1. len() 
l = [2,90,54,22,67]
print(len(l))

# 2. upper() (Converts all characters in the string to uppercase.)
u = "hello world"
print(u.upper())

# 3. lower() (Converts all characters in the string to lowercase.)
l = "HELLO WORLD"
print(l.lower())

# 4. capitalize()  (Capitalizes the first character of the string.)
u = "hello world"
print(u.capitalize())

# 5. title() (Converts the first character of each word to uppercase.)
t = "hello world"
print(t.title())

# 6. replace() (Replaces occurrences of a substring with a new substring.)
r = "Hello World"
print(r.replace("World", "Python"))

# 7. count() (Counts the occurrences of a substring in the string.)
o = "Hello  Hello World"  # case sensitive
print(o.count("Hello"))

# 8. strip() (Removes any leading and trailing whitespace from the string.)
s = "  Hello World "
print(s.strip())

# 9. lstrip() and rstrip() 

# - lstrip()
ls = "  Hello   "
print(ls.lstrip())

# - rstrip()
rs = "  Hello   "
print(rs.rstrip())

# 10. startswith(prefix) and endswith(suffix)
text = "hello world"   # case sensitive
print(text.startswith("hello"))  # Output: True
print(text.endswith("world"))    # Output: True
print(text.endswith("python"))    # Output: False

# 11. join()
text = "hello","world"
print(" ".join(text))

# 12. swapcase() (Swaps uppercase characters to lowercase and vice versa.)
s = "HeLlOw  wOrLd"
print(s.swapcase())  # o/p: hElLoW  WoRlD

# 13. find()  (Returns the index of the first occurrence of the substring, or -1 if not found.)
f = "Hello World"
print(f.find("Hello")) # o/p index 0, as Hello is present.
print(f.find("python")) # o/p index -1, as python is not present.