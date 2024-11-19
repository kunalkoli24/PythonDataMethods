# to find gretest number using function 

# a= 99
# b= 6
# c= 45

# def greatest():
#     if(a>b and a>c):
#         print(f"a is greater = {a}")
#     if(b>a and b>c):
#         print(f"b is greater = {b}")
#     if(c>a and c>b):
#         print(f"c is greater = {c}")
# greatest()


# using return 
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
print(greatest(22,45,2))