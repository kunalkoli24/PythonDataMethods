# print infinite if number is been divided by 0 

try:
    a = int(input("Enter number a :"))
    b = int(input("Enter number b :"))
    print(a/b)

except ZeroDivisionError as z:
    print("Infinite")