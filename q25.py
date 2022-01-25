list=[1,2,3,4,5,6]
b=[]
i=0
while i<len(list):
    if list[i] not in b:
        # b.append([i])
        i+=1
    b.append(i)
print(b)

