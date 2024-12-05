class Employee:
    language = "py"  # this is class attribute
    salary = 12000

    def getinfo(self):
        print(f"the language is {self.language} and salary is {self.salary}")

k2 = Employee()
k2.language = "Javascript"   # this is an instance attribute
print(k2.language, k2.salary)   #o/p: Javascript 12000

k2.getinfo() # o/p: the language is Javascript and salary is 12000
# if  we comment out lind no. 9 then output will be the language is python and salary is 12000