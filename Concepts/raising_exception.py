# We can raise our custom erro 
# e.x dividing by 0 error 

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if(b == 0):
    raise ZeroDivisionError("Cannot divide number by zero!")

else:
    print(f"division is {a/b}")

# # o/p:
# Enter first number:5
# Enter second number:0
# ZeroDivisionError: Cannot divide number by zero!