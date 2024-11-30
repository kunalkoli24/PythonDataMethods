# Another way to operate file. 
# We don't have to explicitly close the file 

with open("Files_I-O/openfile.txt") as f:
    print( f.read())