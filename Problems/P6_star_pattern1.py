# Q6. program to print star pattern 
'''  

  *
 ***
*****
n=3
'''

n = int(input("Enter number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")