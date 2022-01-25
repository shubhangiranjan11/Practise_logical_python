# def sum(a,b):
#     c=a+b
#     print(c)
#     return c
# sum(9,6)


a="hello"
i=0
while i<len(a):
    if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u":
        c=i*2
        print(c,end="")
    else:
        print(a[i],end="")
    i+=1



