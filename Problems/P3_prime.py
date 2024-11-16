# Q3. to check no. is prime or not 

n = int(input("Enter number: "))

for i in range(2,n):
    if(n%i) == 0:
        print("Not a prime number")
        break
else:
    print("Its a prime number")