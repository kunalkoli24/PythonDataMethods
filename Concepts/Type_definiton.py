# Types hints are added using colon (:) syntax for variables. 
# syntax for function return types are "->" 

# - Variable type hint (:)

age : int = 22

# here we are telling py that my age will be an integer 
# now when we will perform 
# "age." -> it will give all integer methods 

name : str = "python"

# here we are telling py that my name will be an str
# now when we will perform 
# "name." -> it will give all str methods 


# - Funtion type hint (->) 

def sum(a : int ,b : int) -> int:
    return a + b
# it specifies that a and b both will except int and will return int "(a : int ,b : int) -> int"

print(sum(10,8))
