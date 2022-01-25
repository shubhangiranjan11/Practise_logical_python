# grocery_list=["flour","cheese","carrots"]
# i=0
# while i<len(grocery_list):
#     print(i,grocery_list[i])
#     i+=1


list1=[["g","f","g"],["f","s"],["b","e","s","t"]]
empty=[]
i=0
while i<len(list1):
    j=0
    while j<len(list1[i]):
        if list1[i] not in empty:
            empty.append(list1[i][j])
        j+=1
    i+=1
print(empty)