# Q7. program to print star pattern 
'''

*
**
***

'''

n = int(input("Enter number: "))
for i in range(1, n+1):
    print("*"* i, end="")
    print("")