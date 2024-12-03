# Q1. program to print multiplication table of a given no. using for and while loop

# for loop 

n = int(input("Enter number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n * i}")

# while loop 
n = int(input("Enter number: "))

i=1
while(i<11):
    print(f"{n} X {i} = {n * i}")
    i +=1


# Q2. greet person whos name start with s stored in the list 

l = ["kunal", "Sanchit", "Sanket", "Prakesh"]
for name in l:
    if(name.startswith("S")) :
        print(f"Hello {name}")