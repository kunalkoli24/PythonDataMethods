# print third, fifth and seven element from list using enumerate 
l = [3,7,2,8,6,9,10,1,5]

for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)