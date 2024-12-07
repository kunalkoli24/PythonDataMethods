# - single inheritance:
# Occurs when child class inherits only a single parent class 


class parent():
    company = "BNY"
    # def show(self):
    #     print(f"name of employee is {self.name} and salary is {self.salary}")

class child(parent):
    company = "Cybage"
    # def showlanguage(self):
    #     print(f"name is {self.name} and good with {self.language} language")
    
 
a = parent()
b = child()
print(a.company,b.company)
 