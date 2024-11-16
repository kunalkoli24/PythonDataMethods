# find factorial of a number using for loop 

n = int(input("Enter number: "))
product = 1
for i in range(1, n+1):
    product = product * i
print(f"Factorial of {n} is {product}")
