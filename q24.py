def list():
    i=0
    c=[]
    while i<=user:
        b=i*user
        i+=1
        c.append(b)
    print(c)
user=int(input("any number"))
list()
