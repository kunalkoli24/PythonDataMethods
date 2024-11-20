# program to convert inch to cm

def inch_to_cm(n):
    if(n==0):
        return
    return n * 2.54
n = int(input("Enter Number in inch: "))
print(f"Number in centimeter is: {inch_to_cm(n)}cm")