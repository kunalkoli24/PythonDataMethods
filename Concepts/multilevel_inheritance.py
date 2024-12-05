# - Multilevel inheritance 
# When a child class becomes a parent for another child class 

class Employee():
    a = 1

class Programmer(Employee):
    b = 2

class coder(Programmer):
    c = 3 

p = Employee()
print(p.a) #o/p: 1
# print(p.b)  #o/p errro: 'Employee' object has no attribute 'b'

p = Programmer()
print(p.a,p.b) # o/p: 1 2  as programmer inherits from employee

p = coder()
print(p.a,p.b,p.c)  # o/p: 1 2 3    as coder inherits from programmer.