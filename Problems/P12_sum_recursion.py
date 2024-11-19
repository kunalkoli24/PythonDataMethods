# to sum first n natural numbers using recursion 

def sum(n):
    if(n==1):
        return 1
    return  sum(n-1) + n
n = int(input("Enter numbers: "))

print(f"sum: {sum(n)}")