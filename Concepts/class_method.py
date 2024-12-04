# class method is the method which "bound to class" and "not the object of class "
# "@classmethod" decorator is used to create a class method 

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"attribute of class a is {cls.a}")

e= Employee()
e.a = 45
e.show()

# o/p: attribute of class a is 45. as it is instance attribute 
# if we want it should take class attribute we should add "@classmethod"

# After adding it the o/p will be : attribute of class a is 1 