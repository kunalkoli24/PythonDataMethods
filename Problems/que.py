# # Q1. find greatest of four no.s entered by users
a1 = int(input("Enter Number a1: "))
a2 = int(input("Enter Number a2: "))
a3 = int(input("Enter Number a3: "))
a4 = int(input("Enter Number a4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest is a1:",a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest is a2:",a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest is a3:",a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("Greatest is a4:",a4)

print("End Of Program")


# Q2. find if student has passed or failed if it requires a toal of 40% 
# and at least 33% in each subject to pass (Assume 3 sub and take marks from user)

m1 = int(input("Enter marks of sub1: "))
m2 = int(input("Enter marks of sub2: "))
m3 = int(input("Enter marks of sub3: "))

# check for total percentage

total_percentage = (100*(m1 + m2 + m3))/300

if(total_percentage >= 40 and m1>=33 and m2>=33 and m3>=33):
    print("You Are Passed: ", total_percentage)

else:
    print("You Are Failed: ", total_percentage)


# Q3. if these words occur in user statement then it must detect that it is a spam message
# "Make a lot of money", "buy now", "subscribe this", "click this link"

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this link"

comment = input("Enter the message:")

if((p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    print("This is a spam comment")

else:
    print("Not spam")


# Q4. find whether given username contains less than 10 charater

name = input("Enter Username:" )

if(len(name)<10):
    print("Less than 10 character")

elif(len(name)==10):
    print("Equal to 10 character")

else:
    print("Greater than 10 character")

# Q5. find name is present in the list

li = ["kunal", "param", "surve","pushkar"]
name = input("Enter name to search: ")

if(name in li):
    print("Name is present in the list")

else:
    print("Name is not in the list")


# Q6. according to marks enter,display the grade

mark = int(input("Enter mark:"))

if(mark<=100 and mark>90):
    grade = "EX"

elif(mark<=90 and mark>80):
    grade = "A"
elif(mark<80 and mark>70):
    grade = "B"
elif(mark<70 and mark>60):
    grade = "C"
elif(mark<60 and mark>50):
    grade = "D"
elif(mark<50 ):
    grade = "F"

print("Your Grade is: ", grade)

# Q7. Does post is talking about "python"

word = input("Enter word: ")
post = "python is the easiest language compare to other languages"

if(word.lower() in post.lower()):
    print("Yes, post is talking about python")

else:
    print("No, post is No talking about python")