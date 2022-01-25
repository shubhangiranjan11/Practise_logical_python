list=["s","d","f","s","d","f","s","f","k","o","p","i","w","e","k","c"]
f=0
c=0
k=0
w=0
i=0
while i<len(list):
    if list[i] == "f":
        f+=1
    if list[i] == "c":
        c+=1
    if list[i] == "k":
        k+=1
    if list[i] == "w":
        w+=1
    i+=1
print("in this list f is",f)
print("in this list c is",c)
print("in this list k is",k)
print("in this list w is",w)
