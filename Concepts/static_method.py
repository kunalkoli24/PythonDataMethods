class Employee:
    language = "py"  # this is class attribute
    salary = 12000

    def getinfo(self):
        print(f"the language is {self.language} and salary is {self.salary}")

    @staticmethod  # means greet is a staic method and it do not need any object
    def greet():
        print("Good Morning")

k2 = Employee()
k2.language = "Javascript"   
k2.greet()
# print(k2.language, k2.salary)   

k2.getinfo() 