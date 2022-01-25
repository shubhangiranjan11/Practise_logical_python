input=[1,2,3,4,5]
j=[]
n=[]
y=(input[:3])
b=(input[3:])
j.append(y)
n.append(b)
# print(j,n)
j.extend(n)
print(j)

