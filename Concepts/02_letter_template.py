name = input("Enter Name: ")
date = int(input("Enter date: "))

print(f''' Dear {name} \n You Are Selected!! \n Date: {date}''')

# Or by Replace method

letter = '''
Dear <name>,
Your Selected!
<date>
'''

print(letter.replace("<name>","Kunal").replace("<date>","09 November")) 
# can use multiple replace. called chaining 