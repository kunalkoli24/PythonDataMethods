# remove word from list and strip at same time 

# to remove word
def rem(l, word):
    for item in l:
        l.remove(word)
        return l    

l= ["c++", "java", "od"]
print(rem(l, "od"))

# to remove word and strip at same time 
def rem(l, word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n    

l= ["c++", "good", "od"]
print(rem(l, "od"))

