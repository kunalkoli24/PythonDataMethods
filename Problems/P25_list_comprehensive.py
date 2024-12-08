# to print a list contains multiplication of entered number using list comprehensive

n = int(input("Enter number: "))

table = [n*i for i in range(1,11)]
print(table)