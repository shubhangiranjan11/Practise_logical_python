list1=[[7,8,9,5],[6,2,4,5],[8,5,7,5]]
empty=[]
main=5
i=0
while i<len(list1):
    j=0
    while j<len(list1[i]):
        if main == list1[i][j]:
            empty.append(main)
        j+=1
    i+=1
print(empty)
c=0
sum=0
while c<len(empty):
    sum=sum+empty[c]
    c+=1
print(sum)

