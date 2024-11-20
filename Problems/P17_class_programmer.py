# create class "programmer" which stores information of few programmer working at microsoft. 

class programmer:
    company ="Microsoft"

    def __init__(self, name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

k = programmer("kunal", 120000, 41121)
print(k.name,k.salary,k.company,k.pincode)

p = programmer("pushkar", 110000, 41011)
print(p.name,p.salary,p.company,p.pincode)

s = programmer("surve", 100000, 41001)
print(s.name,s.salary,s.company,s.pincode)

m = programmer("param", 121000, 410021)
print(m.name,m.salary,m.company,m.pincode)

