# it will terminate the loop when condition is true 

for i in range(100):
    if(i==35):
        break  # exit the loop as soon we get 35. No matter range is till 100.
    print(i)

## continue

for i in range(100):
    if(i==35):
        continue  # skip this iteration (i=1 is an iteration). so it will skip for 35 and we look from 36.
    print(i)

## pass
for i in range(100):  # if i want to work later in this loop and want to execute next loop (while loop ), use pass
    pass

i=0
while(i<33):
    print(i)
    i +=1