# a program should not get crashed even its worng. 
# for this we use exception handling i.e "try"

# case 1: 

# a = int(input("enter number:"))
# print(a)
# if we enter a number it will print it without any error 
# but if we enter a string, it will give an error 

# So to avoid error even if we enter string we can use try 

try:
    a = int(input("enter number:"))
    print(a)

except Exception as e:
    print(e)

print("program ended")

# o/p:    enter number:k
#         invalid literal for int() with base 10: 'k'
#         program ended
# Now it will not throw an error it will give  what you have entered 4