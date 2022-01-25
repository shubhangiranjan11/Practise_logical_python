# var=[[12,23,4],[45,56,78],[5,6,7]]
# i=0
# b=[]
# while i<len(var):
#     b.extend(var[i])
#     i+=1
# print(b)



var=[[12,23,4],[45,56,78],[5,6,7]]
i=0
b=[]
while i<len(var):
    j=0
    while j<len(var[i]):
        if var[i] not in b:
            b.append(var[i][j])
        j+=1
    i+=1
print(b)

i=0
while i<len(b):
    j=0
    while j<len(b):
        if b[i]<b[j]:
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
        j+=1
    i+=1
print(b)
