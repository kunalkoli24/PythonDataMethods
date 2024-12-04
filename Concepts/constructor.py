# __intit__(self) 

class Employee:
    language = "py"  # this is class attribute
    salary = 12000

    def __init__(self, name,salary, language): # called as "dunder method" which is automatically called. 
        self.name = name
        self.salary = salary
        self.language = language
        print("creating an object and will be called when a every new object is created")

k1 = Employee("kunal", 120000, "javascript")  
# k1.language = "javascript"   
print(k1.name, k1.salary ,k1.language)   

# Another method instaed of this : k1.language = "javascript"   



