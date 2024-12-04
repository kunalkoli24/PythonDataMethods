class Employee:
    language = "py"  # this is class attribute
    salary = 12000

k1 = Employee()    # k is an object 
print(k1.language, k1.salary)    # o/p: py 12000

k2 = Employee()
k2.language = "Javascript"   # this is an instance attribute
print(k2.language, k2.salary)   #o/p: Javascript 12000