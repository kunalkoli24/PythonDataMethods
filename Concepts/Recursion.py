# Recursion means fucntion calling function or itself. 

# Example for recursion is "factorial of a number "

# factorial(n) = n * factorial(n-1)

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter The Number: "))
print(f"Factorial is {factorial(n)}")                           