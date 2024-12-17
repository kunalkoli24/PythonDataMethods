# try:
#     a = int(input("enter number:"))
#     print(a)

# except Exception as e:
#     print(e)


# finally:
#     print("Inside else block")

# what's the use of finally if we can directly use print as finally block means it will run no matter what condition is

# Note:  its used in function 
# Note: if you mention return inside try and not mentioned finally then print  will not work

def main():
    try:
        a = int(input("enter number:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return


   
    print("Inside finally ")

main()


# o/p if finally is not mentioned 

# enter number:4
# 4
# enter number:sfsf
# invalid literal for int() with base 10: 'sfsf'

def main():
    try:
        a = int(input("enter number:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return


    finally:
        print("Inside finally ")

main()

# o/p if finally is mentioned 
# enter number:4
# 4
# Inside finally 

# enter number:jdsbf
# invalid literal for int() with base 10: 'jdsbf'
# Inside finally 