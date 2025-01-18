# function created using an expression using 'lambda' keyword 
# syntax :
    # lambda x: expression 
# lambda which will take argument x and (:) perform expression 

# example 1:  squaring number

def square(n):
    return n*n
print(square(5))

# using lambda 
 
square = lambda n : n*n
print(square(5))


# example 2  addition of 3 numbers

add = lambda a,b,c : a+b+c
print(add(3,6,4))
