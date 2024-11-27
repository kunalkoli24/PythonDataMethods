# Group of statements is caleedd as function
# Fun can be reused by programmer in a given program any number of times 
# Syntax to define a function 

# we use def followed by function name and opening and closing parenthesis. user can give any name of the function 

def fun():  # here function name is fun()
    print("Hello")

fun()   # function is been  called here. Without function call the function will not execute the code. 



# simple example of taking average of 3 numbers using function 

a= 23
b= 44
c= 55

def avg():
    print((a + b + c)/3)
avg()

# Let user give the number 
def avg():
    num1 = int(input("Enter  number1: "))
    num2 = int(input("Enter  number2: "))
    num3 = int(input("Enter  number3: "))

    print((num1+num2+num3)/3)
avg()

print("Program is over")

print("Go Ahead With More Numbers!!!")
avg() # function can be used any number of times in the code. 

# Quick_Quiz

# program to greet user using fun 

name = input("Enter Your Name: ")

def greet():
    print("Hye, Nice To See You",name)
greet()