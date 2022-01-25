a="Hello"
# i=0
# while i<len(a):
#     if a[i]=="e" or a[i]=="o":
#         p=i
#         e=(p*2)
#         s=a.replace(a[i],str(e))
#         print(s)
#     i+=1



i=0
while i<len(a):
    if a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u":
        p=i*2
        b=a.replace(a[i],str(p))
        print(b)
    i+=1


# i=0
# while i<len(a):
#     if a[i] == "e" or a[i] == "o":
#         p=a.find(a[i])
#         print(p*2)
#     i+=1


