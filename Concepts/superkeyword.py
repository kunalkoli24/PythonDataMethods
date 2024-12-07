# # super keyword() 
# if a constructor of child class is running and we want constructor of its parent class should also run then
# we can use super keyword()

class Employee():
    def __init__(self):
        print("constructor of employee class")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("constructor of programmer class")
    b = 2

class coder(Programmer):
    def __init__(self):
        super().__init__()
        print("constructor of coder class")
    c = 3 

p = Employee()
print(p.a) 
# o/p: constructor of employee class
#      1


p = Programmer()
print(p.a,p.b) 
# o/p: constructor of programmer class
#      1 2

p = coder()
print(p.a,p.b,p.c) 
# o/p: constructor of coder class
#      1 2 3 

# if i want constructor of programmer class should also run in coder class 
# we can use super (super().__init__()) in coder class 
# so along with the coder class constructor of programmer class will also been called 

p = coder()
print(p.a,p.b,p.c) 
# o/p: 
# constructor of programmer class
# constructor of coder class
# 1 2 3