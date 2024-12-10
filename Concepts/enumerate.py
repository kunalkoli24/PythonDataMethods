
# regular method: 

l = [3,44,32,55]

index = 0
for item in l:
    print(f"item at index{index} is {item}")
    index += 1

# o/p:
# item at index0 is 3
# item at index1 is 44
# item at index2 is 32
# item at index3 is 55

# using Enumerate 

for index, item in enumerate(l):
    print(f"item at index{index} is {item}")

# o/p:
# item at index0 is 3
# item at index1 is 44
# item at index2 is 32
# item at index3 is 55