f = open("Files_I-O/appendfile.txt","a")
data = "\tuse of append method"  
# append method will add the line at end of the file content and as code runs again,
# it will add that number of times.
f.write(data)
f.close()