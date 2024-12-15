# We use try_else if we want to run a code when try was succesful 


try:
    a = int(input("enter number:"))
    print(a)

except Exception as e:
    print(e)


else:
    print("Inside else block")

# if try block is correctly run then  it goes inside else block 
# otherwise in exception block 

# o/p:
# if try block runs correctly:
# enter number:4
# 4
# Inside else block

# if does not run correctly:
# enter number:sffsdf
# invalid literal for int() with base 10: 'sffsdf'