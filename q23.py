def number(n):
    a=str(n)
    i=0
    while i<len(a):
        if a[-i]=="0":
            v=(int(a[:-i]))
        i+=1
    print(v)
number(19000)



# def table():
#     i=1
#     sum=0
#     while i<=limit:
#         if i%3==0 or i%5==0:
#             k=i
#             print(k)
#             sum=sum+k
#         i+=1
#     print(sum)
# limit=int(input("any number"))
# table()






# def limit():
#     user=int(input("any number"))
#     i=2
#     while i<user:
#         j=2
#         c=0
#         while j<i:
#             if i%j==0:
#                 c+=1
#             j+=1
#         if c==0:
#             print(i,"prime number")
#         else:
#             print(i,"not prime number")
#         i+=1
# limit()



# a=[1,2,3,[4,7,[6],9,1]]
# i=0
# while i<len(a):
#     b=[]
#     j=0
#     while j<len(a):
#         if a[j] not in b:
#             k=a[j]
#             b.append(k)
#         j+=1
#     i+=1
# print(b)
