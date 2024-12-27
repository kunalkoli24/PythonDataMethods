# Represented by ":=" 
# Introduced in python 3.8 
# Allows you to assign values to variables as part of an expression 
# Officially called as "Assignment Expression" 

if(n := len([1,2,3,4,5])) > 3:
    
    print(f"List is too long ({n} elements, expected <= 3)")

else:
    
    print("List is >= 3")