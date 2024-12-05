# - Multiple inheritance 
# Occurs if child class inherits from more than on eparent class 

class parent1():
    company = "BNY"
    def show(self):
        print(f"name of employee is {self.company} ")

class parent2():
    language = "javscript"
   
    def lan(self):
        print(f"the language is {self.language}")

class child(parent1, parent2):
    position = "tech lead"
    name = "abc"
    # def pos(self):
    #     print(f"position is {self.position}")

a = child()
# a.show()
# a.lan()
print(a.name,a.company,a.language,a.position)
 