# We also can pass arguments to the functions 

# single argument pass:

def greet(name):
    print("Hello", name)

greet("virat")  # o/p: Hello Kunal

# here function greet takes single argument as name. 
# We have mention a name "kunal" while fun call. So it will assign to the argument pass to fun i.e "name" 
# And as we print hello along with name, it will print hello kunal 


# Multiple argument:  

# We can also pass multiple arguments to the function 
def greet(name, surname):
    print("Hello", name, surname)

# greet("virat","Kohli")

# Here we have two arguments (name and surname) pass to function 
# We have pass name as kunal and surname as koli while calling function call. 


# - Return value in function 

# A function may return something called as return value 

def rtn(name):
    print("Hello", name)

a = rtn("virat")
print(a) # here o/p will be "none". As "a" is not returning anything. 

def rtn(name):
    print("Hello", name)
    return "GOAT"
a = rtn("virat")
print(a)
# now a will return "GOAT"
# Whenever fun return something, it is assign to a variable. 
# here return value is assign to variable a, so it will return "GOAT"


# - Default Argument 

def greet(name, ending="GOD"):
    print(f"Hello {name}")
    print(ending)
greet("virat")

# Here we have defined "GOD" as a default argument to ending. 
# If we do not give any ending parameter then it will take "GOD" as a default parameter. 
# But if we have pass an ending parameter then it will print that and not "GOD". 
# example:

#  greet("virat" ,"best player")
# here we have given an ending parameter as "best player", Now function will print "best player" for ending parameter and not "GOD".