# for i in range(4):  # (4) automatically indicate as (0,4)
# # range will print from 0 to n-1 i.e 4 
#     print(i)

# Q. to print content of list using for loop 

li = [3,6,4,7,"kunal","pushkar"]

for i in li:
    print(i)

# Q. to print content of tuple using for loop 
t = (3,766,43,55,22,99)
for i in t:
    print(i)

# Q. to print content of string using for loop

s = "kunal"
for i in s:
    print(i) 

## for loop with else

l = [22,43,13,54]
for i in l:
    print(i)
else:
    print("Done")