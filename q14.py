# list=[4, 6, 4, 3, 3, 4, 3, 7, 8, 8] 
# k=2
# res=[]
# i=0
# while i<len(list):
#     count=list.count(i)
#     if count>k and i not in res:
#         res.append(i)
#     i+=1
# print(res)

li = [12,34,56]
i= 0
l=[]
while i <len(li):
    s =0 
    a = li[i]
    while a>0:
        r = a%10
        s = s+r
        a = a//10
    i=i+1
    l.append(s)
print(l)
